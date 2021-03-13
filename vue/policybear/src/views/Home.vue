<template>
  <div>
    <b-container>
      <b-row>
        <h1 class="display 3">Hi, I'm Policy Bear! Let's start creating simple arguments from complex data.</h1>
      </b-row>
      <b-card class="w-100 mt-5">
        <b-row>
          <b-col cols="6">
            <b-form>
              <label for="pick-dataset">Compare data of</label>
              <b-form-select id="pick-dataset" v-model="request.selectedDataset" :options="datasetsOptions" class="mb-2" /> <br>
              <label for="starting-date">at the time</label>
              <b-form-select id="starting-date" v-model="request.startDate" :options="yearOptions" class="mb-2" /> <br>
              <label for="end-date">to data at the time</label>
              <b-form-select id="end-date" v-model="request.endDate" :options="yearOptions" class="mb-2" />
            </b-form>
          </b-col>
          <b-col cols="6" class="border-left">
            <b-form>
              <label for="pick-wording">Choose wording</label>
              <b-form-select id="pick-wording" v-model="request.wording" :options="wordingOptions" class="mb-2" /> <br>
              <label for="starting-date">Choose everyday size to compare to</label>
              <b-form-select id="starting-date" v-model="request.compareTo" :options="compareToOptions" class="mb-2" /> <br>
              <label for="end-date">Choose theme</label>
              <b-form-select id="end-date" v-model="request.theme" :options="themeOptions" class="mb-2" />
            </b-form>
          </b-col>
        </b-row>
      </b-card>
      {{response}}
      <b-row>
          <argument-card v-if="requestIsValid" :request="request" :meta="datasets[request.selectedDataset]"/>
      </b-row>
    </b-container>
  </div>
</template>

<script>

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
        {value: 'difference', text: 'Show absolute differnce'},
        {value: 'relative', text: 'Show differnece in percent'},
      ],
      themeOptions : [
        {value: 'classic', text: 'Classic theme'},
        {value: 'modern', text: 'Modern theme'},
        {value: 'newspaper', text: 'Newspaper theme'},
      ],
      request : {
        selectedDataset : null,
        startDate : '',
        endDate : '',
        wording : 'difference',
        theme : 'classic',
        compareTo : '',
      },
      response : '',
    }
  },
  methods: {
    fetchDataSets() {
      fetch(`${this.apiURL}/datasets/`, {})
      .then((resp) => resp.json())
      .then((data) => {
        this.datasets = data;
      })
      .catch(function(error) {
        console.log(error);
      });
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
    compareToOptions()  {
      var options = [ { value: '', text: 'Please select a everyday size' }, ];
      if (this.request.selectedDataset != undefined) {
        options.push(this.datasets[this.request.selectedDataset].compareTo);
        var compareTo = [
          { value: 'cows', text: 'Cows' },
        ]
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

