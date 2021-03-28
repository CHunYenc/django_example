import Vue from "vue";
import VueRouter from "vue-router";
import Base from "../views/Base.vue";
import Index from "../views/L1/Index.vue";
import Login from "../views/L1/Login.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "index",
    component: Index,
  },
  {
    path: "/u",
    component: Base,
    children: [
      {
        path: "/u/login",
        name: "login",
        component: Login,
      },
    ],
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/L1/About.vue"),
  },
  {
    path: "*",
    redirect: { name: "About" },
  },
];

const router = new VueRouter({
  routes,
});

export default router;
