<template>
  <b-card class="border-0 card text-center m-4 p-4">
    <img :src="imageSrc" class="img"/>
    <h3>{{firstName}}<br/>{{lastName}}</h3>
    <p v-if="description">{{description}}</p>
    <h5 v-if="street">{{street}} {{number}}<br/>{{zipCode}} {{city}}</h5>
    <h5 v-if="email">{{email}}</h5>
    <h5>
      <a v-if="github != ''" :href="github" class="m-2"><b-icon-github/></a>
      <a v-if="homepage" :href="homepage" class="m-2"><b-icon-globe/></a>
    </h5>
  </b-card>
</template>

<script>

export default {
  name: 'ContactCard',
  components: {
  },
  props: {
    imageSrc: String,
    firstName: String,
    lastName: String,
    description: String,
    street: String,
    number: String,
    zipCode: String,
    city: String,
    email: String,
    github: String,
    homepage: String,
  },
  data() {
    return {
      
    }
  },
  computed: {
    
  },
  methods: {
    
  },
  watch: {
    
  },
}
</script>

<style lang="scss" scoped>
@import "../../node_modules/nord/src/sass/nord.scss";

  .card {
    max-width: 500px;
    min-width: 200px;
    background-color: $nord3;
    color: $nord5;
    border-radius: 10px;
  }

  a {
    color: $nord5;
  }

  .img {
    border-radius: 50%;
    width: 200px;
    height: 200px;
  }
</style>
