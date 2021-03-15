<template>
  <div>
    <b-row>
      <h1 class="display-3 text-center" style="position:absolute; width:70%; top:30px; left:15%;">"Hi, I'm Policy Bear! Let's start creating simple arguments from complex data."</h1>
      <img src="../assets/policy_bear.jpg" alt="policy bear" style="height:100%; width:100%;"/>
      <b-icon-arrow-down-circle-fill animation="cylon-vertical" font-scale="4" style="position:absolute; right:25%; top:450px"/>
    </b-row>
    <b-container style="margin-top: -400px">
      <b-card class="w-100 mt-5 shadow">
        <b-row>
          <b-col cols="6" class="text-left">
            <b-form>
              <label for="pick-dataset" class="text-left">Compare data of</label>
              <b-form-select id="pick-dataset" v-model="request.selectedDataset" :options="datasetsOptions" class="mb-2" /> <br>
              <label for="starting-date">between year</label>
              <b-form-select id="starting-date" v-model="request.startDate" :options="yearOptions" class="mb-2" /> <br>
              <label for="end-date">and year</label>
              <b-form-select id="end-date" v-model="request.endDate" :options="yearOptionsReverse" class="mb-2" />
            </b-form>
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
      <!--<b-button v-if="requestIsValid" class="mt-5" variant="outline-primary" @click="print()">
        <b-icon-printer class="mr-2"/>Print
      </b-button>-->
      <div ref="argument" style="margin-bottom: 200px; margin-top: 100px">
        <b-row>
          <argument-card v-if="requestIsValid" :request="request" :meta="datasets[request.selectedDataset]" class="my-5"/>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
import html2pdf from 'html2pdf.js'
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

