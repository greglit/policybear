<template>
  <div>
    <div class="mx-auto  rounded mt-5 py-2 d-flex flex-wrap justify-content-center" style="max-width:200px">
      <div class="mx-1"><b-button @click="shareCard()" variant="border-0" class="nord-btn-dark w-100"><b-icon-share-fill class="mr-1"/>Share</b-button></div>
      <div class=""><b-button @click="editCard()" variant="border-0" class="nord-btn-dark w-100"><b-icon-pencil-square class="mr-1"/>Edit</b-button></div>
    </div>
    <b-carousel
      v-model="slideIndex"
      controls
      indicators
      :interval="0"
      class="mt-2 text-center"
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
      slideIndex: 0,
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
  methods: {
    shareCard() {
      store.cardRequest = this.exampleCards[this.slideIndex]
      this.$router.push('/share/')
    },
    editCard() {
      store.cardRequest = this.exampleCards[this.slideIndex]
      this.$router.push('/editor/')
    },
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
