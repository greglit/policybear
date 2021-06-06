<template>
  <div>
    <section class="bg-nord3 pb-5">
      <b-container fluid class="full-height">
        <navbar showIcon bgDark sm class="ml-2"/>
        <b-row class="">
          <b-col cols="12" lg="5" class="mt-2 text-left card-form">
            <side-bar-card style="min-width:100px;" :requestIsValid="requestIsValid"/>
          </b-col>
          <b-col cols="12" lg="7" class="w-100">
            <div v-if="requestIsValid" id="policy-argument-card" class="my-5 mx-4 mx-lg-2 y-center">
              <argument-card ref="argument" style="margin-top:-50px;"/>
            </div>
            <h4 v-else class="text-center rubik-medium y-center txt-nord6">Please fill out missing fields to generate a card.</h4>
          </b-col>
        </b-row>
      </b-container>
    </section>
  </div>
</template>

<script>
import store from '../store.js'

import ArgumentCard from '../components/ArgumentCard.vue'
import DataForm from '../components/DataForm.vue';
import Navbar from '../components/Navbar.vue';
import SideBarCard from '../components/SideBarCard.vue';
import WaveSeperator from '../components/WaveSeperator.vue';

import LeafletMap from '../components/LeafletMap.vue';


export default {
  name: 'Editor',
  components: {
    ArgumentCard,
    Navbar,
    DataForm,
    SideBarCard,
    WaveSeperator,
    LeafletMap,
  },
  data() {
    return {
      request : {
        data : {
          param : null,
          station : null,
          startDateYear : null,
          startDateMonth: null,
          endDateYear : null,
          endDateMonth : null,
          dateFormat : 'annual',
        },
        styling : {
          wording : 'difference',
          theme : 'classic',
          compareTo : null,
        }
      },
    }
  },
  methods: {
    downloadImage() {
      this.$bvModal.hide('modal-share')
      console.log(document.querySelector('#policy-argument-card'))
      let config = {
        target: '#policy-argument-card',
        captureHiddenClass: 'vti__hidden',
        captureShowClass: 'vti__show',
        captureActiveClass: 'vti__active',
        fileName: 'ImageCapture',
        fileType: 'png',
        returnAction: 'download', // blob, base64, canvas, clipboard, newWindow
        callback: (img) => { return img } // modifies what image is returned
      }
      vue2img().image(config);
    },
    downloadPDF() {
      console.log('print')
      let element = this.$refs.argument;
      console.log(element)
      html2pdf(element);
    },
  },
  computed: {
    datasets() {
      return store.datasets;
    },
    requestIsValid() {
      const data = store.cardRequest.data;
      return Boolean(data.param 
          && data.startDateYear 
          && data.endDateYear 
          && (data.startDateMonth && data.endDateMonth || data.startDateMonth == null && data.endDateMonth == null));
    },
    
  },
  async created() {
  },
}
</script>

<style lang="scss" scoped>

</style>

