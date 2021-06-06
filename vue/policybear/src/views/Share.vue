<template>
  <b-container style="min-height:80vh;">
    <div class="mx-auto shadow rounded mt-5 py-2 d-flex flex-wrap justify-content-center" style="max-width:900px">
      <div class=""><b-button @click="copyLink()" variant="border-0" class="nord-btn w-100"><b-icon-files class="mr-1"/>Copy link to clipboard</b-button></div>
      <!--<div class=""><b-button @click="copyText()" variant="border-0" class="nord-btn w-100"><b-icon-files class="mr-1"/>Copy text to clipboard</b-button></div>-->
      <div class=""><b-button @click="downloadImage()" class="nord-btn w-100" variant="border-0"><b-icon-file-earmark-image class="mr-1"/>Download as image</b-button></div>
      <div class=""><b-button @click="downloadPDF()" variant="border-0" class="nord-btn w-100"><b-icon-file-earmark-richtext class="mr-1"/>Download as PDF</b-button></div>
      <div class=""><b-button @click="editCard()" variant="border-0" class="nord-btn w-100"><b-icon-pencil-square class="mr-1"/>Customize in editor</b-button></div>
    </div>
    
    <div ref="print" id="print" class="mx-auto mb-5" style="max-width:750px">
        <argument-card v-if="request" :request="request" class="pt-4 pb-2 px-4 mx-auto" :light="true" style="max-width:700px"/>
        <argument-card v-else class="pt-4 pb-2 px-4 mx-auto" :light="true" style="max-width:700px"/>
    </div>
  </b-container>
</template>

<script>
import store from '../store.js'

import html2pdf from 'html2pdf.js'
import Vue2Img from 'vue-2-img'
import 'vue-2-img/dist/vue-2-img.css'
import ArgumentCard from '../components/ArgumentCard.vue';

export default {
  name: 'Share',
  components: {
    ArgumentCard,
  },
  data() {
    return {
      request : null,
    }
  },
  computed: {
    datasets() {
      return store.datasets; 
    },
  },
  methods: {
    editCard() {
      if (this.request != null) {
        store.cardRequest = this.request;
      }
      this.$router.push('/editor/')
    },
    copyText() {
      const text = this.$refs.print.cardContent.innerHTML
      console.log(text)
      this.copyToClipboard(text);
    },
    copyLink() {
      const url = String(window.location);
      console.log(url)
      const base = url.substring(0, url.indexOf('share/') + 'share/'.length);
      console.log(base)
      const req = this.request ? this.request : store.cardRequest;
      this.copyToClipboard(`${base}${JSON.stringify(req)}`);
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
    //this.fetchDataSets();
    if (this.$route.params.request) {
      this.request = JSON.parse(this.$route.params.request)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>

