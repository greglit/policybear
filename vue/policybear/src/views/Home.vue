<template>
  <div>
    <b-container class="full-height">
      <navbar/>
      <b-row class="mb-5">
        <b-col cols="12" md="6" class="mb-4 mb-md-0">
            <img src="../assets/bearwithisle.svg" alt="policy bear" class="w-75 y-center"/>
        </b-col>
        <b-col cols="12" md="6">
          <h1 class="display-5 text-left rubik-bold my-md-4 m-2">"Hi, I'm Policy Bear!</h1>
          <h1 class="text-left m-2">Let's start creating simple arguments from complex data."</h1>
          <b-overlay :show="!datasets" rounded="sm">
            <b-card class="shadow m-2 mt-md-5 border-0 text-left rounded-lg">
              <data-form :requestData.sync="request.data" :meta="datasets"/>
            </b-card>
          </b-overlay>
        </b-col>
      </b-row>
    </b-container>
    <b-container fluid class="full-height">
      <b-row class="">
        <b-col cols="12" lg="3" class="mt-5 text-left card-form">
          <side-bar-card :request.sync="request" :meta="datasets" style="min-width:100px;"/>
        </b-col>
        <b-col cols="12" lg="9" class="w-100">
          <argument-card v-if="requestIsValid" :request="request" :meta="datasets[request.data.param]" class="my-5 mx-auto y-center"/>
          <h4 v-else class="text-center rubik-medium y-center">Please fill out missing fields on the left to generate a card.</h4>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
//import html2pdf from 'html2pdf.js'
import ArgumentCard from '../components/ArgumentCard.vue';
import DataForm from '../components/DataForm.vue';
import Navbar from '../components/Navbar.vue';
import SideBarCard from '../components/SideBarCard.vue';

export default {
  name: 'Home',
  components: {
    ArgumentCard,
    Navbar,
    DataForm,
    SideBarCard,
  },
  data() {
    return {
      datasets : null,
      request : {
        data : {
          param : null,
          station : null,
          startDateYear : null,
          startDateMonth: null,
          endDateYear : null,
          endDateMonth : null,
        },
        styling : {
          wording : 'difference',
          theme : 'classic',
          compareTo : null,
        }
      },
    }
  },
  methods: {
    fetchDataSets() {
      console.log(`${this.apiURL}datasets/`);
      fetch(`${this.apiURL}datasets/`, {})
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data);
        this.datasets = data;
      })
      .catch((error) => {
        console.log(error);
        this.fetchDataSets();
      });
    },
    /*print() {
      console.log('drucken!')
      let element = this.$refs.argument;
      html2pdf(element);
    }*/
  },
  computed: {
    requestIsValid() {
      const data = this.request.data;
      return data.param 
          && data.startDateYear 
          && data.endDateYear 
          && (data.startDateMonth && data.endDateMonth || data.startDateMonth == null && data.endDateMonth == null);
    },
    
  },
  created() {
    this.fetchDataSets();
  }
}
</script>

<style lang="scss" scoped>

.y-center {
  position: relative;
  top: 50%;
  transform: translateY(-50%);  
}



</style>

