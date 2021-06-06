<template>
    <b-form class="mb-2">
      <label for="pick-parameter" class="text-left mb-n1">Parameter</label>
      <b-form-select id="pick-parameter" v-model="d_requestData.param" :options="parameterOptions" class="w-100"/>
      <div class="mb-3">
        <label for="pick-station" class="text-left mb-n1">Station</label>
        <b-input-group class="w-100 mb-1" id="pick-station">
          <b-input-group-prepend>
            <b-button variant="info" :disabled="!d_requestData.param" @click="showMap = !showMap">
              <b-icon-map-fill/>
            </b-button>
          </b-input-group-prepend>
          <b-form-select v-model="d_requestData.station" :options="stationOptions" :disabled="!d_requestData.param"/>
        </b-input-group>
        <leaflet-map 
          class="my-2 p-0 rounded " style="overflow:hidden"
          v-if="meta != null && showMap" 
          :selectStation="(key) => {d_requestData.param = 'ch4'; d_requestData.station = key}"
        />
      </div>

      <b-form-radio-group
          v-model="d_requestData.dateFormat" :options="dateFormatOptions" :disabled="!d_requestData.station"
          button-variant="outline-primary" buttons class="w-100 my-2" @click="resetDate()"
      ></b-form-radio-group>
      <transition name="fade" mode="out-in">
        <div v-if="d_requestData.dateFormat=='annual'" :key="d_requestData.dateFormat">
          <label for="startdate" class="mb-n1">First year</label>
          <b-form-select id="startdate" class="w-100" v-model="d_requestData.startDateYear" :options="startDateYearOptions" :disabled="!d_requestData.param || !d_requestData.station" />
          <label for="enddate" class="mb-n1">Second year</label>
          <b-form-select id="enddate" class="w-100" v-model="d_requestData.endDateYear" :options="endDateYearOptions" :disabled="!d_requestData.startDateYear" />
        </div>
        <div v-else-if="d_requestData.dateFormat=='monthly'" :key="d_requestData.dateFormat">
          <label for="startdate" class="mb-n1">First date</label>
          <b-input-group class="w-100" id="startdate">
            <b-form-select v-model="d_requestData.startDateYear" :options="startDateYearOptions" :disabled="!d_requestData.param || !d_requestData.station" />
            <b-form-select v-model="d_requestData.startDateMonth" :options="startDateMonthOptions" :disabled="!d_requestData.startDateYear" />
          </b-input-group>
          <label for="enddate" class="mb-n1">Second date</label>
          <b-input-group class="w-100" id="enddate">
            <b-form-select v-model="d_requestData.endDateYear" :options="endDateYearOptions" :disabled="!d_requestData.startDateYear" />
            <b-form-select v-model="d_requestData.endDateMonth" :options="endDateMonthOptions" :disabled="!d_requestData.endDateYear || !d_requestData.startDateMonth" />
          </b-input-group>
        </div>
      </transition>
    </b-form>
</template>

<script>
import store from '../store.js'
import LeafletMap from './LeafletMap.vue';

export default {
  name: 'DataForm',
  components: {
    LeafletMap,
  },
  props: {
    change: Boolean
  },
  data() {
    return {
      d_requestData : store.cardRequest.data,
      meta: null,
      showMap: false,
      dateFormatOptions: [
        { value: 'annual', text: 'Annual values' },
        { value: 'monthly', text: 'Monthly values'},
      ],

      showMap: false,
    }
  },
  watch: {
    d_requestData: {
     handler(newVal){
      if (this.d_requestData.dateFormat == 'annual') {
        this.d_requestData.startDateMonth = null;
        this.d_requestData.endDateMonth = null;
      }
     },
     deep: true
  	},
  },
  computed: {
    parameterOptions() {
      var options = [ { value: null, text: 'Select a parameter', disabled: true }, ];
      if (this.meta != null) {
        for (const [key, entry] of Object.entries(this.meta)) {
          options.push({value: key, text: entry.param_specs.param_name})
        }
      }
      return options;
    },
    stationOptions() {
      var options = [ { value: null, text: 'Select an ICOS station', disabled: true }, ];
      if (this.d_requestData.param != null && this.meta != null) {
        for (const [key, station] of Object.entries(this.meta[this.d_requestData.param].param_stations)) {
          options.push({value: key, text: `${station.station_name} (${station.station_country})`})
        }
      }
      
      return options;
    },
    startDateYearOptions() {
      var options = [ { value: null, text: 'Year', disabled: true }, ];
      if (this.d_requestData.param != null && this.d_requestData.station != null && this.meta != null) {
        var start = this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[0][0];
        var end = this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[1][0];
        for (var year = start; year <= end; year++) {
          options.push({ value: year, text: String(year)})
        }
      }
      return options;
    },
    startDateMonthOptions() {
      var options = [ { value: null, text: 'Month', disabled: true}, ];
      if (this.d_requestData.param != null && this.d_requestData.station != null && this.meta != null && this.d_requestData.startDateYear != null) {
        var start = 1;
        var end = 12;
        //if selected year is the earliest year in possible timeframe, then set the earliest month to the one defined in meta
        if (this.d_requestData.startDateYear == this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[0][0]) {
          start = this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[0][1];
        }
        //if selected year is the latest year in possible timeframe, then set the latest month to the one defined in meta
        if (this.d_requestData.startDateYear == this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[1][0]) {
          end = this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[1][1]-1;
        }
        for (var month = start; month <= end; month++) {
          options.push({ value: month, text: this.month(month-1)})
        }
      }
      return options;
    },
    endDateYearOptions() {
      var options = [ { value: null, text: 'Year', disabled: true}, ];
      if (this.d_requestData.param != null && this.d_requestData.station != null && this.meta != null && this.d_requestData.startDateYear != null) {
        var start = this.d_requestData.startDateMonth == 12 ? this.d_requestData.startDateYear+1 : this.d_requestData.startDateYear;
        var end = this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[1][0];
        for (var year = end; year >= start; year--) {
          options.push({ value: year, text: String(year)})
        }
      }
      return options;
    },
    endDateMonthOptions() {
      var options = [ { value: null, text: 'Month', disabled:true}, ];
      if (this.d_requestData.param && this.d_requestData.station && this.meta && this.d_requestData.endDateYear && this.d_requestData.startDateMonth) {
        var start = 1;
        var end = 12;
        //if selected year is the earliest year in possible timeframe, then set the earliest month to the one defined in meta
        if (this.d_requestData.endDateYear == this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[0][0]) {
          start = this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[0][1];
        }
        //if selected year is the latest year in possible timeframe, then set the latest month to the one defined in meta
        if (this.d_requestData.endDateYear == this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[1][0]) {
          end = this.meta[this.d_requestData.param].param_stations[this.d_requestData.station].station_time_period[1][1];
        }

        //if selected year is same as starDate selected year then the earliest possible month is the month after the month selected for beginning of timeframe
        if (this.d_requestData.endDateYear == this.d_requestData.startDateYear) {
          start = this.d_requestData.startDateMonth + 1;
        }
        for (var month = start; month <= end; month++) {
          options.push({ value: month, text: this.month(month-1)})
        }
      }
      return options;
    },
  },
  async created() {
    this.meta = await store.datasets();
  },
}
</script>

<style lang="scss" scoped>
  .fade-enter-active {
    transition: opacity .5s;
  }
  .fade-leave-active {
    transition: opacity .1s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
</style>
