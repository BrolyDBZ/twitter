<template>
  <q-layout view="lHh Lpr lFf">
    <div class="row" style="">
      <div id="Himage" style="width: 52%">
        <img
          src="~assets/loginPage_image.jpg"
          style="width: 100%; height: 100%; max-width: 100%; max-height: 100%"
          alt=""
        />
      </div>
      <div class="column" style="width: 48%">
        <router-view />
      </div>
    </div>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "LoginLayout",
});
</script>

<style>
* {
  box-sizing: border-box;
}

.column {
  float: left;
  padding: 10px;
  height: 100%;
}

.row:after {
  content: "";
  display: flex;
  clear: both;
}

@media screen and (max-width: 600px) {
  .column {
    width: 100%;
  }
  #Himage {
    display: none !important;
  }
}
</style>
