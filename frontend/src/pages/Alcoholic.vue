<template>
  <q-layout>
    <div class="container">
      <div class="q-pa-md row justify-center items-start q-gutter-md">
        <q-spinner
          v-if="loading"
          color="primary"
          size="3em"
          class="text-center"
        />
        <Item
          v-else
          style="margin: 10px"
          v-for="item in items"
          v-bind:key="item.id"
          :title="item.title"
          :description="item.description"
          :price="item.price"
          :photo="item.photo"
          :item="item"
        />
      </div>
    </div>
  </q-layout>
</template>

<script>
import Item from "../components/Item.vue";

export default {
  data() {
    return {
      items: null,
      loading: true
    };
  },
  components: {
    Item
  },
  methods: {
    getItems() {
      this.$axios
        .get("items/alcoholic")
        .then(response => {
          const data = response.data;
          this.items = [];
          Object.keys(data).forEach(key => {
            if (data[key].inventory_count > 0) {
              this.items.push(data[key]);
            }
            this.items[key];
          });
          this.loading = false;
        })
        .catch(e => {
          console.log(e);
          this.loading = false;
          this.$q.notify({
            color: "negative",
            position: "top",
            message: "Loading failed",
            icon: "report_problem"
          });
        });
    }
  },
  created() {
    this.getItems();
  }
};
</script>
<style scoped>
.container {
  padding: 20px;
  justify-content: center;
}
</style>
