<template>
    <b-form class="mb-2">
      <label for="pick-parameter" class="text-left mb-n1">{{change ? 'Change' : 'Choose'}} Parameter</label>
      <b-form-select id="pick-parameter" v-model="d_requestData.selectedParameter" :options="parameterOptions" class="w-100 mb-2"/>
      <label for="pick-station" class="text-left mb-n1">{{change ? 'Change' : 'Choose'}} Station</label>
      <b-form-select id="pick-station" v-model="d_requestData.selectedStation" :options="stationOptions" :disabled="!d_requestData.selectedParameter" class="w-100 mb-2"/>
      <label for="date" class="mb-n1">Select Timeframe</label>
      <b-input-group class="w-100" id="date">
        <b-form-select v-model="d_requestData.timeStart" :options="timeStartOptions" :disabled="!d_requestData.selectedParameter || !d_requestData.selectedStation" />
        <b-form-select v-model="d_requestData.timeEnd" :options="timeEndOptions" :disabled="!d_requestData.timeStart" />
      </b-input-group>
    </b-form>
</template>

<script>

export default {
  name: 'DataForm',
  components: {
  },
  props: ['requestData', 'meta', 'change'],
  data() {
    return {
      d_requestData : this.requestData,
    }
  },
  watch: {
    d_requestData: {
     handler(val){
       this.$emit('update:requestData', this.d_requestData);
     },
     deep: true
  	}
  },
  computed: {
    parameterOptions() {
      var options = [ { value: null, text: 'Select a parameter', disabled: true }, ];
      if (this.meta != null) {
        for (const [key, entry] of Object.entries(this.meta)) {
          options.push({value: key, text: entry.name})
        }
      }
      return options;
    },
    stationOptions() {
      var options = [ { value: null, text: 'Select an ICOS station', disabled: true }, ];
      if (this.d_requestData.selectedParameter != null && this.meta != null) {
        for (const [key, value] of Object.entries(this.meta[this.d_requestData.selectedParameter].stations)) {
          options.push({value: value, text: value})
        }
      }
      
      return options;
    },
    timeStartOptions() {
      var options = [ { value: null, text: 'Start year', disabled: true }, ];
      if (this.d_requestData.selectedParameter != null && this.d_requestData.selectedStation != null && this.meta != null) {
        var start = this.meta[this.d_requestData.selectedParameter].timeStart[this.d_requestData.selectedStation][0];
        var end = this.meta[this.d_requestData.selectedParameter].timeEnd[this.d_requestData.selectedStation][0];
        for (var year = start; year <= end; year++) {
          options.push({ value: year, text: String(year)})
        }
      }
      return options;
    },
    timeEndOptions() {
      var options = [ { value: null, text: 'End year', disabled: true}, ];
      if (this.d_requestData.selectedParameter != null && this.d_requestData.selectedStation != null && this.meta != null && this.d_requestData.timeStart != null) {
        var start = this.d_requestData.timeStart + 1;
        var end = this.meta[this.d_requestData.selectedParameter].timeEnd[this.d_requestData.selectedStation][0];
        for (var year = end; year >= start; year--) {
          options.push({ value: year, text: String(year)})
        }
      }
      return options;
    },
  },
  methods: {
    
  },
}
</script>

<style lang="scss" scoped>

</style>
