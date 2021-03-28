<template>
  <div>
    <h1>This Login Page</h1>
    <div id="email">
      <label for="">Email:</label>
      <br />
      <input type="email" name="email" id="email" />
    </div>
    <div id="password">
      <label for="">Password:</label>
      <br />
      <input type="password" name="password" id="password" />
    </div>
    <input type="submit" value="Login" @click="toLogin" />
  </div>
</template>

<script>
export default {
  methods: {
    toLogin() {
      console.log(this.$api);
      this.$api
        .post("/")
        .then((result) => {
          console.log(result);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
