<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-black">
      <q-toolbar>
        <q-space />
        <form @submit.prevent="onSearch" class="q-px-md">
          <q-input dark bottom-slots v-model="searchText" label="Search">
            <template v-slot:append>
              <q-icon
                v-if="searchText !== ''"
                name="close"
                @click="searchText = ''"
                class="cursor-pointer"
              />
              <q-icon name="search" />
            </template>
          </q-input>
        </form>

        <ShoppingCart />

        <div v-if="currentUser === null || currentUser === undefined">
          <q-btn flat dense class="q-pa-sm" to="/login">LOG IN</q-btn>
        </div>
        <div v-else>
          <q-btn-dropdown flat dense class="q-pa-sm" :label="`Hi, ${name}`">
            <q-list>
              <q-item>
                <q-btn
                  label="Log Out"
                  class="full-width"
                  flat
                  @click="logout"
                />
              </q-item>
              <q-item>
                <q-btn
                  label="View Profile"
                  class="full-width"
                  flat
                  to="/profile"
                />
              </q-item>
            </q-list>
          </q-btn-dropdown>
        </div>
      </q-toolbar>
      <q-toolbar>
        <div class="center title-font text-weight-medium">
          <q-btn style="font-size: 40px;" :ripple="false" to="/home"
            >KOM GET YOUR BUCHA</q-btn
          >
        </div>
      </q-toolbar>
      <div class="center q-py-sm">
        <q-btn-dropdown
          :ripple="false"
          flat
          label="SHOP ONLINE"
          style="font-size: 18px; width:30%"
        >
          <q-list>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/classic-kombucha"
                >Classic Flavours</q-btn
              >
            </q-item>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/limited-edition"
                >Limited Edition Flavours</q-btn
              >
            </q-item>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/alcoholic"
                >Alcoholic Kombucha</q-btn
              >
            </q-item>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/equipment"
                >Equipment</q-btn
              >
            </q-item>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/all-products"
                >All Products</q-btn
              >
            </q-item>
          </q-list>
        </q-btn-dropdown>
        <!-- <q-btn
          :ripple="false"
          flat
          label="RECIPES"
          style="font-size:18px; width:30%"
          to="/recipes"
        ></q-btn> -->
        <q-btn
          :ripple="false"
          stretch
          flat
          label="ABOUT"
          to="/story"
          style="font-size:18px; width:30%"
        >
          <!-- <q-list>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                style="font-size:18px; width:30%"
                class="q-pt-sm full-width"
                to="/story"
                >Our Story</q-btn
              >
            </q-item> -->
          <!-- <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/contact"
                >Contact</q-btn
              >
            </q-item> -->
          <!-- </q-list> -->
        </q-btn>
        <!-- <q-btn flat label="BLOG" style="font-size: 18px;"></q-btn> -->
      </div>
    </q-header>

    <q-footer elevated class="bg-black q-pa-lg" style="position:absolute">
      <div class="row">
        <div class="col-4">
          <div class="q-pa-sm center">
            <q-btn
              type="a"
              href="https://www.facebook.com/venusultimatemtl/"
              target="_blank"
              icon="fab fa-facebook-f"
            />
          </div>
        </div>
        <div class="col-3">
          <q-btn class="center" to="/where" label="Where To Buy" />
        </div>
        <div class="col-4 q-px-md">
          We are part of the organization Club Ultimate Féminin Montréal (CUFM)
          <div class="q-py-xs">
            Check them out
            <a
              href="http://ultimatefemininmontreal.com/"
              style="color:#df8977"
              target="_blank"
              >here</a
            >
          </div>
          Follow them on Facebook
          <a
            href="https://www.facebook.com/cuvmontreal"
            style="color:#df8977"
            target="_blank"
            >here</a
          >
        </div>
      </div>
      <div class="row">
        <div class="col-4">
          <div class="center">
            <q-btn
              type="a"
              href="https://instagram.com/venus_ultimate?igshid=1crngymo1chph"
              target="_blank"
              icon="fab fa-instagram"
            />
          </div>
        </div>
      </div>
    </q-footer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import ShoppingCart from "../components/ShoppingCart.vue";

export default {
  name: "MainLayout",
  components: { ShoppingCart },
  data() {
    return {
      searchText: null,
      numItems: 0,
      name: this.$store.state.currentUser
        ? this.$store.state.currentUser.name
        : "",
      currentUser: this.$store.state.currentUser,
      inCart: this.$store.state.inCart
    };
  },
  methods: {
    onSearch() {},
    logout: function() {
      this.$store.dispatch("logout").then(this.$router.push({ path: "login" }));
    }
  }
};
</script>

<style scoped>
.center {
  margin: auto;
  width: 50%;
  text-align: center;
}
.title-font {
  font-family: "customfont";
}
.cart {
  display: inline-block;
}
</style>
