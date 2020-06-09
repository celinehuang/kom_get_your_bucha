<template>
  <q-card style=" width: 30%; min-width: 400px;">
    <q-card-section class="row">
      <div class="text-h6">Edit item</div>
      <q-space />
      <q-btn icon="close" flat round dense v-close-popup />
    </q-card-section>
    <q-card-section>
      <q-form class="q-gutter-sm" @submit="updateItem">
        <q-input filled v-model="title" label="Title" />
        <q-input filled v-model="description" label="Description" />
        <q-select
          filled
          v-model="item_type"
          :options="itemTypeOptions"
          label="Item Type"
        />
        <q-input
          filled
          v-model="price"
          mask="#.##"
          fill-mask="0"
          reverse-fill-mask
          label="Price"
        />
        <q-input
          filled
          v-model="inventory_count"
          type="number"
          label="Inventory"
        />
        <q-input
          filled
          stack-label
          v-model="photo"
          type="file"
          @change="onFileChanged"
          label="Photo"
        />
        <q-btn
          class="q-my-md text-black"
          color="secondary"
          type="submit"
          label="Update Item"
        />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "EditItemPopup",
  data: function() {
    return {
      itemTypeOptions: ["Classic", "Limited", "Alcoholic", "Equipment"],
      id: this.item.id,
      description: this.item.description,
      price: this.item.price,
      photo: this.item.photo,
      title: this.item.title,
      item_type: this.item.item_type,
      inventory_count: this.item.inventory_count,
      pic_changed: false
    };
  },
  props: {
    item: Object
  },
  methods: {
    updateItem: function() {
      const token = this.$store.state.token;
      const id = this.id;
      const formData = new FormData();
      if (this.pic_changed == true) {
        formData.append("photo", this.newPic);
      }
      formData.append("title", this.title);
      formData.append("description", this.description);
      formData.append("item_type", this.item_type);
      formData.append("price", this.price * 100);
      console.log(this.price);
      formData.append("inventory_count", this.inventory_count);

      this.$axios
        .put(`/items/${id}/update`, formData, {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "multipart/form-data"
          }
        })
        .then(resp => {
          this.$q.notify({
            color: "green-4",
            position: "top",
            textColor: "white",
            icon: "cloud_done",
            message: "Successfully Updated Item"
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
    },
    onFileChanged: function(event) {
      this.newPic = event.target.files[0];
      this.oldPic = URL.createObjectURL(event.target.files[0]);
      this.pic_changed = true;
    }
  }
};
</script>
