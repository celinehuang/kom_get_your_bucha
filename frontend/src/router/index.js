import Vue from "vue";
import VueRouter from "vue-router";
import routes from "./routes";
import axios from "axios";
import Store from "../store";

Vue.use(VueRouter);

var config = require("../config");

// Axios config
const backendUrl = config.build.backendHost + ":" + config.build.backendPort;

var AXIOS = axios.create({
  baseURL: backendUrl,
  headers: {
    "Content-Type": "application/json"
  }
});

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default function(/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ x: 0, y: 0 }),
    routes,

    // Leave these as they are and change in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  });
  Router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
      console.log(Store.state.currentUser);
      // this route requires auth, check if logged in
      // if not, redirect to login page.
      if (!Store.getters.isLoggedIn) {
        next({
          path: "/login",
          query: { redirect: to.fullPath }
        });
      } else if (Store.getters.isLoggedIn && Store.state.currentUser === null) {
        // get user with stored token
        console.log("inside else if");
        const token = Store.state.token;

        const body = {
          token: token
        };

        AXIOS.post("/auth/token", body)
          .then(resp => {
            console.log("hello inside then");
            Store.commit("set_user", resp.data);
            next();
          })
          .catch(e => {
            console.log(e);
            // token is invalid
            Store.dispatch("logout").then(
              next({
                path: "/login",
                query: { redirect: to.fullPath }
              })
            );
            next();
          });
      } else {
        next();
      }
    } else {
      if (Store.getters.isLoggedIn && Store.state.currentUser === null) {
        // get user with stored token
        console.log("inside else if");
        const token = Store.state.token;

        const body = {
          token: token
        };

        AXIOS.post("/auth/token", body)
          .then(resp => {
            console.log("hello inside then");
            Store.commit("set_user", resp.data);
            next();
          })
          .catch(e => {
            console.log(e);
            // token is invalid
            Store.dispatch("logout").then(
              next({
                path: "/login",
                query: { redirect: to.fullPath }
              })
            );
            next();
          });
      } else {
        next();
      }
    }
  });

  return Router;
}
