<template>
  <q-layout>
    <div class="container">
      <div class="q-pa-md row justify-center items-start q-gutter-md">
        <Item
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
      items: null
    };
  },
  components: {
    Item
  },
  methods: {
    getItems() {
      this.$axios
        .get("http://localhost:5000/items/classic")
        .then(response => {
          const data = response.data;
          this.items = [];
          Object.keys(data).forEach(key => {
            console.log(data[key].item_type);
            if (data[key].inventory_count > 0) {
              this.items[key] = data[key];
            }
            this.items[key];
          });
        })
        .catch(e => {
          console.log(e);
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