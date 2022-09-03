import { store } from "quasar/wrappers";
import { ref } from "vue";
import { createStore } from "vuex";

// import example from './module-example'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default store(function (/* { ssrContext } */) {
  const Store = createStore({
    state() {
      return {
        auth: false,
        username: ref(""),
      };
    },
  });

  return Store;
});
