<template>
	<div>
		<div class="card red shadow">
			<h1 class="display-4" v-if="responseData != undefined">
				The {{meta.name}} concentration did change by {{responseData.change}} ppm from {{responseData.begin_period}} to {{responseData.end_period}}.
			</h1>
		</div>
		<p>{{'Created with Policy Bear to save the arctic. Raahhhrr! 🌏'}}</p>
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
}

.red {
	background-color: rgb(255, 73, 73);
}

.image-wrapper {
  width: 100%
}

.image {
  object-fit: scale-down;
}
</style>
