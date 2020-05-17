<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-black">
      <q-toolbar class="q-pr-xl">
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
        <q-btn flat dense icon="shopping_cart" class="q-px-sm" to="/cart">( {{numItems}} )</q-btn>
        <q-btn flat dense class="q-pa-sm" to="/login">LOG IN</q-btn>
      </q-toolbar>
      <q-toolbar>
        <div class="center title-font text-weight-medium">
          <q-btn
            style="font-size: 40px; white-space: pre-wrap;"
            :ripple="false"
            to="/home"
          >KOM GET YOUR&#10;BUCHA</q-btn>
        </div>
      </q-toolbar>
      <div class="center q-py-sm">
        <q-btn-dropdown :ripple="false" flat label="SHOP ONLINE" style="font-size: 18px; width:30%">
          <q-list>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/classic-kombucha"
              >Classic Flavours</q-btn>
            </q-item>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/limited-edition"
              >Limited Edition Flavours</q-btn>
            </q-item>
            <q-item>
              <q-btn
                :ripple="false"
                flat
                class="q-pt-sm full-width"
                to="/alcoholic"
              >Alcoholic Kombucha</q-btn>
            </q-item>
            <q-item>
              <q-btn :ripple="false" flat class="q-pt-sm full-width" to="/equipment">Equipment</q-btn>
            </q-item>
            <q-item>
              <q-btn :ripple="false" flat class="q-pt-sm full-width" to="/all-products">All Products</q-btn>
            </q-item>
          </q-list>
        </q-btn-dropdown>
        <q-btn :ripple="false" flat label="RECIPES" style="font-size:18px; width:30%" to="/recipes"></q-btn>
        <q-btn-dropdown
          :ripple="false"
          stretch
          flat
          label="ABOUT"
          style="font-size:18px; width:30%"
        >
          <q-list>
            <q-item>
              <q-btn :ripple="false" flat class="q-pt-sm full-width" to="/story">Story</q-btn>
            </q-item>
            <q-item>
              <q-btn :ripple="false" flat class="q-pt-sm full-width" to="/contact">Contact</q-btn>
            </q-item>
          </q-list>
        </q-btn-dropdown>
        <!-- <q-btn flat label="BLOG" style="font-size: 18px;"></q-btn> -->
      </div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "MainLayout",

  components: {},

  data() {
    return {
      searchText: null,
      numItems: 0
    };
  },
  methods: {
    onSearch() {}
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
</style>