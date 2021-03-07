import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import vuetify from "./plugins/vuetify";
import routes from "./plugins/router";

Vue.use(VueRouter);

Vue.config.productionTip = false;
const router = new VueRouter({
  mode: "history",
  routes
});

export const EventBus = new Vue();
const api_protocol = 'http'
const api_url = 'localhost'
const api_port = '8000'
export const url = `${api_protocol}://${api_url}:${api_port}/`
new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount("#app");
