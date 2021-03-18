<template>
  <div id="app" class="h-100">
    <navbar/>
    <router-view class="h-100"/>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';

export default {
  name: 'Home',
  components: {
    Navbar,

  },
}
</script>

<style lang="scss">
@import './assets/styles/custom.scss';
@import '../node_modules/bootstrap/scss/bootstrap';
@import '../node_modules/bootstrap-vue/src/index.scss';
@import "../node_modules/nord/src/sass/nord.scss";

@font-face {
  font-family: "Rubik";
  src: local("Rubik"),   url(./assets/fonts/Rubik-Regular.ttf) format("truetype");
}
.rubik {
  font-family: Rubik;
}

@font-face {
  font-family: "Rubik-Medium";
  src: local("Rubik-Medium"),   url(./assets/fonts/Rubik-Medium.ttf) format("truetype");
}
.rubik-medium {
  font-family: Rubik-Medium;
}

@font-face {
  font-family: "Rubik-Bold";
  src: local("Rubik-Bold"),   url(./assets/fonts/Rubik-Bold.ttf) format("truetype");
}
.rubik-bold {
  font-family: Rubik-Bold;
}

html, body {
    max-width: 100%;
    overflow-x: hidden;

    height: 100%; margin: 0px; padding: 0px;
}

#app {
  font-family: Rubik, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: theme-color("primary") !important;
}


</style>
