<template>
  <div class="hello">
    <NewsItem v-for="(item, index) in list.data.articles" :key="index" v-bind:item="item" />
  </div>
</template>

<script>
import axios from 'axios'
import NewsItem from './NewsItem';

export default {
  name: 'NewsList',
  components: {
    NewsItem
  },
  props: {
    msg: String
  },
  data() {
    return {
      list: { data: {'articles': []}},
      polling: null
    }
  },

  methods: {

    getData: function () {
      axios.get('http://localhost:8081/api/news/').then(response => (this.list = response))
    },

    pollData: function() {
      this.polling = setInterval(() => this.getData(), 15 * 60 * 1000)
    }

  },
  beforeDestroy () {
    clearInterval(this.polling)
  },

  created: function () {
      this.getData();
      this.pollData()
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
