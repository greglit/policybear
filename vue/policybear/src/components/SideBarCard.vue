<template>
  <div class="shadow m-2 border-0 rounded-lg bg-white p-lg-3 p-2" ref="container">
    <div class="w-50 d-inline-block px-1"><b-button v-b-modal.modal-cutomize class="toggle-form nord-btn w-100" variant="border-0"><b-icon-brush-fill/></b-button></div>
    <div class="w-50 d-inline-block px-1"><b-button :to="`card/${JSON.stringify(request)}`" variant="border-0" class="nord-btn w-100" v-if="requestIsValid"><b-icon-share-fill/></b-button></div>
    <b-modal id="modal-cutomize" class="modal-form" hide-footer>
      <data-form :requestData.sync="d_request.data" :meta="meta" change2/>
      <hr>
      <styling-form :requestStyling.sync="d_request.styling" :requestData="d_request.data" :meta="meta"/>
    </b-modal>
    <!--<b-modal id="modal-share" class="modal-form" hide-footer>
      <b-container ref="container" class="m-0 p-0">
        <b-form-group label-size="sm" label="Share as Link">
          <b-input-group>
            <b-input-group-prepend>
              <b-button disabled variant="info">
                <b-icon-link45deg/>
              </b-button>
            </b-input-group-prepend>
            <b-form-input disabled v-model="cardurl"></b-form-input>
            <b-input-group-append>
              <b-button variant="info" @click="copyToClipboard(cardurl)">
                <b-icon-files/>
                Copy
              </b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
        <hr>
        <div class="w-50 d-inline-block px-1"><b-button @click="downloadImage()" class="nord-btn w-100" variant="border-0"><b-icon-file-earmark-image class="mr-1"/>Download as Image</b-button></div>
        <div class="w-50 d-inline-block px-1"><b-button @click="downloadPDF()" variant="border-0" class="nord-btn w-100"><b-icon-file-earmark-richtext class="mr-1"/>Download as PDF</b-button></div>
      </b-container>    
    </b-modal>-->
    <div class="card-form">
      <hr>
      <b-button v-b-toggle.data-form variant="border-0" class="nord-btn rubik-medium w-100 text-left pl-0">
        Change Data
        <b-icon-chevron-up class="when-open float-right" /><b-icon-chevron-down class="when-closed float-right"/>
      </b-button>
      <b-collapse id="data-form" class="mt-2 ml-2">
        <data-form :requestData.sync="d_request.data" :meta="meta" change/>
      </b-collapse>
      <hr>
      <b-button v-b-toggle.style-form variant="border-0" class="nord-btn rubik-medium w-100 text-left pl-0">
        Change Appearance
        <b-icon-chevron-up class="when-open float-right" /><b-icon-chevron-down class="when-closed  float-right"/>
      </b-button>
      <b-collapse visible id="style-form" class="mt-2 ml-2">
        <styling-form :requestStyling.sync="d_request.styling" :requestData="d_request.data" :meta="meta"/>
      </b-collapse>
    </div>
  </div>
</template>

<script>
import StylingForm from './StylingForm.vue';
import DataForm from './DataForm.vue';



export default {
  name: 'SideBarCard',
  components: {
    StylingForm,
    DataForm
  },
  props: ['request', 'meta', 'requestIsValid'],
  data() {
    return {
      d_request : this.request,
    }
  },
  watch: {
    d_request: {
     handler(val){
       this.$emit('update:request', this.d_request);
     },
     deep: true
  	}
  },
  computed: {
    /*cardurl() {
      const url = String(window.location)
      const strRequest = JSON.stringify(this.request);
      return `${url}card/${strRequest}`;
    }*/
  },
  methods: {
  },
  
}
</script>

<style lang="scss" scoped>

.collapsed > .when-open,
.not-collapsed > .when-closed {
  display: none;
}

.card-form {
  display: inline;
}

.toggle-form {
  display: none !important;
}

@media (max-width: 992px) {
  .card-form {
    display: none !important;
  }
  .toggle-form {
    display: inline !important;
  }
}

.modal-form{
  border: none !important;
  background-color: transparent !important;
}

</style>
