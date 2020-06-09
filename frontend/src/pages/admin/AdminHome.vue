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
        <q-select
          borderless
          clearable
          v-model="sortBy"
          :options="options"
          type="text"
          label="Sort By:"
          @input="findSort"
          style="width:15%"
          class="float-right q-mx-lg"
        >
          <template v-if="clearData" v-slot:append>
            <q-icon
              name="cancel"
              @click.stop="clearData = null"
              class="cursor-pointer"
            />
          </template>
        </q-select>
        <div class="container">
          <div class="q-pa-md row justify-center items-start q-gutter-md">
            <q-spinner
              v-if="loading"
              color="primary"
              size="3em"
              class="text-center"
            />
            <EditItem
              v-else
              style="margin: 10px"
              v-for="item in items"
              v-bind:key="item.id"
              :item="item"
              @item-updated="getItems"
            />
          </div>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
import EditItem from "../../components/EditItem.vue";
export default {
  name: "MainLayout",
  data() {
    return {
      leftDrawerOpen: false,
      name: this.$store.state.currentUser.name,
      items: null,
      loading: true,
      sortBy: null,
      clearData: null,
      options: [
        "Lowest Price",
        "Highest Price",
        "Lowest Inventory",
        "Highest Inventory"
      ]
    };
  },
  components: {
    EditItem
  },
  methods: {
    logout: function() {
      this.$store.dispatch("logout").then(this.$router.push({ path: "login" }));
    },
    getItems() {
      this.$axios
        .get("/items")
        .then(response => {
          const data = response.data;
          this.items = [];
          Object.keys(data).forEach(key => {
            if (data[key].inventory_count > 0) {
              this.items[key] = data[key];
            }
            this.items[key];
          });
          this.loading = false;
        })
        .catch(e => {
          console.log(e);
          this.$q.notify({
            color: "negative",
            position: "top",
            message: "Loading failed",
            icon: "report_problem"
          });
          this.loading = false;
        });
    },
    findSort: function(event) {
      if (this.sortBy == "Lowest Price") {
        this.onLowestPriceClick();
      } else if (this.sortBy == "Highest Price") {
        this.onHighestPriceClick();
      } else if (this.sortBy == "Lowest Inventory") {
        this.onLowestInventoryClick();
      } else {
        this.onHighestInventoryClick();
      }
    },
    onLowestPriceClick() {
      this.sortBy = "Lowest Price";
      this.items.sort(function(x, y) {
        if (x.price < y.price) {
          return -1;
        }
        if (x.price > y.price) {
          return 1;
        }
        return 0;
      });
    },
    onHighestPriceClick() {
      this.items.sort(function(x, y) {
        if (x.price < y.price) {
          return 1;
        }
        if (x.price > y.price) {
          return -1;
        }
        return 0;
      });
    },
    onHighestInventoryClick() {
      this.items.sort(function(x, y) {
        if (x.inventory_count < y.inventory_count) {
          return 1;
        }
        if (x.inventory_count > y.inventory_count) {
          return -1;
        }
        return 0;
      });
    },
    onLowestInventoryClick() {
      this.items.sort(function(x, y) {
        if (x.inventory_count < y.inventory_count) {
          return -1;
        }
        if (x.inventory_count > y.inventory_count) {
          return 1;
        }
        return 0;
      });
    }
  },
  created() {
    this.getItems();
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
.container {
  padding: 20px;
  justify-content: center;
}
</style>
