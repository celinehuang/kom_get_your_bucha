const routes = [
  { path: "", redirect: "/home" },
  {
    path: "/home",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Home.vue") }]
  },
  {
    path: "/classic-kombucha",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Classic.vue") }]
  },
  {
    path: "/limited-edition",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/LimitedEdition.vue") }
    ]
  },
  {
    path: "/alcoholic",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Alcoholic.vue") }]
  },
  {
    path: "/equipment",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Equipment.vue") }]
  },
  {
    path: "/all-products",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/AllProducts.vue") }]
  },
  {
    path: "/recipes",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Recipes.vue") }]
  },
  {
    path: "/story",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Story.vue") }]
  },
  {
    path: "/contact",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Contact.vue") }]
  },
  {
    path: "/login",
    component: () => import("pages/UserLogin.vue")
  },
  {
    path: "/admin",
    component: () => import("pages/admin/AdminLogin.vue")
  },
  {
    path: "/checkout",
    meta: { requiresAuth: true },
    component: () => import("pages/Checkout.vue")
  }
];

// Always leave this as last one
if (process.env.MODE !== "ssr") {
  routes.push({
    path: "*",
    component: () => import("pages/Error404.vue")
  });
}

export default routes;
