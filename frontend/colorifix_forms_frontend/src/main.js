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
new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount("#app");
