<template>
	<div style="width: 100%">
		<div :class="'card shadow border-0 mx-auto text-left ' + request.styling.theme" >
			<div v-if="responseData != undefined">
				The {{meta.name}} concentration at the ICOS station {{responseData.station}}
				<div v-if="request.styling.wording == 'difference'">
					{{responseData.change > 0 ? 'increased' : 'decreased'}} by <b>{{responseData.change}} {{responseData.unit}}</b> 
					between {{responseData.begin_period}} and {{responseData.end_period}}.
				</div>
				<div v-else-if="request.styling.wording == 'relative'">
					{{responseData.change > 0 ? 'increased' : 'decreased'}} by 
					<b>{{((1-(responseData.start_abs_value/responseData.end_abs_value))*100).toFixed(2)}} %</b> 
					between {{responseData.begin_period}} and {{responseData.end_period}}.
				</div>
				<div v-else-if="request.styling.wording == 'absolute'">
					was <b>{{responseData.start_abs_value}} {{responseData.unit}}</b> in {{responseData.begin_period}} and <b>{{responseData.end_abs_value}} {{responseData.unit}}</b> in {{responseData.end_period}}.
				</div>

				<div v-if="request.styling.convertTo != '' && responseData.compare_amount != undefined && request.styling.wording != 'absolute'">
					This is equivalent to the annual emission of <b>{{responseData.compare_amount}}</b> {{request.styling.convertTo}}.
				</div>
			</div>
			<div v-else>
				<h1>loading...</h1>
			</div>
		</div>
		<p>Created with <img src="../../public/policybear_logo.png" alt="logo" style="width:20px;height:20px; margin-top:-3px" class="mx-1"/> Policy Bear to save the arctic. Raahhhrr! ❤</p>
	</div>
</template>

<script>


export default {
  name: 'ArgumentCard',
  components: {
    
  },
  props: ['request','meta'],
  data() {
    return {
			responseData : undefined,
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
}
</script>

<style lang="scss" scoped>
.card {
	color: white;
	padding: 40px;
	margin: 20px;
	border-radius: 0px;
	max-width: 900px;
	font-size: 3vw;
}

@media (max-width: 992px) {
    .card {
		font-size: 5vw !important;
	}
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
</style>
