<template>
  <div id="app">
    <Navbar />
    <OpenAIInterface />
  </div>
</template>


<script>
import Navbar from './components/Navbar.vue'
import OpenAIInterface from './components/OpenAIInterface.vue'


export default {
  name: 'App',
  components: { OpenAIInterface, Navbar }
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
