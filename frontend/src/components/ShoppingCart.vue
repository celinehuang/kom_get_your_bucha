<template>
  <div class="cart">
    <q-btn flat icon="shopping_cart" @click="cartExpanded = true"
      >( {{ numItems }} )</q-btn
    >
    <q-dialog v-model="cartExpanded">
      <q-card class="cart-cards">
        <q-toolbar>
          <q-toolbar-title>Shopping Cart</q-toolbar-title>
          <q-btn flat round dense icon="close" @click="log" v-close-popup />
        </q-toolbar>

        <q-card-section>
          <q-list style="min-width: 500px">
            <q-item
              class="list-items"
              v-for="item in inCart.keys()"
              v-bind:key="item.id"
            >
              <q-item-section>
                <q-avatar rounded>
                  <img v-bind:src="item.photo" />
                </q-avatar>
              </q-item-section>
              <q-item-section>
                <q-item-label v-if="inCart.get(item) > 0">{{
                  inCart.get(item)
                }}</q-item-label>
              </q-item-section>

              <q-item-section>
                <q-item-label lines="1">{{ item.title }}</q-item-label>
              </q-item-section>

              <q-item-section>{{ item.price | formatPrice }}</q-item-section>

              <q-item-section>
                <q-btn flat icon="delete" @click="removeFromCart(item)"></q-btn>
              </q-item-section>
            </q-item>
          </q-list>
        </q-card-section>

        <div v-if="inCart.size > 0">
          <q-card-section align="right">
            <div class="text-subtitle">
              <!-- Total: {{ totalPrice | formatPrice }} -->
            </div>
          </q-card-section>

          <q-card-actions align="right">
            <!-- add @click for redirect notification -->
            <q-btn
              flat
              style="background=#f3e5cf;"
              @click="showLoginNotif"
              to="/checkout"
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
      inCart: this.$store.state.inCart
      //   tolNumItems: 0
    };
  },
  filters: {
    formatPrice: function(value) {
      return "$" + (value / 100).toString();
    }
  },
  computed: {
    totalPrice() {
      console.log("is this even called total price");
      var tolPrice = 0;
      return this.inCart.forEach(item => {
        tolPrice += this.item.price;
        console.log("total price" + tolPrice);
      });
    },
    numItems() {
      console.log("numItems is called");
      var tolNumItems = 0;
      this.inCart.forEach(function(value, key) {
        tolNumItems += value;
      });

      return tolNumItems;
    }
  },
  methods: {
    removeFromCart(item) {
      this.$store.dispatch("removeFromCart", item);
    },
    log() {
      console.log(this.numItems);
    },
    showLoginNotif() {
      this.$q.notify({
        color: "red-3",
        position: "top",
        textColor: "white",
        icon: "error",
        message: "Please log in before preceeding to checkout"
      });
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
</style>
