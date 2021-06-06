import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Share from '../views/Share.vue'
import Editor from '../views/Editor.vue'
import PrivacyPolicy from '../views/PrivacyPolicy.vue'
import Contact from '../views/Contact.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/editor/',
    name: 'Editor',
    component: Editor
  },
  {
    path: '/share/:request',
    name: 'ShareRequest',
    component: Share
  },
  {
    path: '/share/',
    name: 'Share',
    component: Share
  },
  {
    path: '/privacy',
    name: 'Privacy Policy',
    component: PrivacyPolicy
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
