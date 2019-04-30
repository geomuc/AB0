import Vue from 'vue'
import App from './App.vue'
import router from './router.js'
import BootstrapVue from 'bootstrap-vue'
import VueResource from 'vue-resource'

Vue.use(BootstrapVue);
Vue.use(VueResource);
Vue.config.productionTip = false;

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

export const eventBus = new Vue ({
  methods: {
    deletePerson (id) {
      console.log('Lösche Person mit Id: ');
      console.log(id);
      this.$emit('personLoeschen', id);
    },
    editPerson (id) {
      console.log('Editiere Person mit Id: ');
      console.log(id);
      this.$emit('personEditieren', id);
    }
  }
});

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
