<template>
  <div class="col-md-3 col-sm-6 col-xs-12">
    <q-card class="my-card">
      <div v-if="photo === null">
        <q-img :ratio="1">
          <img src="../assets/default-image.jpg" />
          <div class="price-caption">{{ price | formatPrice }}</div>
        </q-img>
      </div>
      <div v-else>
        <q-img :ratio="1">
          <img class="img" :src="'data:image/jpg;base64,' + photo" />
          <div class="price-caption">{{ price | formatPrice }}</div>
        </q-img>
      </div>

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
          <q-card-section class="text-subitle2">{{
            description
          }}</q-card-section>
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
  props: {
    item: Object,
    id: Number,
    description: String,
    price: Number,
    photo: String,
    title: String
  },
  methods: {
    addToCart(item) {
      var counts = {};
      this.inCart.forEach(function(x) {
        counts[x] = (counts[x] || 0) + 1;
      });
      if (counts[item] > item.inventory_count) {
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
.img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
