<template>
  <div class="container">
    <button
      type="button"
      class="btn btn-primary btn-lg btn-block"
      style="width: 100%; height: 40px; border-radius: 1in; background-color;: #57cef2; opacity: 0.8;font-weight:600; font-size:18px;padding:0px"
      data-toggle="modal"
      data-target="#signupModal"
    >
      Sign up with email..
    </button>
  </div>

  <div
    class="modal fade"
    id="signupModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header border-bottom-0">
          <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="form-title text-center">
            <h4>Login</h4>
          </div>
          <div class="d-flex flex-column text-center">
            <form>
              <div class="form-group" style="width: 70%">
                <input
                  type="text"
                  class="form-control"
                  id="firstname"
                  placeholder="first name"
                  style="margin-left: 25%"
                />
              </div>
              <div class="form-group" style="width: 70%">
                <input
                  type="text"
                  class="form-control"
                  id="lastname"
                  placeholder="lastname"
                  style="margin-left: 25%"
                />
              </div>
              <div class="form-group" style="width: 70%">
                <input
                  type="date"
                  class="form-control"
                  id="birth date"
                  placeholder="birth date"
                  style="margin-left: 25%"
                />
              </div>
              <div class="form-group" style="width: 70%">
                <input
                  type="text"
                  class="form-control"
                  id="username"
                  placeholder="username"
                  style="margin-left: 25%"
                />
              </div>
              <div class="form-group" style="width: 70%">
                <input
                  type="email"
                  class="form-control"
                  id="email"
                  placeholder="email"
                  style="margin-left: 25%"
                />
              </div>
              <div class="form-group" style="width: 70%">
                <input
                  type="password"
                  class="form-control"
                  id="password1"
                  placeholder="password"
                  style="margin-left: 25%"
                />
              </div>
              <div class="form-group" style="width: 70%">
                <input
                  type="password"
                  class="form-control"
                  id="password2"
                  placeholder="re-enter your password"
                  style="margin-left: 25%"
                />
              </div>
              <button type="button" class="btn btn-info btn-block btn-round">
                signup
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // name: 'ComponentName',
  name: "SignUp",
  setup() {
    return {};
  },
};
</script>

<style>
.container {
  padding: 2rem 0rem;
}

@media (min-width: 576px) {
  .modal-dialog {
    max-width: 600px;

    .modal-content {
      padding: 1rem;
    }
  }
}

.modal-header {
  .close {
    margin-top: -1.5rem;
  }
}

.form-title {
  margin: -2rem 0rem 2rem;
}

.btn-round {
  border-radius: 3rem;
}

.delimiter {
  padding: 1rem;
}

.social-buttons {
  .btn {
    margin: 0 0.5rem 1rem;
  }
}

.signup-section {
  padding: 0.3rem 0rem;
}
</style>
