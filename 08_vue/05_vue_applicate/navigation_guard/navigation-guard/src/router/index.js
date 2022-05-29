import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import NotFound404 from '../views/NotFound404.vue'
import TodoView from '../views/TodoView.vue'

Vue.use(VueRouter)

const isLoggedIn = false

const routes = [
  {
    path: '/todo',
    name: 'TodoView',
    component: TodoView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter: (to, from, next) => {
      if (isLoggedIn) {
        console.log('이미 로그인함')
        next({ name: 'home'})
      } else {
        console.log('계획대로 이동!')
        next()
      }
    }
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


// 전역 가드
// router.beforeEach((to, from, next) => {
//   // to: 이동할 url 정보가 담긴 라우터 객체
//   // from: 현재 url 정보가 담긴 라우터 객체
//   // next: to에서 지정한 url로 이동하기 위해 꼭 호출해야 하는 함수

//   // 로그인 여부 확인(실제로는 vuex에서 불러옵니다)
//   const isLoggedIn = true

//   // 로그인이 필요한 페이지
//   // [] 안에 들어가는 이름은 위쪽 routes의 name!
//   const authPages = ['about']

//   // 앞으로 이동할 페이지가 로그인이 필요한 사이트인지 확인
//   const isAuthRequired = authPages.includes(to.name)

//   // 로그인이 필요한 페이지인데, 로그인이 안 되어 있다면?
//   if (isAuthRequired && !isLoggedIn) {
//       console.log('로그인 안됨')
//       next({ name: 'login'})
//     } else {
//       console.log('니가 로그인이 되어 있거나, 로그인이 필요한 url로 이동함')
//       next()
//     }
// })




export default router
