<template>
  <div>
    <b-carousel
      style="display:block;"
      v-if="meta"
      controls
      indicators
      v-model="slide"
      class="mt-5"
    >
      <b-carousel-slide v-for="card in exampleCards" :key="JSON.stringify(card)" style="width:300px">
        <argument-card  :request="card" :meta="meta[card.data.param]" :light="false" style="width:300px"/>
      </b-carousel-slide>
    </b-carousel>

    <argument-card v-for="card in exampleCards" :key="JSON.stringify(card)" :request="card" :meta="meta[card.data.param]" :light="false" style="width:450px"/>
    
    <div>loading...</div>
    
  </div>
</template>

<script>
import ArgumentCard from './ArgumentCard.vue'

export default {
  name: 'Examples',
  components: {
    ArgumentCard,
  },
  props: ['meta'],
  data() {
    return {
      slide: 0,
      exampleCards: [
        {
          data : {
            param : 'ch4',
            station : 'GAT',
            startDateYear : 2016,
            startDateMonth: null,
            endDateYear : 2021,
            endDateMonth : null,
            dateFormat : 'annual',
          },
            styling : {
            wording : 'difference',
            theme : 'classic',
            compareTo : 'cows',
          }
        },
        {
          data : {
            param : 'co2',
            station : 'LIN',
            startDateYear : 2016,
            startDateMonth: 2,
            endDateYear : 2021,
            endDateMonth : 2,
            dateFormat : 'monthly',
          },
            styling : {
            wording : 'difference',
            theme : 'news',
            compareTo : 'cars',
          }
        },
        {
          data : {
            param : 'co2',
            station : 'LIN',
            startDateYear : 2016,
            startDateMonth: 2,
            endDateYear : 2021,
            endDateMonth : 2,
            dateFormat : 'monthly',
          },
            styling : {
            wording : 'difference',
            theme : 'news',
            compareTo : 'cars',
          }
        },
      ]
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

</style>
