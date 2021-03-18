<template>
  <div class="h-100">
    <b-container class="h-100">
      <b-row class="h-100">
        <b-col cols="12" md="6">
            <img src="../assets/polarbear-transparent.png" alt="policy bear" class="w-75 y-center"/>
        </b-col>
        <b-col cols="12" md="6">
          <h1 class="display-5 text-left rubik-bold my-md-5">"Hi, I'm Policy Bear!</h1>
          <h1 class="text-left ">Let's start creating simple arguments from complex data."</h1>
          <!--<b-icon-arrow-down-circle-fill animation="cylon-vertical" font-scale="4" style=""/>-->
          <b-card class="shadow m-3 mt-5 border-0">
            <b-form inline>
              <label for="pick-dataset" class="text-left">Compare data</label>
              <b-form-select id="pick-dataset" v-model="request.selectedDataset" :options="datasetsOptions" class="mb-2" />
              <label for="pick-dataset" class="text-left">Select a ICOS station</label>
              <b-form-select id="pick-dataset" v-model="request.selectedDataset" :options="datasetsOptions" class="mb-2" />
              <label for="starting-date">Timeframe start</label>
              <b-form-select id="starting-date" v-model="request.startDate" :options="yearOptions" class="mb-2" />
              <label for="end-date">Timeframe end</label>
              <b-form-select id="end-date" v-model="request.endDate" :options="yearOptionsReverse" class="mb-2" />
            </b-form>
          </b-card>
        </b-col>
      </b-row>

      <b-card class="w-100 mt-5 shadow">
        <b-row>
          <b-col cols="6" class="text-left">
            
          </b-col>
          <b-col cols="6" class="border-left text-left">
            <b-form>
              <label for="pick-wording">Choose wording</label>
              <b-form-select id="pick-wording" v-model="request.wording" :options="wordingOptions" class="mb-2" /> <br>
              <label for="starting-date">Choose everyday size to compare to</label>
              <b-form-select id="starting-date" v-model="request.compareTo" :options="compareToOptions" class="mb-2" :disabled="request.wording == 'absolute'"/> <br>
              <label for="end-date">Choose theme</label>
              <b-form-select id="end-date" v-model="request.theme" :options="themeOptions" class="mb-2" />
            </b-form>
          </b-col>
        </b-row>
      </b-card>
      <div ref="argument" style="margin-bottom: 200px; margin-top: 100px">
        <b-row>
          <argument-card v-if="requestIsValid" :request="request" :meta="datasets[request.selectedDataset]" class="my-5"/>
        </b-row>
      </div>
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
        selectedDataset : null,
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
    datasetsOptions() {
      var options = [ { value: null, text: 'Please select a dataset' }, ];
      for (const [key, entry] of Object.entries(this.datasets)) {
        options.push({value: key, text: entry.description})
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
      var options = [ { value: '', text: 'Please select a everyday size' }, ];
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

