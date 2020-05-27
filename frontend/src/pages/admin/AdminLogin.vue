<template>
  <q-layout>
    <q-toolbar class="q-pa-xl">
      <q-btn icon="keyboard_arrow_left" flat label="Back to Home" to="/home" />
    </q-toolbar>
    <q-toolbar>
      <div class="center title-font text-weight-medium q-pa-md">
        <q-toolbar-title
          class="q-pb-lg"
          style="font-size: 30px; white-space: pre-wrap;"
          :ripple="false"
        >KOM GET YOUR&#10;BUCHA</q-toolbar-title>
      </div>
    </q-toolbar>

    <div class="center q-pa-md q-gutter-y-md" style="max-width: 500px">
      <q-card class="q-pa-md">
        <q-card-section>
          <div class="text-h6">Admin Login</div>
        </q-card-section>

        <q-form @submit="onLogIn" class="q-gutter-md">
          <q-input
            filled
            v-model="email"
            label="Email"
            lazy-rules
            :rules="[
                  val => (val && val.length > 0) || 'Please enter your email'
                ]"
          />

          <q-input
            filled
            v-model="password"
            label="Password"
            type="password"
            lazy-rules
            :rules="[
                  val =>
                    (val !== null && val !== '') || 'Please enter your password'
                ]"
          />

          <div>
            <q-btn label="Log In" type="submit" class="text-black" style="background:#f3e5cf;" />
          </div>
        </q-form>
      </q-card>
    </div>
  </q-layout>
</template>

<script>
export default {
  name: "AdminLogin",
  data() {
    return {
      email: null,
      password: null
    };
  },
  methods: {
    onLogIn: function() {
      this.submitting = true;
      let email = this.email;
      let password = this.password;
      this.$store
        .dispatch("adminLogin", { email, password })
        .then(() => {
          this.$q.notify({
            color: "green-4",
            position: "top",
            textColor: "white",
            icon: "cloud_done",
            message: "Logged in successfully"
          });
          this.submitting = false;
          this.$router.push({ path: "/home" });
        })
        .catch(_err => {
          console.log(_err);
          this.$q.notify({
            color: "red-4",
            position: "top",
            textColor: "white",
            icon: "error",
            message: "Wrong email or password"
          });
          this.submitting = false;
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.center {
  margin: auto;
  width: 50%;
  text-align: center;
}
.title-font {
  font-family: "customfont";
}
</style>
