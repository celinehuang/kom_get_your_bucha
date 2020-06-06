<template>
  <div class="col-md-3 col-sm-6 col-xs-12">
    <q-card class="my-card">
      <q-img v-bind:src="photo" :ratio="1">
        <div class="price-caption">{{ price | formatPrice }}</div>
      </q-img>

      <q-card-section class="title-artist">
        <div class="text-h6">{{ title }}</div>
      </q-card-section>

      <q-card-actions>
        <q-btn
          round
          flat
          dense
          :icon="expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
          @click="expanded = !expanded"
        />
        <q-space />
        <q-btn flat icon="add_shopping_cart" @click="addToCart(item)" />
      </q-card-actions>

      <q-slide-transition>
        <div v-show="expanded">
          <q-separator />
          <q-card-section class="text-subitle2">{{ description }}</q-card-section>
        </div>
      </q-slide-transition>
    </q-card>
  </div>
</template>
<script>
export default {
  name: "Item",
  data() {
    return {
      expanded: false,
      inCart: this.$store.state.inCart
    };
  },
  props: ["item", "id", "description", "price", "photo", "title"],
  methods: {
    addToCart(item) {
      if (this.inCart.get(item) > item.inventory_count) {
        this.$q.notify({
          color: "red-4",
          position: "top",
          textColor: "white",
          icon: "error",
          message: "Item cannot be add to cart, there is not enough in stock"
        });
      } else {
        this.$store.commit("add_to_cart", item);
      }
      console.log(item);
    }
  },
  filters: {
    formatPrice: function(value) {
      return "$" + (value / 100).toString();
    }
  }
};
</script>
<style scoped>
.my-card {
  width: 100%;
  max-width: 350px;
}
.price-caption {
  position: absolute;
  bottom: 10px;
  left: 10px;
  background-color: black;
  border-radius: 5px;
  height: auto;
  width: auto;
  padding: 5px;
}
</style>
