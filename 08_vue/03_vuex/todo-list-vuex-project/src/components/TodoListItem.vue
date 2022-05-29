<template>
  <div>
    <!-- 특수 문법 => updateTodo 걸어두고, 실행할 때 인자로 todo 넘겨주세요 -->
    <span @click="updateTodo(todo)" :class="{ 'is-completed': todo.isCompleted}">
      {{ todo.title }}
    </span>
    <button @click="deleteTodo(todo)" >[삭제]</button>
  </div>
</template>

<script>
// import vuex from 'vuex'
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object
    }
  },
  methods: {
    // actions의 'deleteTodo' 함수를 바로 쓰고 싶다.
    // deleteTodo: function () {
    //  console.log(mapActions) // vuex가 어떤 것 들을 갖고 있는지 보자 => mapGetters 등등 다 갖고 있음
    //  vuex.mapActions(['deleteTodo', 'createTodo'])} // 얘의 반환값이 store의 actions 안의 deleteTodo, createTodo 를 담고 있는 객체

      // actions의 deleteTodo 함수를 바로 쓰고 싶다.
      // deleteTodo : vuex.mapActions(['deleteTodo', 'createTodo']).deleteTodo
      // deleteTodo : mapActions(['deleteTodo', 'createTodo']).deleteTodo


    //   // store에 삭제 요청
    //   // 두 번째 인자로 무엇을 삭제할 지 보내 주어야 한다.
    //   this.$store.dispatch('deleteTodo', this.todo)
    // }
    ...mapActions(['createTodo', 'updateTodo', 'deleteTodo']),
    }
  }

</script>

<style>
.is-completed {
  text-decoration: line-through;
}
</style>