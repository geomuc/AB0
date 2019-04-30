import Vue from 'vue'
import Router from 'vue-router'
import LoginComponent from "./components/security/login.vue"
import Bearbeiten from './components/bearbeiten/Bearbeiten.vue'
import Home from './components/Home.vue'
import Auskunft from './components/auskunft/Auskunft.vue'

Vue.use(Router)

export default new Router({
    routes: [
        /*{
            path: '/',
            redirect: {
                name: "login"
            }
        },*/
        {
            path: "/login",
            name: "login",
            component: LoginComponent
        },
        {
            path: '', 
            name: 'home',
            component: Home
        },
        {
            path: '/bearbeiten', 
            component: Bearbeiten
        },
        {
            path: '/auskunft', 
            component: Auskunft
        }
    ]
})



