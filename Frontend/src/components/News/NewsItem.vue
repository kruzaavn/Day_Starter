<template>
  <div class="news-item" v-if="item.content">
    <div class="img-container">
      <img :src="item.urlToImage" alt="">
      <div class="link-container">
        <a :href="item.url"><h1>{{item.title}}</h1></a>
      </div>
    </div>
    <!--<div class="content-container">-->
      <!--<p>{{ item.content }}</p>-->
    <!--</div>-->
  </div>
</template>

<script>


export default {
  name: 'NewsItem',
  props: ['item'],
  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .news-item {
    border-bottom: 3px grey solid;
    background-color: #f0f0f0;
    display: inline-grid;
    grid-template-columns: auto;
  }
  .img-container {
    position: relative;
  }

  .link-container {
    position: absolute;
    top: 5px;
    left: 5px;
    max-width: 100%;
  }

  .content-container {
    padding: 0px 10px;
    font-size: .85em;
  }

  img {
    max-width: 100%;
    height: auto;
    filter: grayscale(100%);
  }

  h1 {
    color: #e1e1e1;
    text-shadow: 1px 1px #484848;
    padding: 0 1em 0 0;
    font-size: 1em;
  }

  a:link,  a:visited {
    text-decoration: none;
  }

  a:hover, a:active {
    text-decoration: underline;
    text-decoration-color: white;
  }

  p {
    padding: 0;
    margin: 0;
  }

</style>
