<template>
  <div class="col-md-3 col-sm-6 col-xs-12">
    <q-card class="my-card">
      <div v-if="item.photo === null">
        <q-img :ratio="1">
          <img src="../assets/default-image.jpg" />
          <div class="price-caption">{{ item.price | formatPrice }}</div>
        </q-img>
      </div>
      <div v-else>
        <q-img :ratio="1">
          <img class="img" :src="'data:image/jpg;base64,' + item.photo" />
          <div class="price-caption">{{ item.price | formatPrice }}</div>
        </q-img>
      </div>

      <q-card-section class="title-artist">
        <div class="text-h6">{{ item.title }}</div>
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
        <q-btn
          flat
          color="primary"
          label="Edit"
          @click="showEditItemPopup = true"
          class="float-right"
        />
        <q-btn flat color="red" label="Delete" @click="deleteItem" class="float-right" />
      </q-card-actions>

      <q-dialog v-model="showEditItemPopup">
        <EditItemPopup @item-updated="notifyParent" :item="item" />
      </q-dialog>
      <q-slide-transition>
        <div v-show="expanded">
          <q-separator />
          <q-card-section class="text-subitle2">
            {{
            item.description
            }}
          </q-card-section>
        </div>
      </q-slide-transition>
    </q-card>
  </div>
</template>

<script>
import EditItemPopup from "../components/EditItemPopup.vue";

export default {
  name: "EditItem",
  data() {
    return {
      showEditItemPopup: false,
      expanded: false
    };
  },
  components: {
    EditItemPopup
  },
  props: {
    item: Object
  },
  methods: {
    notifyParent() {
      this.showEditItemPopup = false;
      this.$emit("item-updated");
    },
    deleteItem() {
      this.$axios
        .delete(`/items/${this.id}`)
        .then(resp => {
          this.$q.notify({
            color: "green-4",
            position: "top",
            textColor: "white",
            icon: "cloud_done",
            message: "Successfully Deleted"
          });
          this.$emit("item-updated");
        })
        .catch(err => {
          this.$q.notify({
            color: "red-4",
            position: "top",
            textColor: "white",
            icon: "error",
            message: "Something went wrong, please try again."
          });
        });
    }
  },
  filters: {
    formatPrice: function(value) {
      return (
        "$" +
        parseFloat(value / 100)
          .toFixed(2)
          .toString()
      );
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
