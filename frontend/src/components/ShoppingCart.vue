<template>
  <div class="cart">
    <q-btn flat icon="shopping_cart" @click="cartExpanded = true"
      >( {{ inCart.length }} )</q-btn
    >
    <q-dialog v-model="cartExpanded">
      <q-card class="cart-cards">
        <q-toolbar>
          <q-toolbar-title>Shopping Cart</q-toolbar-title>
          <q-btn flat round dense icon="close" v-close-popup />
        </q-toolbar>

        <q-card-section>
          <q-list style="min-width: 500px">
            <q-item
              class="list-items"
              v-for="(item, index) in inCart"
              v-bind:key="`${index}-${item.id}`"
            >
              <q-item-section>
                <q-avatar rounded v-if="item.photo === null">
                  <img src="../assets/default-image.jpg" />
                </q-avatar>
                <q-avatar rounded v-else>
                  <img class="img" :src="'data:image/jpg;base64,' + item.photo"
                /></q-avatar>
              </q-item-section>

              <q-item-section>
                <q-item-label lines="1">{{ item.title }}</q-item-label>
              </q-item-section>

              <q-item-section>{{ item.price | formatPrice }}</q-item-section>

              <q-item-section>
                <q-btn
                  flat
                  icon="delete"
                  @click="removeFromCart(index)"
                ></q-btn>
              </q-item-section>
            </q-item>
          </q-list>
        </q-card-section>

        <div v-if="inCart.length > 0">
          <q-card-section align="right">
            <div class="text-subtitle">
              Total: {{ totalPrice | formatPrice }}
            </div>
          </q-card-section>

          <q-card-actions align="right">
            <!-- add @click for redirect notification -->
            <q-btn flat style="background:#f3e5cf; color:black;" to="/checkout"
              >Checkout</q-btn
            >
          </q-card-actions>
        </div>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "ShoppingCart",
  data() {
    return {
      cartExpanded: false,
      inCart: this.$store.state.inCart,
      isLoggedIn: this.$store.state.isLoggedIn
    };
  },
  filters: {
    formatPrice: function(value) {
      return "$" + (value / 100).toString();
    }
  },
  computed: {
    totalPrice() {
      return this.inCart.reduce(
        (acc, cur) => parseFloat(acc) + parseFloat(cur.price),
        0
      );
    }
  },
  methods: {
    removeFromCart(index) {
      this.$store.dispatch("removeFromCart", index);
    }
  }
};
</script>

<style scoped>
.cart-cards {
  padding: 10px;
}
.list-items {
  padding: 10px;
}
.img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
