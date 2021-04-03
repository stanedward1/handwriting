import Vue from 'vue'
import Router from 'vue-router'
import Home from "../views/Home";
import handwriting_course from "../views/handwriting_course"
import culture_course from "../views/culture_course";
import mall from "../views/mall";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/handwriting_course',
      name: 'handwriting_course',
      component: handwriting_course
    },
    {
      path: '/culture_course',
      name: 'culture_course',
      component: culture_course
    },
    {
      path: '/mall',
      name: 'mall',
      component: mall
    },
  ]
})
