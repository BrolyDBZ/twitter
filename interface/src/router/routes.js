const routes = [
  {
    path: "/home",
    component: () => import("layouts/LoginLayout.vue"),
    children: [{ path: "", component: () => import("pages/MainLogin.vue") }],
  },
  {
    path: "/",
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
