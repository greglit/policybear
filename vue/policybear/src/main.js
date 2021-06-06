import 'vue-resize/dist/vue-resize.css'
import 'leaflet/dist/leaflet.css';

import Vue from 'vue'
import App from './App.vue'
import router from './router'

import VueResize from 'vue-resize'
Vue.use(VueResize)

import VueSmoothScroll from 'vue2-smooth-scroll'
Vue.use(VueSmoothScroll)

Vue.config.productionTip = false

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import VueClipboard from 'vue-clipboard2'
//VueClipboard.config.autoSetContainer = true // add this line
Vue.use(VueClipboard)

import store from './store.js';

Vue.mixin({
  methods: {
    month(number) {
      const months = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ];
      return months[number];
    },
    capitFirstChar(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    makeToast(message) {
      this.$bvToast.toast(message, {
        //title: ``,
        autoHideDelay: 2000,
        appendToast: false,
        variant: 'success',
        toaster: 'b-toaster-top-full',
        solid: true,
        headerClass: 'd-none'
      })
    },
    copyToClipboard(value) {
      let container = this.$refs.container
      this.$copyText(value, container).then((e) => {
        this.makeToast(`Copied ${value} to the clipboard!`);
      }, (error) => {
        console.log('failed to copy:'+e)
      })
    },
    withPoints(num) {
      return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.')
    },
  }
})


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
