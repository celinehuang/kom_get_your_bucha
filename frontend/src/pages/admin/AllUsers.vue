<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <q-header elevated class="bg-black">
        <q-toolbar>
          <q-btn
            flat
            dense
            round
            icon="menu"
            aria-label="Menu"
            @click="leftDrawerOpen = !leftDrawerOpen"
          />

          <q-toolbar-title>
            <div class="title-font text-weight-medium">
              <q-btn style="font-size: 30px;" :ripple="false" to="/admin-home"
                >KOM GET YOUR BUCHA</q-btn
              >
            </div>
          </q-toolbar-title>
          <div>
            <q-btn-dropdown flat dense class="q-pa-sm" :label="`Hi, ${name}`">
              <q-list>
                <q-item>
                  <q-btn
                    label="Log Out"
                    class="full-width"
                    flat
                    @click="logout"
                  />
                </q-item>
                <q-item>
                  <q-btn
                    label="View Profile"
                    class="full-width"
                    flat
                    to="/admin-profile"
                  />
                </q-item>
              </q-list>
            </q-btn-dropdown>
          </div>
        </q-toolbar>
      </q-header>

      <q-drawer v-model="leftDrawerOpen">
        <q-list class="q-pt-xl">
          <q-item clickable v-ripple to="/all-users">
            <q-item-section avatar>
              <q-icon name="person" />
            </q-item-section>
            <q-item-section>View All Users</q-item-section>
          </q-item>

          <q-item clickable v-ripple to="/order-history">
            <q-item-section avatar>
              <q-icon name="history" />
            </q-item-section>
            <q-item-section>View All Order History</q-item-section>
          </q-item>
        </q-list>
      </q-drawer>

      <q-page>
        <div class="q-ma-lg q-pa-md q-gutter-sm">
          <q-table
            class="q-ma-lg q-pa-md center"
            title="Users"
            :data="users"
            :columns="columns"
            :filter="filter"
            row-key="email"
            wrap-cells
          >
            <template v-slot:top-right>
              <q-input
                borderless
                dense
                debounce="300"
                v-model="filter"
                placeholder="Search"
              >
                <template v-slot:append>
                  <q-icon name="search"></q-icon>
                </template>
              </q-input>
            </template>
          </q-table>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "AllUsers",
  data() {
    return {
      name: this.$store.state.currentUser.name,
      leftDrawerOpen: false,
      users: [],
      filter: "",
      //Columns of Table
      columns: [
        {
          name: "name",
          required: true,
          label: "Name",
          align: "left",
          field: row => row.name
        },
        {
          name: "email",
          align: "left",
          label: "Email",
          field: "email"
        }
      ]
    };
  },
  methods: {
    //Get all users
    getUsers() {
      const token = this.$store.state.token;
      this.$axios
        .get("/users", {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(res => {
          this.users = res.data;
        })
        .catch(() => {
          this.$q.notify({
            color: "red-4",
            position: "top",
            textColor: "white",
            icon: "error",
            message: "Something went wrong, please try again"
          });
        });
    }
  },
  created() {
    this.getUsers();
  }
};
</script>

<style scoped>
.home-btn {
  font-size: 25px;
  font-weight: bold;
  letter-spacing: 0.5rem;
}
.title-font {
  font-family: "customfont";
}
.center {
  margin: auto;
  width: 80%;
  text-align: center;
}
</style>
