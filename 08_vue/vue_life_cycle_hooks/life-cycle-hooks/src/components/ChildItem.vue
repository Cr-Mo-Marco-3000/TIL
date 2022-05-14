<template>
  <div>
    <h1 ref="childText">{{ childText }}</h1>
  </div>
</template>

<script>
export default {
  name: 'ChildItem',
  inject: ['age'],
  data() {
    return {
      childText: 'Init Text'
    }
  },
  
  created() {
    console.log('%c     ----- created Child.vue -----', "color:green")
  },

  mounted() {
    // this.$nextTick(() => {
    //   this.childText = 'mount가 모두 완료 된 후, 실행됩니다.'
    // })
    console.log('%c     ----- mounted Child.vue -----', "color:red")
    this.childText = 'Child Component가 Mount 되었습니다.'
    console.log(`%c      == ${this.childText}  ==`, "color:blue")
    alert(this.childText)
  },


  beforeDestroy() {
    console.log('%c     -----  Child.vue is beforeDestroy -----', "color:orange")
    this.childText = 'beforeDestroy'
    console.log(`%c     == ${this.childText} ==`, "color:gray")
    console.log(`%c     ${this.$refs.childText.innerText}`, "color:gray") // undifined dom은 접근 불가
  },


  destroyed() {
    console.log('%c     -----  Child.vue is Destroyed -----', "color:red")
    this.childText = 'destroyed'
    console.log(`%c     == ${this.childText} ==`, "color:gray")
    console.log(`     ${this.$refs.childText}`) // undifined dom은 접근 불가
  }
}
</script>