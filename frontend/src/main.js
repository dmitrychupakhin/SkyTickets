import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import "bootstrap/dist/css/bootstrap.min.css"
import 'bootstrap-icons/font/bootstrap-icons.css';
import "bootstrap"
import './assets/styles/global.css';
import AOS from 'aos'
import 'aos/dist/aos.css'

import components from "@/components/UI"


const app = createApp(App)
const pinia = createPinia();

components.forEach(component => {
    app.component(component.name, component)
})
AOS.init()
app.use(router).use(pinia).mount('#app');
