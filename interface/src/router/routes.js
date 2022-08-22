const routes = [
  {
    path: "/",
    component: () => import("layouts/LoginLayout.vue"),
  },
  {
    path: "/home",
    component: () => import("layouts/HomeLayout.vue"),
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
