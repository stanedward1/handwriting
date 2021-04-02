import Vue from 'vue'
import App from './App'
import router from './router'

// eslint-disable-next-line no-unused-vars
import store from './store'
import axios from 'axios'
import cookies from 'vue-cookies'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.config.productionTip = false

Vue.prototype.$axios = axios
Vue.prototype.$cookies = cookies

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
