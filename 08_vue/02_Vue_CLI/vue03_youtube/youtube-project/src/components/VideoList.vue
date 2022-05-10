<template>
  <div class="col">
    <ul class="list-group">
      <VideoListItem v-for="(video, idx) in videos" :key="idx" :video="video" 
      @select-video="onSelectVideo"
      />
      
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  props: {
    videos: Array,
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', this.video)
    }
  },
  components: {
    VideoListItem,
  },
}
</script>

<style>
  
</style>