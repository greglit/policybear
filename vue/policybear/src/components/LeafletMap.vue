 <template>
  <div style="height: 500px; width: 100%;">
    <l-map
      v-if="meta && param"
      :zoom="meta[param].map_opts.map_zoom"
      :center="[meta[param].map_opts.map_centroid_latlon[0], meta[param].map_opts.map_centroid_latlon[1]]"
      :options="mapOptions"
      style="height: 100%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker v-for="(station, key) in this.meta[param].param_stations" :lat-lng="[station.station_latlon[0], station.station_latlon[1]]" :key="key" @click="selectStation(key)">
        <l-tooltip :options="{ permanent: false, interactive: false }">
          {{station.station_name}} ({{station.station_country}})<br/>
          {{month(station.station_time_period[0][1])}} {{station.station_time_period[0][0]}} - {{month(station.station_time_period[1][1])}} {{station.station_time_period[1][0]}}
        </l-tooltip>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import store from '../store.js'

import { LMap, LTileLayer, LMarker, LPopup, LTooltip } from "vue2-leaflet";

import { Icon } from 'leaflet';

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});


export default {
  name: "LeafletMap",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip
  },
  props: {
    selectStation : Function,
  },
  data() {
    return {
      param: store.cardRequest.data.param,
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    
      mapOptions: {
        zoomSnap: 0.5
      },
      showMap: true,
    };
  },
  computed: {
    meta() {
      return store.datasets;
    }
  },
  methods: {
    zoomUpdate(zoom) {
      this.zoom = zoom;
    },
    centerUpdate(center) {
      this.center = center;
    },
    innerClick() {
      alert("Click!");
    },
    clickedMarker(key) {
      console.log(`clicked station: ${this.stationNames[key]}`)
    },
  },
};
</script>