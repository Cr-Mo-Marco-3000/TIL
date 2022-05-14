import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // data
  state: {
    todos: [
      {
        title: '점심먹기',
        iscompleted: false,
        date: new Date().getTime()
      },
      {
        title: '응가하기',
        iscompleted: false,
        date: new Date().getTime() + 1
      }
    ]
  },
  // computed
  getters: {
  },

  // methods => data change를 담당
  mutations: {
    // 모든 mutations는 콜백함수인데 첫 번째 인자로 state 를 받는다 => 자동으로 넘어옴
    // mutations 는 애플리케이션의 데이터를 관리하는 애이다 보니 모두 대문자로 작성한다.
    CREATE_TODO: function (state, todo) {
      state.todos.push({title: '봉봉하기', iscompleted: false, date: new Date().getTime() + 2})
    }
  },  
  
  // methods => change를 제외한 나머지
  actions: {
    createTodo: function (context) {
      // context => 모든 기능이 다 들어 있다.
      context.commit('CREATE_TODO')
    },
    // createTodo: function ({ commit }) {
    //   // 구조 분해 할당을 통해 이렇게 할 수도 있다.
    //   commit('CREATE_TODO')
    // },
  },

})
