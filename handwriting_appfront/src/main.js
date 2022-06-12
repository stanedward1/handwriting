import Vue from 'vue'
import App from './App'
import router from './router'

// eslint-disable-next-line no-unused-vars
import store from './store'
import axios from 'axios'
import cookies from 'vue-cookies'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

// 配置全局样式
import '@/assets/css/global.css'
// 配置全局自定义设置
import settings from '@/assets/js/settings'
Vue.prototype.$settings = settings
// 在所有需要与后台交互的组件中：this.$settings.base_url + '再拼接具体后台路由'
// vue-video播放器
require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');
import VideoPlayer from 'vue-video-player'
Vue.use(VideoPlayer);
Vue.use(ElementUI)
Vue.config.productionTip = false

Vue.prototype.$axios = axios
Vue.prototype.$cookies = cookies

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
