<template>
  <li class="list-group-item" @click="selectVideo">
    <img :src="youtubeImageSrc" alt="youtube-thumbnail">
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods:{
    selectVideo: function() {
      this.$emit('select-video', this.video)
    }},
    
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>
  .list-group-item {
    display: flex;
    margin-bottom: 1rem;
    cursor: pointer;
  }

  .list-group-item:hover {
    background: #eee;
  }

  .list-group-item img{
    height: fit-content; /* 텍스트가 길어져도 이미지가 늘어나지 않도록 설정 */
    margin-right: 0.5rem; /* 이미지와 텍스트 사이의 여백 */
  }
</style>