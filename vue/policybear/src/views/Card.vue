<template>
  <div class="m-5" style="height: 80vh">
    <argument-card v-if="datasets && request" :request="request" :meta="datasets[request.data.param]" class="m-5 mx-auto" light="true"/>
  </div>
</template>

<script>
import ArgumentCard from '../components/ArgumentCard.vue';

export default {
  name: 'Card',
  components: {
    ArgumentCard,
  },
  data() {
    return {
      datasets : null,
      request : null,
    }
  },
  methods: {
    fetchDataSets() {
      console.log(`${this.apiURL}datasets/`);
      fetch(`${this.apiURL}datasets/`, {})
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data);
        this.datasets = data;
      })
      .catch((error) => {
        console.log(error);
        this.fetchDataSets();
      });
    },
  },
  computed: {    
  },
  created() {
    this.fetchDataSets();
    this.request = JSON.parse(this.$route.params.request)
  }
}
</script>

<style lang="scss" scoped>

</style>

