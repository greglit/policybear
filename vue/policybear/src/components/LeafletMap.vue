 <template>
  <div style="height: 500px; width: 100%;">
    <l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 100%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker v-for="(coords, key) in stationCoords" :lat-lng="latLong(coords[0], coords[1])" :key="key" @click="selectStation(key)">
        <l-tooltip :options="{ permanent: false, interactive: false }">
          {{stationNames[key]}}
        </l-tooltip>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup, LTooltip } from "vue2-leaflet";

import { Icon } from 'leaflet';

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});


export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip
  },
  props: ['stationCoords', 'stationNames', 'selectStation'],
  data() {
    return {
      zoom: 13,
      center: latLng(48.137154, 11.576124),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    
      mapOptions: {
        zoomSnap: 0.5
      },
      showMap: true,
    };
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
    latLong(lat, long) {
      return latLng(lat,long);
    },
    clickedMarker(key) {
      console.log(`clicked station: ${this.stationNames[key]}`)
    },
  },
};
</script>