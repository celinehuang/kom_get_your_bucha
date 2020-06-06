<template>
  <div class="q-pa-md">
    <!-- Change password section -->
    <div class="text-h6 q-mb-md">Edit Account Details</div>

    <q-form @submit="changeProfile" class="q-gutter-md q-ma-md">
      <q-input filled v-model="email" hint="Cannot change email" disable />
      <q-input filled v-model="name" label="Name" />
      <q-input filled v-model="shipping_addr" label="Address" />
      <div class="float-right">
        <q-btn class="button q-ma-lg" to="/home" flat label="Cancel" />
        <q-btn class="button" flat type="submit" label="Done" />
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

      username: this.$store.state.currentUser.username,
      name: this.$store.state.currentUser.name,
      shipping_addr: this.$store.state.currentUser.shipping_addr,
      email: this.$store.state.currentUser.email,
      id: this.$store.state.currentUser.id
    };
  },
  methods: {
    changeProfile: function() {
      this.submitting = true;
      //   const body = {
      //     old_password: this.oldPassword,
      //     new_password: this.newPassword
      //   };
      //   this.$axios
      //     .post("/auth/change-password", body, {
      //       headers: { "X-CSRF-TOKEN": this.$q.cookies.get("csrf_access_token") },
      //     })
      //     .then(() => {
      //       this.$q.notify({
      //         color: "green-4",
      //         position: "top",
      //         textColor: "white",
      //         icon: "cloud_done",
      //         message: "Password Updated Successfully",
      //       });
      //       this.submitting = false;
      //       this.oldPassword = "";
      //       this.newPassword = "";
      //       this.confirmNewPassword = "";
      //     })
      //     .catch((_err) => {
      //       console.log(_err);
      //       this.$q.notify({
      //         color: "red-4",
      //         position: "top",
      //         textColor: "white",
      //         icon: "error",
      //         message: "Incorrect Old Password",
      //       });
      //       this.submitting = false;
      //     });
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
