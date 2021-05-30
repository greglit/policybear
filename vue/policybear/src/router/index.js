import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Card from '../views/Card.vue'
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
    path: '/card/:request',
    name: 'Card',
    component: Card
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
