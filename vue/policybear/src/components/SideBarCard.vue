<template>
  <b-card class="shadow m-2 border-0 rounded-lg">
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
  </b-card>
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
  props: ['request', 'meta'],
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

</style>
