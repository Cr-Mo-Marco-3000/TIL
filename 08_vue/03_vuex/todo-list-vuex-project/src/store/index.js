import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  // data
  state: {
    todos: [
      {
        title: '점심먹기',
        isCompleted: false,
        date: new Date().getTime()
      },
      {
        title: '응가하기',
        isCompleted: false,
        date: new Date().getTime() + 1
      }
    ]
  },
  // computed
  // state를 기반으로 값을 계산해 냄
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount(state) {
      return state.todos.filter(todo => {
        return !todo.isCompleted
      }).length
    },
  },


  // methods => data change를 담당
  mutations: {
    // 모든 mutations는 콜백함수인데 첫 번째 인자로 state 를 받는다 => 자동으로 넘어옴
    // mutations 는 애플리케이션의 데이터를 관리하는 애이다 보니 모두 대문자로 작성한다.
    CREATE_TODO: function (state, todo) {
      state.todos.push(todo)
    },
    DELETE_TODO: function (state, todoItem) {
      // 내가 받은 todoItem이 todos에서 몇 번 인덱스에 있는가?
      const idx = state.todos.indexOf(todoItem)
      // splice => (어디부터, 몇 개를) 지우겠다
      state.todos.splice(idx, 1)
    },
    UPDATE_TODO(state, todo) {
      state.todos.map(todoitem => {
        if (todo === todoitem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    // LOAD_TODOS(state) {
    //   const todoString = localStorage.getItem('todos')
    //   state.todos = JSON.parse(todoString)
    // }
  },  
  
  // methods => change를 제외한 나머지
  actions: {
    // saveTodos({state}) {
    //   const jsonData = JSON.stringify(state.todos)
    //   localStorage.setItem('todos', jsonData)
    // },
    createTodo: function (context, todo) {
      // context => 모든 기능이 다 들어 있다.
      context.commit('CREATE_TODO', todo)
      // context.dispatch('saveTodos')
    },
    // createTodo: function ({ commit }) {
    //   // 구조 분해 할당을 통해 이렇게 할 수도 있다.
    //   commit('CREATE_TODO')
    // },
    // deleteTodo({ commit, dispatch }, todoItem) {
    deleteTodo({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
      // dispatch('saveTodos')
    },
    // updateTodo({commit, dispatch}, todo) {
    updateTodo({ commit }, todo) {
      commit('UPDATE_TODO', todo)
      // dispatch('saveTodos')

    }
  },
  plugins: [createPersistedState()],
})
