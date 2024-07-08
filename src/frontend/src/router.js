import {createRouter, createWebHistory} from 'vue-router'
import Landing from './pages/Landing.vue'
import Login from './pages/Login.vue'
import Register from "./pages/Register.vue";
import Home from './pages/Home.vue'
import Preview from './pages/Preview.vue'
import OrganizerPanel from './pages/OrganizerPanel.vue'
import CreateEvent from './pages/CreateEvent.vue'
import UpdateEvent from './pages/UpdateEvent.vue'
import Tickets from './pages/Tickets.vue'

const routes = [
    {
        path: '/',
        name: 'landing',
        component: Landing
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    {
        path: '/home',
        name: 'home',
        component: Home
    },
    {
        path: '/preview',
        name: 'preview',
        component: Preview
    },
    {
        path: '/organizer-panel',
        name: 'organizer-panel',
        component: OrganizerPanel
    },
    {
        path: '/create-event',
        name: 'create-event',
        component: CreateEvent
    },
    {
        path: '/update-event',
        name: 'update-event',
        component: UpdateEvent
    },
    {
        path: '/tickets',
        name: 'tickets',
        component: Tickets
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
