<template>
  <div id="app">
    <header>
      <SearchBar @input-search="onInputSearch" :videoLength="videos.length" />
    </header>
    <section>
      <VideoDetail :video="selectedVideo" />
      <VideoList :videos="videos" @select-video="onVideoSelect"/>
    </section>
  </div>
</template>

<script>
// @ 붙이면 앞 뒤 생략가능
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'
import axios from 'axios'

// API key는 깃에 올리면 안 된다!
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'


export default {
  name: 'App',
  data: function () {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: '',
    }
  },
  components: {
    // 축약 문법을 쓴 것
    // SearchBar: SearchBar
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    onVideoSelect: function (video) {
      this.selectedVideo = video
    },

    onInputSearch: function (inputText) {
      this.inputValue = inputText
      const params = {
        key: API_KEY,
        part: 'snippet',
        q: this.inputValue,
        type: 'video',
      }

      axios.get(API_URL, {params,})
      .then(res => {
        console.log(res)
        console.log(res.data.items)
        this.videos = res.data.items
        // 검색하면 첫 번째 영상을 selected Video로 지정
        // if (!this.selectedVideo) { // selectedVideo가 없다면
        //   this.selectedVideo = this.videos[0]
        // }
        this.selectedVideo = this.video[0]
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

section, header {
  width: 80%; /* 전체 넓이의 80% */
  margin: 0 auto; /* 양 옆의 margin을 균등하게 배분(가로 가운데 정렬) */
  padding: 1rem 0; /* 위, 아래 padding을 1rem씩 주기 */
}

section {
  display: flex; /* Detail, List를 가로 배치 */
}



#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
