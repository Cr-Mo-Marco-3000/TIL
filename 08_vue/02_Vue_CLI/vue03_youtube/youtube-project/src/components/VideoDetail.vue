<template>
  <div class="video-detail" v-if="video">
  <div class="video-container">
    <iframe :src="video.id.videoID" frameborder="0"></iframe>
  </div>
  <div class="video-container">
    <h2>{{ video.snippet }}</h2>
  </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name:"VideoDetail",
  props: {
    video:{
      type: [String, Object]
      }
  },
  computed: {
    videoURI: function () {
      const videoID = this.
  }},
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>
.video-datail {
  width: 70%;
  padding-right: 1rem;
}
.video-container {
  position: relative;
  padding-top: 50%;
}

.video-container > iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.detail {
  margin-top: 20px;
  padding: 20px;
  border: solid 1px lightgray;
  border-radius: 10px;
}

</style>