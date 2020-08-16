<template>
  <div id="app">
    <Navbar />
    <div id="content">
    <OpenAIInterface />
  </div>
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
  text-align: right;
  color: #2c3e50;
  font-size: 12px; 
}

#content{
  margin-top: 20px;
  margin-right: 260px;


}
</style>
