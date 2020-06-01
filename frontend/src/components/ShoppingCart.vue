<template>
  <div class="cart">
    <q-btn flat icon="shopping_cart" @click="cartExpanded = true"
      >( {{ inCart.length }} )</q-btn
    >

    <q-dialog v-model="cartExpanded">
      <q-card class="cart-cards">
        <q-toolbar style="background-color:primary">
          <q-toolbar-title>Shopping Cart</q-toolbar-title>
          <q-btn flat round dense icon="close" v-close-popup />
        </q-toolbar>

        <q-card-section>
          <q-list style="min-width: 350px">
            <q-item
              class="list-items"
              v-for="(item, index) in inCart"
              v-bind:key="item.id"
            >
              <q-item-section>
                <!-- <q-avatar rounded>
                  <img v-bind:src="item.photo" />
                </q-avatar>-->
              </q-item-section>

              <q-item-section>
                <q-item-label lines="1">{{ item.title }}</q-item-label>
                <!-- <q-item-label caption>{{item.artist}}</q-item-label> -->
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
            <q-btn flat color="primary" to="/checkout">Checkout</q-btn>
          </q-card-actions>
        </div>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "shoppingCart",
  data() {
    return {
      cartExpanded: false
    };
  },
  filters: {
    formatPrice: function(value) {
      return "$" + (value / 100).toString();
    }
  },
  computed: {
    inCart() {
      return this.$store.getters.inCart;
    },
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

<style lang="stylus">
.cart-cards {
  padding: 10px;
}

.list-items {
  padding: 10px;
}
</style>
