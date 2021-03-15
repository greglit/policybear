import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false


import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.mixin({
  computed: {
    apiURL() {
      if (Vue.config.devtools) {
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
