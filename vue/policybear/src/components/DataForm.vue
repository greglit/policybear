<template>
    <b-form class="mb-2">
      <label for="pick-parameter" class="text-left mb-n1">{{change ? 'Change' : 'Choose'}} Parameter</label>
      <b-form-select id="pick-parameter" v-model="d_requestData.param" :options="parameterOptions" class="w-100 mb-2"/>
      <label for="pick-station" class="text-left mb-n1">{{change ? 'Change' : 'Choose'}} Station</label>
      <b-form-select id="pick-station" v-model="d_requestData.station" :options="stationOptions" :disabled="!d_requestData.param" class="w-100 mb-2"/>
      <label for="startdate" class="mb-n1">Select first date</label>
      <b-input-group class="w-100" id="date">
        <b-form-select v-model="d_requestData.startDateYear" :options="startDateYearOptions" :disabled="!d_requestData.param || !d_requestData.station" />
        <b-form-select v-model="d_requestData.startDateMonth" :options="startDateMonthOptions" :disabled="!d_requestData.startDateYear" />
      </b-input-group>
      <label for="enddate" class="mb-n1">Select second date</label>
      <b-input-group class="w-100" id="date">
        <b-form-select v-model="d_requestData.endDateYear" :options="endDateYearOptions" :disabled="!d_requestData.startDateYear" />
        <b-form-select v-model="d_requestData.endDateMonth" :options="endDateMonthOptions" :disabled="!d_requestData.endDateYear || !d_requestData.startDateMonth" />
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

      months : [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ],
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
      if (this.d_requestData.param != null && this.meta != null) {
        for (const [key, value] of Object.entries(this.meta[this.d_requestData.param].stations)) {
          options.push({value: value, text: value})
        }
      }
      
      return options;
    },
    startDateYearOptions() {
      var options = [ { value: null, text: 'Year', disabled: true }, ];
      if (this.d_requestData.param != null && this.d_requestData.station != null && this.meta != null) {
        var start = this.meta[this.d_requestData.param].timeStart[this.d_requestData.station][0];
        var end = this.meta[this.d_requestData.param].timeEnd[this.d_requestData.station][0];
        for (var year = start; year <= end; year++) {
          options.push({ value: year, text: String(year)})
        }
      }
      return options;
    },
    startDateMonthOptions() {
      var options = [ { value: null, text: 'Month (optional)', disabled: true }, ];
      if (this.d_requestData.param != null && this.d_requestData.station != null && this.meta != null && this.d_requestData.startDateYear != null) {
        var start = 1;
        var end = 12;
        //if selected year is the earliest year in possible timeframe, then set the earliest month to the one defined in meta
        if (this.d_requestData.startDateYear == this.meta[this.d_requestData.param].timeStart[this.d_requestData.station][0]) {
          start = this.meta[this.d_requestData.param].timeStart[this.d_requestData.station][1];
        }
        //if selected year is the latest year in possible timeframe, then set the latest month to the one defined in meta
        if (this.d_requestData.startDateYear == this.meta[this.d_requestData.param].timeEnd[this.d_requestData.station][0]) {
          end = this.meta[this.d_requestData.param].timeEnd[this.d_requestData.station][1]-1;
        }
        for (var month = start; month <= end; month++) {
          options.push({ value: month, text: this.months[month-1]})
        }
      }
      return options;
    },
    endDateYearOptions() {
      var options = [ { value: null, text: 'Year', disabled: true}, ];
      if (this.d_requestData.param != null && this.d_requestData.station != null && this.meta != null && this.d_requestData.startDateYear != null) {
        var start = this.d_requestData.startDateMonth == 12 ? this.d_requestData.startDateYear+1 : this.d_requestData.startDateYear;
        var end = this.meta[this.d_requestData.param].timeEnd[this.d_requestData.station][0];
        for (var year = end; year >= start; year--) {
          options.push({ value: year, text: String(year)})
        }
      }
      return options;
    },
    endDateMonthOptions() {
      //const monthText = this.d_requestData.startDateMonth ? 'Month' : 'Month (optional)';
      var options = [ { value: null, text: 'Month', disabled: true }, ];
      if (this.d_requestData.param && this.d_requestData.station && this.meta && this.d_requestData.endDateYear && this.d_requestData.startDateMonth) {
        var start = 1;
        var end = 12;
        //if selected year is the earliest year in possible timeframe, then set the earliest month to the one defined in meta
        if (this.d_requestData.endDateYear == this.meta[this.d_requestData.param].timeStart[this.d_requestData.station][0]) {
          start = this.meta[this.d_requestData.param].timeStart[this.d_requestData.station][1];
        }
        //if selected year is the latest year in possible timeframe, then set the latest month to the one defined in meta
        if (this.d_requestData.endDateYear == this.meta[this.d_requestData.param].timeEnd[this.d_requestData.station][0]) {
          end = this.meta[this.d_requestData.param].timeEnd[this.d_requestData.station][1];
        }

        //if selected year is same as starDate selected year then the earliest possible month is the month after the month selected for beginning of timeframe
        if (this.d_requestData.endDateYear == this.d_requestData.startDateYear) {
          start = this.d_requestData.startDateMonth + 1;
        }
        for (var month = start; month <= end; month++) {
          options.push({ value: month, text: this.months[month-1]})
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
