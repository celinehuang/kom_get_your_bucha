<template>
  <div class="q-pa-md">
    <!-- Change Account section -->
    <div class="text-h6 q-mb-md">Edit Account Details</div>

    <q-form @submit="changeProfile" class="q-gutter-md q-ma-md">
      <q-input filled v-model="email" hint="Cannot change email" disable />
      <q-input filled v-model="name" label="Name" />
      <q-input filled v-model="shipping_addr" label="Address" />
      <div class="float-right">
        <q-spinner
          v-if="submitting"
          color="secondary"
          size="2.5em"
          class="q-mr-md"
        />
        <q-btn
          class="button"
          :disabled="submitting"
          flat
          type="submit"
          label="Done"
        />
      </div>
    </q-form>
  </div>
</template>

<script>
export default {
  name: "EditUserDetails",
  data: function() {
    return {
      submitting: false,
      name: this.$store.state.currentUser.name,
      shipping_addr: this.$store.state.currentUser.shipping_addr,
      email: this.$store.state.currentUser.email,
      id: this.$store.state.currentUser.user_id
    };
  },
  methods: {
    changeProfile: function() {
      this.submitting = true;
      const id = this.id;
      const token = this.$store.state.token;

      const body = {
        shipping_addr: this.shipping_addr,
        name: this.name
      };
      this.$axios
        .put(`/users/${this.id}/profile`, body, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(() => {
          this.$q.notify({
            color: "green-4",
            position: "top",
            textColor: "white",
            icon: "cloud_done",
            message: "Account Updated Successfully"
          });
          this.submitting = false;
        })
        .catch(_err => {
          console.log(_err);
          this.$q.notify({
            color: "red-4",
            position: "top",
            textColor: "white",
            icon: "error",
            message: "Sorry, something went wrong"
          });
          this.submitting = false;
        });
    }
  }
};
</script>

<style scoped>
.button {
  background-color: #f3e5cf;
  color: black;
}
</style>
