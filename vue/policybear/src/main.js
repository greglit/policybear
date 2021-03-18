import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.mixin({
  computed: {
    apiURL() {
      var url = String(window.location)
      if (Vue.config.devtools || url.includes('dev')) {
        return 'https://dev-policybear.herokuapp.com/'; //'https://policybear.herokuapp.com/';//'http://192.168.178.25:5000/';
      } else {
        return 'https://policybear.herokuapp.com/';
      }
    },
  },
  methods: {
    capitFirstChar(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
  }
})


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
