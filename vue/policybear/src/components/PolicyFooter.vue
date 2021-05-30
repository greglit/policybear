<template>
  <footer>
    <wave-seperator svgWidth="500%" svgFill="#2e3440" class="mt-n4"/>
    <div class="bg-nord0">
      <a href="https://github.com/greglit/policybear"><b-icon-github class="git mb-2"/></a>
      <div><router-link :to="'/contact'" class="txt-nord6">Contact / Imprint</router-link></div>
      <div><router-link :to="'/privacy'" class="txt-nord6">Privacy Policy</router-link></div>
      <div class="py-3">
        Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
      </div>
    </div>
  </footer>
</template>

<script>
import WaveSeperator from './WaveSeperator.vue'

export default {
  name: 'PolicyFooter',
  components: {
    WaveSeperator
  },
  props: [],
  data() {
    return {
      
    }
  },
  computed: {
    
  },
  methods: {
    
  },
  watch: {
    
  },
}
</script>

<style lang="scss" scoped>
@import "../../node_modules/nord/src/sass/nord.scss";

  .git {
    font-size: 20pt;
    &:hover {
      color: $nord5;
    }
  }
</style>
