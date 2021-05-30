<template>
	<div ref="argument" style="width:100%">
    <div class="aspect-ratio-box mx-auto">
      <div :class="'aspect-ratio-box-inside card border-0 shadow text-left ' + request.styling.theme" ref="innerCard" :style="cardStyling">
        <resize-observer @notify="handleResize" />
        <div v-if="responseData != undefined">
          The {{meta.name}} concentration at the ICOS station "{{meta.stations_name[responseData.station]}}"
          <div v-if="request.styling.wording == 'difference'">
            {{responseData.change > 0 ? 'increased' : 'decreased'}} by <b>{{responseData.change}} {{responseData.unit}}</b> 
            between {{responseData.begin_period}} and {{responseData.end_period}}.
          </div>
          <div v-else-if="request.styling.wording == 'relative'">
            {{responseData.change > 0 ? 'increased' : 'decreased'}} by 
            <b>{{Math.abs(responseData.change_pct)}} %</b> 
            between {{responseData.begin_period}} and {{responseData.end_period}}.
          </div>
          <div v-else-if="request.styling.wording == 'absolute'">
            was <b>{{responseData.start_abs_value}} {{responseData.unit}}</b> in {{responseData.begin_period}} and <b>{{responseData.end_abs_value}} {{responseData.unit}}</b> in {{responseData.end_period}}.
          </div>

          <div v-if="request.styling.convertTo != '' && responseData.compare_amount != undefined && request.styling.wording != 'absolute'">
            This is equivalent to the annual emission of <b>{{withPoints(responseData.compare_amount)}}</b> {{request.styling.convertTo}}.
          </div>
        </div>
        <div v-else>
          <h1>loading...</h1>
        </div>
      </div>
    </div>
		<p :class="[!light ? 'txt-nord6' : '', 'text-footer text-center mt-3']">Created with <img src="../../public/policybear_icon.png" alt="logo" style="width:20px; height:20px; margin-top:-3px" class="mx-1"/> Policy Bear to save the arctic. Raahhhrr!</p>
	</div>
</template>

<script>


export default {
  name: 'ArgumentCard',
  components: {
    
  },
  props: ['request','meta', 'light'],
  data() {
    return {
			responseData : undefined,
      cardFontSize: 0,
    }
  },
  methods: {
		fetchData() {
			var startDate = this.request.data.startDateYear + (this.request.data.startDateMonth ? '-'+this.request.data.startDateMonth : '');
			var endDate = this.request.data.endDateYear + (this.request.data.endDateMonth ? '-'+this.request.data.endDateMonth : '');
			var convertTo = this.request.styling.convertTo ? `&compareTo=${this.request.styling.convertTo}` : '';
			var query = `${this.apiURL}datapoints/?param=${this.request.data.param}&station=${this.request.data.station}&startdate=${startDate}&enddate=${endDate}${convertTo}`;
			console.log(query)
      fetch(query, {})
      .then((resp) => resp.json())
      .then((data) => {
				console.log(data)
        this.responseData =  data;
      })
      .catch(function(error) {
        console.log('Error: ' + error);
      });
    },
    handleResize(e) {
      if (this.$refs.innerCard != undefined) {
        const cardWidth = this.$refs.innerCard.clientWidth;
        //console.log('width',this.$refs.innerCard.clientWidth);
        this.cardFontSize = cardWidth*0.04
        //console.log('fontSize',this.cardFontSize);
      }
    },
    
  },
  computed: {
    cardStyling() {
      let style = '';
      style = this.request.styling.theme != 'drastic' ? `font-size:${this.cardFontSize}pt;` : `font-size:${this.cardFontSize*0.9}pt;`
      style += ` padding:${this.cardFontSize}px;`
      console.log(style);
      return style;
    }
  },
  watch: {
    request: {
     handler(val){
       this.fetchData();
     },
     deep: true
  	}
  },
  created() {
		this.fetchData();
	},
  mounted() {
    this.handleResize()
  },
}
</script>

<style lang="scss" scoped>
.card {
	color: white;
	padding: 3vw;
	border-radius: 0px;
	max-width: 900px;
}

.card-footer {
  font-size: 1vw;
}

.classic {
	background-color: rgb(255, 73, 73);
}

.drastic {
	background-color: rgb(37, 37, 37);
	color: rgb(255, 255, 255);
	font-family: 'Courier New', Courier, monospace;
}

.news {
	background-color: rgb(255, 246, 230);
	color: black;
	font-family: 'Times New Roman', Times, serif;
}

.image-wrapper {
  width: 100%
}

.image {
  object-fit: scale-down;
}

.aspect-ratio-box {
  margin-top: -50px;
  height: 0;
  overflow: hidden;
  padding-top: 60%;
  background: none;
  position: relative;
}
.aspect-ratio-box-inside {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
