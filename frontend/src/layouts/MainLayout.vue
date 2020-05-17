<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-black">
      <q-toolbar class="float-right">
        <q-space />
        <form @submit.prevent="onSearch" class="q-pt-sm q-px-md">
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
        <q-btn flat round dense icon="shopping_cart">( {{numItems}} )</q-btn>
      </q-toolbar>
      <q-toolbar>
        <div
          class="center my-font text-weight-medium"
          style="font-size: 40px; white-space: pre-wrap;"
        >
          <div style="text-align:center">KOM GET YOUR&#10;BUCHA</div>
          <!-- <img src="../assets/white-logo.png" /> -->
        </div>
      </q-toolbar>
      <div class="center q-py-sm">
        <q-btn-dropdown flat label="SHOP ONLINE" style="font-size: 18px; width:30%">
          <q-list>
            <q-item>
              <q-btn flat class="q-pt-sm full-width">Classic Flavours</q-btn>
            </q-item>
            <q-item>
              <q-btn flat class="q-pt-sm full-width">Limited Edition Flavours</q-btn>
            </q-item>
            <q-item>
              <q-btn flat class="q-pt-sm full-width">Alcoholic Kombucha</q-btn>
            </q-item>
            <q-item>
              <q-btn flat class="q-pt-sm full-width">Equipment</q-btn>
            </q-item>
            <q-item>
              <q-btn flat class="q-pt-sm full-width">Sale</q-btn>
            </q-item>
          </q-list>
        </q-btn-dropdown>
        <q-btn flat label="RECIPES" style="font-size: 18px; width:30%"></q-btn>
        <q-btn-dropdown stretch flat label="ABOUT" style="font-size: 18px;width:30%"></q-btn-dropdown>
        <!-- <q-btn flat label="BLOG" style="font-size: 18px;"></q-btn> -->
      </div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
// import EssentialLink from "components/EssentialLink";

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
.my-font {
  font-family: "customfont";
}
</style>