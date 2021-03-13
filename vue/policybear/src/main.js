import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

import { 
  LayoutPlugin,
  CardPlugin,
} from 'bootstrap-vue'

Vue.use(LayoutPlugin)
Vue.use(CardPlugin)

import { BIcon } from 'bootstrap-vue'
Vue.component('b-icon', BIcon)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
