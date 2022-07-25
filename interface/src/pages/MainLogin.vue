<template>
  <q-page class="flex">
    <div
      class="flex"
      style="
        flex-direction: row;
        flex-wrap: wrap;
        align-content: stretch;
        justify-content: flex-start;
        align-items: flex-start;
        padding: 12px;
      "
    >
      <div class="flex" style="width: 100%; height: 10% !important">
        <img
          src="~assets/twitter_logo.png"
          alt=""
          style="width: 60px; height: 60px"
        />
      </div>
      <div
        class="flex"
        style="width: 100%; height: 30% !important  padding: 10px;"
      >
        <h2 class="happening">Happening now</h2>
      </div>
      <div class="flex" style="width: 100%; height: 10% !important">
        <h5 style="font-size: 35px; font-weight: 750">Join Twitter today.</h5>
      </div>
      <div style="width: 50%; height: 60%; !important">
        <SignUp />
        <p style="font-size: 10px; margin-bottom: 10px; padding: 0%">
          By signing up, you agree to the
          <span style="color: #1dc1f2">Terms of Service</span> and
          <span style="color: #1dc1f2">Privacy Policy,</span> including
          <span style="color: #1dc1f2">Cookie Use.</span>
        </p>
        <p style="padding: 0%; margin-bottom: 10px">
          <b>Already have an account?</b>
        </p>
        <SignIn />
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";

import SignUp from "components/signUp.vue";
import SignIn from "components/signIn.vue";
export default defineComponent({
  name: "IndexPage",
  components: { SignIn, SignUp },
});
</script>

<style>
.happening {
  font-family: TwitterChirpExtendedHeavy, "Merriweather";
  font-weight: 900;
  font-size: 80px;
  font-stretch: ultra-expanded;
}
</style>
