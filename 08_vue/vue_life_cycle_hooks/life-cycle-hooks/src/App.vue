<template>
  <div id="app">
    <h3 ref="appText">{{ text }}</h3>
    <button @click="increase">Update Data</button>
    <h3 ref="appNumber">{{ number }}</h3>
    <hr>
    <hr>
    <button @click="toggleActive">Toggle ChildItem Component</button>
    <ChildItem ref="child" v-if="isActive"/>
  </div>
</template>

<script>
import ChildItem from './components/ChildItem.vue'

export default {
  name: 'App',
  components: {
    ChildItem
  },
  provide: {
    age: 20
  },
  data() {
    return {
      number: 0,
      text: '초기 데이터',
      isActive: true
    }
  },
  computed: {
    computedText() {
      return [`%c   ==  computed called  ==`, "color:blue"]
    }
  },
  methods: {
    increase() {
      console.log('%c   ==  increase method called  ==', "color:red")
      this.number++
    },
    toggleActive() {
      console.log('%c   ==  isActice Toggle  ==', "color:red")
      this.isActive = !this.isActive
    }
  },

  beforeCreate() {
    console.log('--------beforeCreate App.vue---------')
    console.log(this.text) // undefined
    this.text = 'App.vue instance가 create된 직후입니다.' // data 접근 가능 X
    console.log(this.$data) // undefined
    alert(this.text) // App.vue instance가 create된 직후입니다.
  },


  created() {
    console.clear() // log 제거
    console.log(this)
    console.log('--------created App.vue---------')
    console.log(this.$refs.appText) // undefined dom 접근 불가능
    console.log(this.$data)
    this.text = 'App.vue instance가 create 되었습니다.', // data 접근 가능

    this.increase() // methods 접근 가능
    console.log(...this.computedText) // computed 호출 가능
    alert(this.text) // App.vue가 create 되었습니다.
  },


  beforeMount() {
    console.clear() // log 제거
    console.log('--------beforeMount App.vue---------')
    console.log(this.$refs.appText) // undefined dom 접근 불가능
    this.text = 'DOM이 부착(mount)되기 직전에 호출됩니다..'
    alert(this.text)
  },


  mounted() {
    console.log('--------mounted App.vue---------')
    console.log(this.$refs.appText) // dom 접근 가능
    this.text = 'App.vue가 mount되었습니다.'
    alert(this.text)
  },


  beforeUpdate() {
    console.clear() // log 제거
    console.log('--------beforeupdate App.vue---------')
    // console.log(this.number) // 1 
  },


  updated() {
    console.log('--------updated App.vue---------')
    // console.log(this.number) // 1
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
