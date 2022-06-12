import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
// eslint-disable-next-line camelcase
import handwriting_video from '../views/HandwritingVideo'
// eslint-disable-next-line camelcase
import culture_video from '../views/CultureVideo'
import culture_video_detail from "../views/CultureVideoDetail";
// eslint-disable-next-line no-unused-vars
import Goods from '../views/Goods'
import GoodsDetail from '../views/GoodsDetail'
// eslint-disable-next-line camelcase
import handwriting_video_detail from '../views/HandwritingVideoDetail'
// eslint-disable-next-line no-unused-vars
import search from '../views/Search'
import PaySuccess from '../views/PaySuccess'
// eslint-disable-next-line no-unused-vars
import Cart from '../views/Cart'
import Pcenter from "../views/Pcenter";

Vue.use(Router)

export default new Router({
  mode: 'history',
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
      path: '/culturevideo/detail/:id',
      name: 'culture_video_detail',
      component: culture_video_detail
    },
    {
      path: '/mall',
      name: 'goods',
      component: Goods
    },
    {
      path: '/mall/detail/:id',
      name: 'GoodsDetail',
      component: GoodsDetail
    },
    {
      path: '/search',
      name: 'search',
      component: search
    },
    {
      path: '/pay/success',
      name: 'PaySuccess',
      component: PaySuccess
    },
    {
      path: '/cart',
      name: 'Cart',
      component: Cart
    },
        {
      path: '/center',
      name: 'Center',
      component: Pcenter
    },
  ]
})
