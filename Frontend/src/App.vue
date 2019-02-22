<template>
  <div id="app">
    <MirrorItem />
    <NewsList />
  </div>
</template>

<script>

import NewsList from "./components/News/NewsList";
import MirrorItem from "./components/Mirror/MirrorItem";


export default {
  name: 'app',
  components: {
    MirrorItem,
    NewsList

  }
}
</script>

<style>
#app {
  font-family: 'Dosis','Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #cdcdcd;
  background-color: black;
  display: grid;
  grid-template-columns: auto 15%;
}

body {
  margin: 0;
  padding: 0;
}
</style>
