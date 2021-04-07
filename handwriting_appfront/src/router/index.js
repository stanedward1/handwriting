import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
// eslint-disable-next-line camelcase
import handwriting_video from '../views/handwriting_video'
// eslint-disable-next-line camelcase
import culture_video from '../views/culture_video'
import mall from '../views/mall'
import handwriting_video_detail from "../views/handwriting_video_detail";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/handwriting_video',
      name: 'handwriting_video',
      component: handwriting_video
    },
    {
      path: '/video/detail/:id',
      name: 'handwriting_video_detail',
      component: handwriting_video_detail
    },
    {
      path: '/culture_video',
      name: 'culture_video',
      component: culture_video
    },
    {
      path: '/mall',
      name: 'mall',
      component: mall
    }
  ]
})
