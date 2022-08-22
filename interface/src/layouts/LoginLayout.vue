<template>
  <q-layout view="lHh Lpr lFf">
    <div class="container-fluid" style="padding-left: 0; padding-right: 0">
      <div class="row" style="height: 600px">
        <div class="col-lg-6">
          <div class="image">
            <svg viewBox="0 0 24 24" aria-hidden="true" class="big-bird">
              <g>
                <path
                  d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"
                ></path>
              </g>
            </svg>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="content">
            <svg viewBox="0 0 24 24" aria-hidden="true" class="small-bird">
              <g>
                <path
                  d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"
                ></path>
              </g>
            </svg>

            <h1 class="mt-4">Happening now</h1>
            <h3 class="mt-4">Join Twitter today.</h3>

            <div class="button">
              <button
                href="#"
                class="btn btn-signup mt-4"
                data-bs-toggle="modal"
                data-bs-target="#signupModal"
              >
                signup
              </button>
              <div
                class="modal fade"
                id="signupModal"
                tabindex="-1"
                aria-labelledby="signupModalLabel"
                aria-hidden="true"
              >
                <div
                  class="modal-dialog rounded-3xl shadow-3xl relative w-auto pointer-events-none"
                >
                  <div
                    class="modal-content rounded-3xl border-none relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
                  >
                    <div class="max-w-2xl rounded-3xl mx-auto bg-white p-16">
                      <form>
                        <div class="grid gap-6 mb-6 lg:grid-cols-2">
                          <div>
                            <label
                              for="first_name"
                              class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                              >First name</label
                            >
                            <input
                              type="text"
                              id="first_name"
                              class="bg-gray-50 focus:outline-none border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                              placeholder="John"
                              required
                            />
                          </div>
                          <div>
                            <label
                              for="last_name"
                              class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                              >Last name</label
                            >
                            <input
                              type="text"
                              id="last_name"
                              class="bg-gray-50 focus:outline-none border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                              placeholder="Doe"
                              required
                            />
                          </div>
                          <div>
                            <label
                              for="phone"
                              class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                              >username</label
                            >
                            <input
                              type="text"
                              id="phone"
                              class="bg-gray-50 focus:outline-none border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                              placeholder="username"
                              required
                            />
                          </div>
                          <div>
                            <label
                              for="visitors"
                              class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                              >date of Birth</label
                            >
                            <input
                              type="Date"
                              id="visitors"
                              class="bg-gray-50 border focus:outline-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                              placeholder=""
                              required
                            />
                          </div>
                        </div>
                        <div class="mb-6">
                          <label
                            for="email"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                            >Email address</label
                          >
                          <input
                            type="email"
                            id="email"
                            class="bg-gray-50 focus:outline-none border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="john.doe@company.com"
                            required
                          />
                        </div>
                        <div class="mb-6">
                          <label
                            for="password"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                            >Password</label
                          >
                          <input
                            type="password"
                            id="password"
                            class="bg-gray-50 focus:outline-none border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="•••••••••"
                            required
                          />
                        </div>
                        <div class="mb-6">
                          <label
                            for="confirm_password"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                            >Confirm password</label
                          >
                          <input
                            type="password"
                            id="confirm_password"
                            class="bg-gray-50 focus:outline-none border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="•••••••••"
                            required
                          />
                        </div>
                        <div class="flex items-start mb-6">
                          <div class="flex items-center h-5">
                            <input
                              id="remember"
                              type="checkbox"
                              value=""
                              class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800"
                              required
                            />
                          </div>
                          <label
                            for="remember"
                            class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-400"
                            >I agree with the
                            <a
                              href="#"
                              class="text-blue-600 hover:underline dark:text-blue-500"
                              >terms and conditions</a
                            >.</label
                          >
                        </div>
                        <button
                          type="submit"
                          class="text-white flex justify-center bg-blue item-center hover:bg-blue focus:ring focus:outline-none focus:ring-blue font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue dark:hover:bg-blue dark:focus:ring-blue"
                        >
                          Submit
                        </button>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
              <button
                href="#"
                class="btn btn-login mt-3"
                data-bs-toggle="modal"
                data-bs-target="#signinModal"
              >
                Log in
              </button>
              <div
                class="modal fade"
                id="signinModal"
                tabindex="-1"
                aria-labelledby="signupinLabel"
                aria-hidden="true"
              >
                <div class="modal-dialog relative w-auto pointer-events-none">
                  <div
                    class="modal-content rounded-3xl shadow-3xl relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
                  >
                    <!-- Modal content -->
                    <div class="relative bg-white rounded-3xl px-12 py-12">
                      <div class="py-6 px-6 lg:px-8">
                        <div class="flex">
                          <h3
                            class="mb-4 text-xl font-medium text-gray-900 dark:text-white"
                          >
                            Sign in to our platform
                          </h3>
                        </div>
                        <form class="space-y-6" action="#">
                          <div>
                            <label
                              for="email"
                              class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                              >Your email</label
                            >
                            <input
                              type="email"
                              name="email"
                              id="email"
                              class="bg-gray-50 focus:outline-none border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                              placeholder="name@company.com"
                              required
                            />
                          </div>
                          <div>
                            <label
                              for="password"
                              class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                              >Your password</label
                            >
                            <input
                              type="password"
                              name="password"
                              id="password"
                              placeholder="••••••••"
                              class="bg-gray-50 border focus:outline-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                              required
                            />
                          </div>
                          <div class="flex justify-between">
                            <div class="flex items-start">
                              <div class="flex items-center h-5">
                                <input
                                  id="remember"
                                  type="checkbox"
                                  value=""
                                  class="w-4 h-4 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300 dark:bg-gray-600 dark:border-gray-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800"
                                  required
                                />
                              </div>
                              <label
                                for="remember"
                                class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                                >Remember me</label
                              >
                            </div>
                            <a
                              href="#"
                              class="text-sm text-blue-700 hover:underline dark:text-blue-500"
                              >Lost Password?</a
                            >
                          </div>
                          <button
                            type="submit"
                            class="w-full focus:outline-none text-white bg-blue font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                          >
                            Login to your account
                          </button>
                          <div
                            class="text-sm font-medium text-gray-500 dark:text-gray-300"
                          >
                            Not registered?
                            <a
                              href="#"
                              class="text-blue-700 hover:underline dark:text-blue-500"
                              data-bs-toggle="modal"
                              data-bs-target="#signupModal"
                              >Create account</a
                            >
                          </div>
                        </form>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="footer">
        <nav>
          <a href="#">About</a>
          <a href="#">help center</a>
          <a href="#">terms of service</a>
          <a href="#">privacy policy</a>
          <a href="#">cookie policy</a>
          <a href="#">ads info</a>
          <a href="#">blog</a>
          <a href="#">status</a>
          <a href="#">careers</a>
          <a href="#">brand resources</a>
          <a href="#">advertising</a>
          <a href="#">merketing</a>
          <a href="#">twitter for business</a>
          <a href="#">developers</a>
          <a href="#">directory</a>
          <a href="#">settings</a>
          <div>&copy; 2021 Twitter, Inc.</div>
        </nav>
      </div>
    </div>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
