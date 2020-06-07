<template>
  <q-layout>
    <q-card class="q-ma-xl">
      <div class="row q-pa-md">
        <div class="col-3" v-if="$q.screen.width >= 600">
          <q-list padding class="rounded-borders">
            <q-item
              clickable
              v-ripple
              :active="selected === 'Account'"
              @click="selected = 'Account'"
              active-class="menu-item"
            >
              <q-item-section avatar>
                <q-icon name="person" />
              </q-item-section>

              <q-item-section>Account Details</q-item-section>
            </q-item>

            <q-item
              clickable
              v-ripple
              :active="selected === 'Password'"
              @click="selected = 'Password'"
              active-class="menu-item"
            >
              <q-item-section avatar>
                <q-icon name="lock" />
              </q-item-section>

              <q-item-section>Password</q-item-section>
            </q-item>
          </q-list>
        </div>
        <!-- Show dropdown on mobile -->
        <div v-else class="col-12 q-pa-sm">
          <q-select
            filled
            class="q-mb-md"
            v-model="selected"
            :options="options"
          />
        </div>

        <q-separator vertical v-if="$q.screen.width >= 600" />

        <div class="col" v-if="$q.screen.width >= 600">
          <EditUserDetails v-if="selected === 'Account'" />
          <EditUserPassword v-if="selected === 'Password'" />
        </div>
        <div class="col-12" v-else>
          <EditUserDetails v-if="selected === 'Account'" />
          <EditUserPassword v-if="selected === 'Password'" />
        </div>
      </div>
    </q-card>
  </q-layout>
</template>

<script>
import EditUserDetails from "../components/EditUserDetails.vue";
import EditUserPassword from "../components/EditUserPassword.vue";
export default {
  name: "EditProfile",
  components: {
    EditUserDetails,
    EditUserPassword
  },
  data() {
    return {
      selected: "Account",
      options: ["Account", "Password"]
    };
  }
};
</script>

<style scoped>
.button {
  background-color: #f3e5cf;
  color: black;
}
</style>
