import Vue from 'vue'
import App from './App.vue'
import router from './router'

import 'leaflet/dist/leaflet.css';

import VueSmoothScroll from 'vue2-smooth-scroll'
Vue.use(VueSmoothScroll)

Vue.config.productionTip = false

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

import VueClipboard from 'vue-clipboard2'
//VueClipboard.config.autoSetContainer = true // add this line
Vue.use(VueClipboard)

Vue.mixin({
  computed: {
    apiURL() {
      const url = String(window.location)
      if (Vue.config.devtools || url.includes('dev')) {
        return 'http://192.168.178.22:5000/';//'https://dev-policybear.herokuapp.com/'; //'https://policybear.herokuapp.com/';//'http://192.168.178.25:5000/'//;
      } else {
        return 'https://policybear.herokuapp.com/';
      }
    },
  },
  methods: {
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
    }
  }
})


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