export default defineComponent({
  name: "LoginLayout",
  components: {},
});
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Lato&display=swap");

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Lato", sans-serif;
  min-height: 100vh;
  overflow-x: hidden;
}

.container {
  /* width: 100vw;
  
  /* display: flex; */
  /* flex-wrap: wrap; */
  /* height: 87vh; */
  padding: 0px;
}

.image {
  height: 100%;
  background-image: url("../assets/cover_image.png");
  /* flex: 0 1 45vw; */
  /* position: relative; */
}

.content {
  flex: 0 0 50vw;
  /* display: flex; */
  /* flex-direction: column; */
  /* align-items: flex-start; */
  /* justify-content: space-evenly; */
  padding: 2rem;
}

.big-bird {
  width: 16rem;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  fill: #fff;
}

.small-bird {
  width: 3.5rem;
  fill: #1da1f2;
}

h1,
h3 {
  color: #0f1419;
  font-weight: 900;
}

h1 {
  font-size: 5.5vw;
}

h3 {
  font-size: 2.3rem;
}

.btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24rem;
  height: 3.3rem;
  border-radius: 10vw;
  font-size: 1rem;
  text-decoration: none;
  font-weight: 700;
}

.btn-signup {
  background: #1da1f2;
  color: #fff;
  transition: all 0.2s ease;
  margin-bottom: 20px;
}

.btn-signup:hover {
  background: #1f94dd;
}

.btn-login {
  border: 1px solid #1da1f2;
  color: #1da1f2;
}

.footer {
  padding: 1rem 2%;
}

.footer nav {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.footer nav a,
.footer nav div {
  text-decoration: none;
  font-size: 13px;
  color: #536471;
  margin: 0.3rem 0.5rem;
  text-transform: capitalize;
  border-bottom: 1px solid transparent;
  transition: all 0.2s ease;
}

.footer nav a:hover {
  border-bottom: 1px solid #536471;
}

/* @media (max-width: 1050px) {
  .content {
    order: -1;
    max-width: 600px;
    height: 80vh;
    margin: 0 auto;
  }

  .image {
    height: 50vh;
    flex: 0 1 100vw;
  }

  .button {
    display: flex;
  }

  .btn {
    width: 15rem;
    margin-right: 1rem;
  }

  h1 {
    font-size: 8vw;
  }
} */

@media (max-width: 580px) {
  .content {
    padding: 2rem;
    margin: 0;
  }

  .button {
    flex-direction: column;
  }

  .btn {
    width: 25rem;
  }
  h1 {
    font-size: 10vw;
  }

  h3 {
    font-size: 1.7rem;
  }
}
</style>
