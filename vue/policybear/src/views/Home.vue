<template>
  <div class="h-100">
    <b-container class="h-100">
      <b-row class="h-100 mb-5">
        <b-col cols="12" md="6" class="mb-4 mb-md-0">
            <img src="../assets/polarbear-transparent.png" alt="policy bear" class="w-75 y-center"/>
        </b-col>
        <b-col cols="12" md="6">
          <h1 class="display-5 text-left rubik-bold my-md-5 m-2">"Hi, I'm Policy Bear!</h1>
          <h1 class="text-left m-2">Let's start creating simple arguments from complex data."</h1>
          <!--<b-icon-arrow-down-circle-fill animation="cylon-vertical" font-scale="4" style=""/>-->
          <b-card class="shadow m-2 mt-md-5 border-0 text-left rounded-lg">
            <b-form class="mb-2">
              <label for="pick-parameter" class="text-left mb-n1">Choose Parameter</label>
              <b-form-select id="pick-parameter" v-model="request.selectedDataset" :options="parameterOptions" class="w-100 mb-2"/>
              <label for="pick-station" class="text-left mb-n1">Choose Station</label>
              <b-form-select id="pick-station" v-model="request.selectedStation" :options="stationOptions" class="w-100 mb-2"/>
              <label for="date" class="mb-n1">Select Timeframe</label>
              <b-input-group class="w-100" id="date">
                <b-form-select v-model="request.startDate" :options="yearOptions" class="" />
                <b-form-select v-model="request.endDate" :options="yearOptionsReverse" class="" />
              </b-input-group>
            </b-form>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <b-container fluid class="h-100">
      <b-row class="mt-5">
        <b-col cols="3" class="mt-5 text-left border-right">
          <b-form class="mb-2">
            <label for="pick-parameter" class="text-left mb-n1">Change Parameter</label>
            <b-form-select id="pick-parameter" v-model="request.selectedDataset" :options="parameterOptions" class="w-100 mb-2"/>
            <label for="pick-station" class="text-left mb-n1">Chnage Station</label>
            <b-form-select id="pick-station" v-model="request.selectedStation" :options="stationOptions" class="w-100 mb-2"/>
            <label for="date" class="mb-n1">Change Timeframe</label>
            <b-input-group class="w-100" id="date">
              <b-form-select v-model="request.startDate" :options="yearOptions" class="" />
              <b-form-select v-model="request.endDate" :options="yearOptionsReverse" class="" />
            </b-input-group>
          </b-form>
          <hr>
          <b-form>
            <label for="pick-wording">Change wording</label>
            <b-form-select id="pick-wording" v-model="request.wording" :options="wordingOptions" class="mb-2" /> <br>
            <label for="starting-date">Add everyday size to compare to</label>
            <b-form-select id="starting-date" v-model="request.compareTo" :options="compareToOptions" class="mb-2" :disabled="request.wording == 'absolute'"/> <br>
            <label for="end-date">Change theme</label>
            <b-form-select id="end-date" v-model="request.theme" :options="themeOptions" class="mb-2" />
          </b-form>
        </b-col>
        <b-col cols="9" class="w-100">
          <argument-card v-if="requestIsValid" :request="request" :meta="datasets[request.selectedDataset]" class="my-5 mx-auto"/>
          <h3 v-else class="text-center rubik-medium y-center">Please fill out fields on the left to see a card.</h3>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
//import html2pdf from 'html2pdf.js'
import ArgumentCard from '../components/ArgumentCard.vue';

export default {
  name: 'Home',
  components: {
    ArgumentCard,

  },
  data() {
    return {
      datasets : {},
      wordingOptions : [
        {value: 'absolute', text: 'Compare absolute values'},
        {value: 'difference', text: 'Show absolute difference'},
        {value: 'relative', text: 'Show difference in percent'},
      ],
      themeOptions : [
        {value: 'classic', text: 'Classic theme'},
        {value: 'drastic', text: 'Typerwriter theme'},
        {value: 'news', text: 'Newspaper theme'},
      ],
      request : {
        selectedParameter : null,
        selectedStation : null,
        startDate : '',
        endDate : '',
        wording : 'difference',
        theme : 'classic',
        compareTo : '',
      },
    }
  },
  methods: {
    fetchDataSets() {
      fetch(`${this.apiURL}datasets/`, {})
      .then((resp) => resp.json())
      .then((data) => {
        this.datasets = data;
      })
      .catch(function(error) {
        console.log(error);
      });
    },
    print() {
      console.log('drucken!')
      let element = this.$refs.argument;
      html2pdf(element);
    }
  },
  computed: {
    requestIsValid() {
      return this.request.selectedDataset != null && this.request.startDate !='' && this.request.endDate !='';
    },
    parameterOptions() {
      var options = [ { value: null, text: 'Select a parameter' }, ];
      for (const [key, entry] of Object.entries(this.datasets)) {
        options.push({value: key, text: entry.name})
      }
      return options;
    },
    stationOptions() {
      var options = [ { value: null, text: 'Select an ICOS station' }, ];
      for (const [key, entry] of Object.entries(this.datasets)) {
        options.push({value: key, text: entry.name})
      }
      return options;
    },
    yearOptions() {
      var options = [ { value: '', text: 'Please select a year' }, ];
      if (this.request.selectedDataset != undefined) {
        var start = this.datasets[this.request.selectedDataset].minYear;
        var end = this.datasets[this.request.selectedDataset].maxYear;
        for (var year = start; year <= end; year++) {
          options.push({ value: year, text: String(year)})
        }
      }
      return options;
    },
    yearOptionsReverse() {
      var options = [ { value: '', text: 'Please select a year' }, ];
      if (this.request.selectedDataset != undefined) {
        var start = this.datasets[this.request.selectedDataset].minYear;
        var end = this.datasets[this.request.selectedDataset].maxYear;
        for (var year = end; year >= start; year--) {
          options.push({ value: year, text: String(year)})
        }
      }
      return options;
    },
    compareToOptions()  {
      var options = [ { value: '', text: 'Please select an everyday size' }, ];
      if (this.request.selectedDataset != undefined) {
        for (const compare of this.datasets[this.request.selectedDataset].compareTo) {
          options.push({ value: compare, text: this.capitFirstChar(compare) });
        }
      }
      return options;
    }
  },
  created() {
    this.fetchDataSets();
  }
}
</script>

<style lang="scss" scoped>
.y-center-help {
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}

.y-center {
  //vertical-align: middle;
  position: relative;
  top: 50%;
  transform: translateY(-50%);  
}

.form {
  background-color: rgb(213, 245, 255);
}

.image-wrapper {
  width: 100%
}

.image {
  object-fit: scale-down;
}
</style>

