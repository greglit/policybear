<template>
  <div id="app">
    <router-view/>
    <footer>
      <wave-seperator svgWidth="500%" svgFill="#2e3440" class="mt-n4"/>
      <div class="bg-nord0">
        <div><a href="#/about" class="txt-nord6">About</a></div>
        <div><a href="#/privacy" class="txt-nord6">Privacy Agreement</a></div>
        <div class="py-3">
          Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import WaveSeperator from './components/WaveSeperator.vue';

export default {
  name: 'Home',
  components: {
    Navbar,
    WaveSeperator,
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

#app {
  font-family: Rubik, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: theme-color("primary");
  //background-color: $nord0; try nightmode
}

.full-height {
  min-height: 100vh;
}

.nord-btn {
  color: $nord3;
  background-color: transparent;

  &:hover {
    color: $nord3;
    background-color: $nord6;
  }
}

.nord-btn-primary {
  color: $nord6;
  background-color: $nord10;

  &:hover {
    color: $nord6;
    background-color: $nord9;
  }
}

.bg-nord3 {
  background-color: $nord3;
}

.bg-nord0 {
  background-color: $nord0;
}

.bg-nord6 {
  background-color: $nord6 !important;
}

.txt-nord6 {
  color: $nord6 !important;
}

.txt-nord3 {
  color: $nord3 !important;
}

.y-center {
  position: relative;
  top: 50%;
  transform: translateY(-50%);  
}

</style>
