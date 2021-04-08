import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
// eslint-disable-next-line camelcase
import handwriting_video from '../views/HandwritingVideo'
// eslint-disable-next-line camelcase
import culture_video from '../views/CultureVideo'
import mall from '../views/Mall'
// eslint-disable-next-line camelcase
import handwriting_video_detail from '../views/HandwritingVideoDetail'
// eslint-disable-next-line no-unused-vars
import search from '../views/Search'

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
    },
    {
      path: '/search',
      name: 'search',
      component: search
    }
  ]
})
