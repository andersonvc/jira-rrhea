import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Element from 'element-ui'


Vue.use(Element)
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

Vue.component('OpenAIInterface', require('vue-spinner/src/PulseLoader.vue'));




new Vue({
  render: h => h(App),
}).$mount('#app')
