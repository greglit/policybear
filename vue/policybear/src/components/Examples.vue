<template>
  <div>
    <b-carousel
      controls
      indicators
      :interval="0"
      class="mt-5 text-center"
      img-width="800"
      img-height="300"
    >
      <b-carousel-slide v-for="card in exampleCards" :key="JSON.stringify(card)" style="width:100%;" class="mb-4">
        <template #img>
          <div style="width:50vw" class="mx-auto card-wrapper">
            <argument-card  :request="card" :light="false"/>
          </div>
        </template>
      </b-carousel-slide>
    </b-carousel>
    
    <div>loading...</div>
    
  </div>
</template>

<script>
import store from '../store.js'
import ArgumentCard from './ArgumentCard.vue'

export default {
  name: 'Examples',
  components: {
    ArgumentCard,
  },
  data() {
    return {
      exampleCards: [
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
            theme : 'drastic',
            compareTo : null,
          }
        },
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
        
      ]
    }
  },
}
</script>

<style lang="scss" scoped>
  .card-wrapper {
    width:50vw;
  }

  @media (max-width: 992px) {
    .card-wrapper {
      width:85vw !important;
    }
  }
</style>
