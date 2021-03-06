import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";

Vue.use(Vuex);

var config = require("../config");

// Axios config
const frontendUrl = config.build.host + ":" + config.build.port;
const backendUrl = config.build.backendHost + ":" + config.build.backendPort;

var AXIOS = axios.create({
  baseURL: backendUrl,
  headers: {
    "Access-Control-Allow-Origin": frontendUrl,
    "Content-Type": "application/json"
  }
});

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation
 */

const Store = new Vuex.Store({
  // plugins: [createPersistedState()],
  state: {
    status: "",
    token: localStorage.getItem("token") || "",
    currentUser: null,
    inCart: []
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    inCart: state => state.inCart
  },
  mutations: {
    auth_request(state) {
      state.status = "loading";
    },
    auth_success(state, authObj) {
      state.status = "success";
      state.token = authObj.token;
      state.currentUser = authObj.user;
    },
    auth_error(state) {
      state.status = "error";
    },
    logout(state) {
      state.status = "";
      state.token = "";
      state.currentUser = null;
    },
    set_user(state, user) {
      state.currentUser = user;
    },
    add_to_cart(state, item) {
      state.inCart.push(item);
    },
    remove_from_cart(state, index) {
      state.inCart.splice(index, 1);
    },
    empty_cart(state) {
      state.inCart = [];
    }
  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        AXIOS.post("/auth/login", {
          email: user.email,
          password: user.password
        })
          .then(resp => {
            const token = resp.data.token;
            const user = resp.data.user;
            localStorage.setItem("token", token);
            axios.defaults.headers.common["Authorization"] = token;
            commit("auth_success", { token, user });
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    adminLogin({ commit }, admin) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        AXIOS.post("/auth/admin-login", {
          email: admin.email,
          password: admin.password
        })
          .then(resp => {
            const token = resp.data.token;
            const admin = resp.data.admin;
            localStorage.setItem("token", token);
            axios.defaults.headers.common["Authorization"] = token;
            commit("auth_success", { token, admin });
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    register({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        AXIOS.post("/auth/register", {
          name: user.name,
          email: user.email,
          password: user.password
        })
          .then(resp => {
            const token = resp.data.token;
            const user = resp.data.user;
            localStorage.setItem("token", token);
            axios.defaults.headers.common["Authorization"] = token;
            commit("auth_success", { token, user });
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error", err);
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    logout({ commit }) {
      return new Promise((resolve, reject) => {
        commit("logout");
        localStorage.removeItem("token");
        delete axios.defaults.headers.common["Authorization"];
        resolve();
      });
    },
    addToCart({ commit }, item) {
      commit("add_to_cart", item);
    },
    removeFromCart({ commit }, index) {
      commit("remove_from_cart", index);
    },
    emptyCart({ commit }) {
      commit("empty_cart");
    }
  },
  // enable strict mode (adds overhead!)
  // for dev mode only
  modules: {
    // example
  },
  strict: process.env.DEV
});

export default Store;
