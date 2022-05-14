import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [
      {
        title: '할 일1',
      completed: false,
    },
      {
        title: '할 일2',
      completed: false,
    },
    ],
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
    allTodosCount: function (state) {
      return state.todos.length
    }
  },
  mutations: {
    // State를 변경할 때 씀
    // 비동기 처리로 state를 변경하면 데이터가 이상해질 수 있어서 동기적 코드만 작성
    // 첫 번째 인자로 항상 state를 받고 commit 메소드로 호출(사용)
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO : function (state, todoItem) {
      // console.log(state)
      // 1. todoITem이 첫 번째로 만나는 요소의 index를 가져옵니다.
      const index = state.todos.indexOf(todoItem)

      // 2. 해당 index 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
      this.state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      // 배열의 각 요소에 함수를 적용 시킨 뒤 새로운 배열을 만들어서 state.todos에 할당
      state.todos = state.todos.map((todo) => {
        // 1. 클릭한 todoItem과 일치하는 state의 todo를 찾으면, 
        if (todo === todoItem) {
          // todo.completed = !todo.completed : return 없어도 된다.
          return {...todo, completed: !todo.completed }
      }

      return todo
      })
    }
  },
  actions: {
    // 비지니스 로직
    // state를 직접 변경하진 않고, mutations에 정의된 메소드 호출
    // 비동기 작업, Data fetch 및 처리 & 가공
    // Data fetch : 데이터를 가져옴
    // 첫 번째 인자로 항상 context를 받고 dispatch 메소드로 호출(사용)
    createTodo: function ({ commit }, todoItem) {
      // console.log(context)
      // console.log('---')
      // console.log(todoItem)
      // console.log(context.state.todos)
      // console.log(state.todos)
      // context.commit('CREATE_TODO', todoItem)
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    },
  },
  modules: {
    
  }
})
