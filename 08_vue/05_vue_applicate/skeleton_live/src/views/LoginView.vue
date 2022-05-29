<template>
  <div>
    <h1>Login</h1>

    <form>
      <div>
        <label for="username">username: </label>
        <input type="text" id="username" required />
      </div>

      <div>
        <label for="password">password: </label>
        <input type="password" id="password" required />
      </div>

      <button>Login</button>
    </form>
  </div>
</template>

<script>
  // 모든 것들은 Actions 아니면 Getters에서 꺼낼 것! 고민할 필요 없다! 
  // import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'LoginView',
    computed: {},
    methods: {},
  }
</script>

<style></style>
