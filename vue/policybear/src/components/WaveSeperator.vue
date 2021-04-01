<template>
  <div class="wave-wrapper">
    <svg :width="svgWidth" height="45" viewBox="0 0 1178 54" :fill="svgFill" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" style="bottom:-1px;position:relative;min-width:1178px">
      <path d="M66.5 11.1261C40.5 -1.27388 11.3333 5.95946 0 11.1261V53.6261H1177.5V11.1261C1177.5 11.1261 1114 28.1261 1080 11.1261C1046 -5.87389 1032 -1.37387 1001 11.1261C970 23.6261 941.5 26.6261 912 11.1261C882.5 -4.37389 855.5 1.12613 834.5 11.1261C813.5 21.1261 803.5 19.6261 761 11.1261C718.5 2.62611 689 0.126134 651 11.1261C613 22.1261 584.5 22.6261 550.5 11.1261C516.5 -0.373885 491.5 -2.87387 460.5 11.1261C429.5 25.1261 411 25.1261 380 11.1261C349 -2.87389 337.5 -1.37387 309 11.1261C280.5 23.6261 260 24.1261 227.5 11.1261C195 -1.87387 179.5 -2.87388 144 11.1261C108.5 25.1261 99 26.6261 66.5 11.1261Z"/>
    </svg>
  </div>
</template>

<script>
export default {
  props: {
    svgWidth : {
      type : String,
      default : '105%'
    },
    svgFill : {
      type : String,
      default : '#4C566A'
    }
  }
}
</script>


<style lang="scss" scoped>
  .wave-wrapper {
    overflow: hidden;
    width: 100%;
  }
</style>
