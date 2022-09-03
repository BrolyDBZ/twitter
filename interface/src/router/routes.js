const routes = [
  {
    path: "/",
    component: () => import("layouts/LoginLayout.vue"),
    meta: { auth: false },
  },
  {
    path: "/home",
    component: () => import("layouts/HomeLayout.vue"),
    name: "home",
    meta: { auth: true },
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
