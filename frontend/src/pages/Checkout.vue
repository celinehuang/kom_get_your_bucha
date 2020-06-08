<template>
  <q-layout>
    <q-toolbar class="q-pa-md">
      <q-btn icon="keyboard_arrow_left" flat label="Back to Home" to="/home" />
    </q-toolbar>
    <div class="row items-start q-pa-lg">
      <div class="col-7 q-px-xl q-py-lg">
        <q-card class=" q-pa-lg">
          <q-card-section>
            <div class="text-h6">Review Order & Checkout</div>
          </q-card-section>
          <q-card-section>
            <q-form @submit="checkout" class="q-ma-md">
              <q-input
                filled
                v-model="name"
                label="Name"
                lazy-rules
                :rules="[val => !!val || 'Field is required']"
              />
              <q-input
                filled
                v-model="email"
                label="Email"
                lazy-rules
                :rules="[val => !!val || 'Field is required']"
              />
              <q-input
                filled
                v-model="shipping_addr"
                label="Delivery Address"
                lazy-rules
                :rules="[val => !!val || 'Field is required']"
              />
              <q-separator class="q-my-md" />
              <q-input
                filled
                v-model="cardNum"
                label="Card Number"
                mask="#### #### #### ####"
                lazy-rules
                :rules="[val => !!val || 'Field is required']"
              />
              <q-input
                filled
                v-model="cardName"
                label="Name On Card"
                lazy-rules
                :rules="[val => !!val || 'Field is required']"
              />
              <div>
                <q-input
                  style="width:50%; float:left; padding-right:10px"
                  filled
                  v-model="expDate"
                  label="MM/YY"
                  mask="##/##"
                  lazy-rules
                  :rules="[val => !!val || 'Field is required']"
                />
                <q-input
                  style="width:50%; padding-left:10px"
                  filled
                  v-model="cvc"
                  label="CVC"
                  lazy-rules
                  :rules="[val => !!val || 'Field is required']"
                />
              </div>
              <q-input
                filled
                v-model="billing_addr"
                label="Billing Address"
                lazy-rules
                :rules="[val => !!val || 'Field is required']"
              />
              <div>
                <q-btn
                  class="text-black float-right"
                  flat
                  style="background:#f3e5cf;"
                  type="submit"
                  label="Checkout"
                />
              </div>
            </q-form>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-5 q-pa-lg">
        <q-card class="q-pa-lg">
          <q-card-section>
            <q-list>
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
                    <img
                      class="img"
                      :src="'data:image/jpg;base64,' + item.photo"
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
                    @click="removeFromCart(item)"
                  ></q-btn>
                </q-item-section>
              </q-item>
            </q-list>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-layout>
</template>

<script>
export default {
  name: "Checkout",
  data() {
    return {
      inCart: this.$store.state.inCart,
      name: this.$store.state.currentUser.name,
      email: this.$store.state.currentUser.email,
      cardName: null,
      billing_addr: null,
      shipping_addr: this.$store.state.currentUser.shipping_addr,
      cardNum: this.cardNum,
      expDate: this.expDate,
      cvc: this.cvc,
      userId: this.$store.state.currentUser.id
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
    removeFromCart(item) {
      this.$store.dispatch("removeFromCart", item);
    },
    emptyCart() {
      this.$store.dispatch("emptyCart");
    },
    getUniqueIds(inCart) {
      var uniqueIds = {};
      Object.keys(inCart).forEach(key => {
        var id = inCart[key].id;
        var inventory_count = inCart[key].inventory_count;
        if (!(id in uniqueIds)) {
          uniqueIds[id] = {};
          uniqueIds[id].numInCart = 1;
          uniqueIds[id].inventory_count = inventory_count;
        } else if (id in uniqueIds) {
          uniqueIds[id].numInCart += 1;
        }
      });
      return uniqueIds;
    },
    checkout() {
      var inCart = this.inCart;
      var uniqueIds = this.getUniqueIds(inCart);
      Object.keys(uniqueIds).forEach(id => {
        const body = {
          inventory_count:
            uniqueIds[id].inventory_count - uniqueIds[id].numInCart
        };
        itemData.append(
          "inventory_count",
          uniqueIds[id].inventory_count - uniqueIds[id].numInCart
        );
        this.$axios
          .put(`/items/${this.id}/update`, itemData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .catch(err => {
            this.$q.notify({
              color: "red-4",
              position: "top",
              textColor: "white",
              icon: "error",
              message: "Something went wrong, please try again"
            });
          });
      });
      for (var i = 0; i < inCart.length; i++) {
        var purchaseData = new FormData();
        purchaseData.append("username", this.userId);
        purchaseData.append("iId", inCart[i].id);
        purchaseData.append("shipping_addr", this.shipping_addr);
        purchaseData.append("total_amt", inCart[i].price);
        this.$axios
          .post("/api/payments/", purchaseData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .catch(err => {
            this.$q.notify({
              color: "red-4",
              position: "top",
              textColor: "white",
              icon: "error",
              message: "Something went wrong, please try again"
            });
          });
      }
      this.emptyCart();
      this.$router.push({ path: "/home" });
    }
  }
};
</script>

<style scoped>
.img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
