<template>
	<div style="width: 100%">
		<div :class="'card shadow border-0 mx-auto text-left ' + request.theme" >
			<div v-if="responseData != undefined">
				The {{meta.name}} concentration in the arctic
				<div v-if="request.wording == 'difference'">
					{{responseData.change > 0 ? 'increased' : 'decreased'}} by <b>{{responseData.change}} ppm</b> 
					between {{responseData.begin_period}} and {{responseData.end_period}}.
				</div>
				<div v-else-if="request.wording == 'relative'">
					{{responseData.change > 0 ? 'increased' : 'decreased'}} by 
					<b>{{((1-(responseData.begin_data/responseData.end_data))*100).toFixed(2)}} %</b> 
					between {{responseData.begin_period}} and {{responseData.end_period}}.
				</div>
				<div v-else-if="request.wording == 'absolute'">
					was <b>{{responseData.begin_data}} ppm</b> in {{responseData.begin_period}} and <b>{{responseData.end_data}} ppm</b> in {{responseData.end_period}}.
				</div>

				<div v-if="request.compareTo != '' && responseData.comp_amount != undefined">
					This is equivalent to the annually emission of <b>{{responseData.comp_amount}}</b> {{request.compareTo}}.
				</div>
			</div>
			<div v-else>
				<h1>loading...</h1>
			</div>
		</div>
		<p>Created with <img src="../../public/policybear_logo.png" alt="logo" style="width:20px;height:20px; margin-top:-3px" class="mx-1"/> Policy Bear to save the arctic. Raahhhrr! 🌏</p>
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
			var query = `${this.apiURL}datapoints/?dataset=${this.request.selectedDataset}&startdate=${this.request.startDate}&enddate=${this.request.endDate}`;
			if (this.request.compareTo  != '') {
				query += `&compareTo=${this.request.compareTo}`;
			}
			console.log(query)
      fetch(query, {})
      .then((resp) => resp.json())
      .then((data) => {
				console.log(data)
        this.responseData =  data;
      })
      .catch(function(error) {
        console.log('Error: ' + error);
				return null;
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
	font-size: 40pt;
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
