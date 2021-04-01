<template>
  <b-container style="min-height:80vh;">
    <div class="mx-auto shadow rounded mt-5 p-2" style="max-width:750px">
      <div class="w-36 d-inline-block px-1"><b-button @click="copyLink()" variant="border-0" class="nord-btn w-100"><b-icon-files class="mr-1"/>Copy link to clipboard</b-button></div>
      <div class="w-36 d-inline-block px-1"><b-button @click="downloadImage()" class="nord-btn w-100" variant="border-0"><b-icon-file-earmark-image class="mr-1"/>Download as image</b-button></div>
      <div class="w-36 d-inline-block px-1"><b-button @click="downloadPDF()" variant="border-0" class="nord-btn w-100"><b-icon-file-earmark-richtext class="mr-1"/>Download as PDF</b-button></div>
    </div>
    
    <div ref="print" id="print" class="mx-auto mb-5" style="max-width:750px">
        <argument-card v-if="datasets && request" :request="request" :meta="datasets[request.data.param]" class="pt-4 pb-2 px-4 mx-auto" light="true" style="max-width:700px"/>
    </div>
  </b-container>
</template>

<script>
import html2pdf from 'html2pdf.js'
import Vue2Img from 'vue-2-img'
import 'vue-2-img/dist/vue-2-img.css'
import ArgumentCard from '../components/ArgumentCard.vue';

export default {
  name: 'Card',
  components: {
    ArgumentCard,
  },
  data() {
    return {
      datasets : null,
      request : null,
    }
  },
  methods: {
    fetchDataSets() {
      console.log(`${this.apiURL}datasets/`);
      fetch(`${this.apiURL}datasets/`, {})
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data);
        this.datasets = data;
      })
      .catch((error) => {
        console.log(error);
        this.fetchDataSets();
      });
    },
    copyLink() {
      const url = String(window.location);
      const base = url.substring(0, url.indexOf('card/') + 'card/'.length);
      console.log(base)
      this.copyToClipboard(`${base}${JSON.stringify(this.request)}`);
    },
    downloadPDF() {
      console.log('print')
      let element = this.$refs.print;
      console.log(element)
      html2pdf(element);
    },
    downloadImage() {
      this.$bvModal.hide('modal-share')
      console.log(document.querySelector('#print'))
      let config = {
        target: '#print',
        captureHiddenClass: 'vti__hidden',
        captureShowClass: 'vti__show',
        captureActiveClass: 'vti__active',
        fileName: 'PolicyBear',
        fileType: 'png',
        returnAction: 'download', // blob, base64, canvas, clipboard, newWindow
        callback: (img) => { return img } // modifies what image is returned
      }
      vue2img().image(config);
    }
  },
  created() {
    this.fetchDataSets();
    this.request = JSON.parse(this.$route.params.request)
  }
}
</script>

<style lang="scss" scoped>

</style>

