import { createApp } from 'vue'
import App from './App.vue'
import mitt from 'mitt';
import { createPinia } from 'pinia';

const emitter = mitt()

export const bus = emitter;
const pinia = createPinia()

const app = createApp(App)
app.use(pinia)

app.mount('#app')