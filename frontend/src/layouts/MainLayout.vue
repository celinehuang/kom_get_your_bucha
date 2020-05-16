<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-black">
      <q-toolbar class="float-right">
        <q-space />
        <q-btn flat round dense icon="search" class="q-mr-xs" />
        <q-btn flat round dense icon="shopping_cart" />
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
      <!-- <q-toolbar inset>
        <q-breadcrumbs class="center" active-color="white" style="font-size: 20px">
          <q-breadcrumbs-el flat round dense label="SHOP ONLINE" icon="expand_more" />
          <q-breadcrumbs flat round dense label="SHOP ONLINE" icon="expand_more" />
          <q-tab label="RECIPES" />/
          <q-tab label="ABOUT" />
        </q-breadcrumbs>
      </q-toolbar>-->
      <div class="center q-py-sm">
        <q-btn-dropdown stretch flat label="SHOP ONLINE" style="font-size: 18px">
          <q-list>
            <!-- <q-item-label header>Folders</q-item-label>
          <q-item v-for="n in 3" :key="`x.${n}`" clickable v-close-popup tabindex="0">
            <q-item-section avatar>
              <q-avatar icon="folder" color="secondary" text-color="white" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Photos</q-item-label>
              <q-item-label caption>February 22, 2016</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-icon name="info" />
            </q-item-section>
          </q-item>
          <q-separator inset spaced />
          <q-item-label header>Files</q-item-label>
          <q-item v-for="n in 3" :key="`y.${n}`" clickable v-close-popup tabindex="0">
            <q-item-section avatar>
              <q-avatar icon="assignment" color="primary" text-color="white" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Vacation</q-item-label>
              <q-item-label caption>February 22, 2016</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-icon name="info" />
            </q-item-section>
            </q-item>-->
          </q-list>
        </q-btn-dropdown>
        <q-btn flat label="RECIPES" style="font-size: 18px"></q-btn>
        <q-btn-dropdown stretch flat label="ABOUT" style="font-size: 18px"></q-btn-dropdown>
        <q-btn flat label="BLOG" style="font-size: 18px"></q-btn>
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
    return {};
  }
};
</script>

<style scoped>
.center {
  margin: auto;
  width: 50%;
  /* border: 3px solid green; */
  /* padding: 10px; */
  text-align: center;
}
.my-font {
  font-family: "customfont";
}
</style>