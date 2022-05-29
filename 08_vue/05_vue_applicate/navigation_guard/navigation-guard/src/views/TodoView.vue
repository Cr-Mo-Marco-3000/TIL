<template>
  <div>
    <h1>
      투두투두
    </h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoView',
  methods: {
    getTodo: function() {
      axios.get('http://127.0.0.1:8000/todo')
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
        this.$router.push({ name: 'NotFound404' })

        // if (err.response.status === 404) {
        //   this.$router.push({name: 'NotFound404'})
        // }
      })
    }
  },
  created() {
    // 페이지가 생성될 때 getTodo 메소드 실행
    this.getTodo()
  }
}

</script>

<style>

</style>