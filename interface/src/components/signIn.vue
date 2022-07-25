<template>
  <div class="container">
    <button
      type="button"
      class="btn"
      style="
        width: 100%;
        height: 40px;
        border-radius: 1in;
        color: #1dc1f2;
        background-color: white;
        border-color: black;
        font-weight: 600;
      "
      data-toggle="modal"
      data-target="#loginModal"
    >
      Login
    </button>
  </div>

  <div
    class="modal fade"
    id="loginModal"
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
              <div class="form-group">
                <input
                  type="email"
                  class="form-control"
                  id="email1"
                  placeholder="Your username or email address..."
                />
              </div>
              <div class="form-group">
                <input
                  type="password"
                  class="form-control"
                  id="password1"
                  placeholder="Your password..."
                />
              </div>
              <button type="button" class="btn btn-info btn-block btn-round">
                Login
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

  name: "SignIn",
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
