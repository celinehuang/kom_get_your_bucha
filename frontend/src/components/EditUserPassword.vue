<template>
  <div class="q-pa-md">
    <!-- Change account details section -->
    <div class="text-h6 q-mb-md">Change Password</div>

    <q-form @submit="changePassword" class="q-gutter-md q-ma-md">
      <q-input
        label="Old Password"
        v-model="oldPassword"
        filled
        lazy-rules
        :type="isPwd ? 'password' : 'text'"
      >
        <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
      </q-input>
      <q-input
        label="New Password"
        v-model="newPassword"
        filled
        lazy-rules
        :type="isPwd1 ? 'password' : 'text'"
      >
        <template v-slot:append>
          <q-icon
            :name="isPwd1 ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd1 = !isPwd1"
          />
        </template>
      </q-input>
      <q-input
        label="Confirm New Password"
        v-model="confirmNewPassword"
        filled
        lazy-rules
        :type="isPwd2 ? 'password' : 'text'"
        :rules="[val => val === newPassword || 'Passwords do not match']"
      >
        <template v-slot:append>
          <q-icon
            :name="isPwd2 ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd2 = !isPwd2"
          />
        </template>
      </q-input>

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
  name: "EditUserPassword",
  data: function() {
    return {
      submitting: false,
      isPwd: true,
      isPwd1: true,
      isPwd2: true,
      newPassword: "",
      oldPassword: "",
      confirmNewPassword: "",
      id: this.$store.state.currentUser.user_id
    };
  },
  methods: {
    changePassword: function() {
      this.submitting = true;
      const id = this.id;
      const token = this.$store.state.token;
      const body = {
        old_password: this.oldPassword,
        new_password: this.newPassword
      };
      this.$axios
        .post(`/auth/${this.id}/password`, body, {
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
            message: "Password Updated Successfully"
          });
          this.submitting = false;
          this.oldPassword = "";
          this.newPassword = "";
          this.confirmNewPassword = "";
        })
        .catch(_err => {
          console.log(_err);
          this.$q.notify({
            color: "red-4",
            position: "top",
            textColor: "white",
            icon: "error",
            message: "Incorrect Old Password"
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
