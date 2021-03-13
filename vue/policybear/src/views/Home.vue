<template>
  <div>
    <input v-model="date" />
    <button @click="fetchData">fetch</button>
    {{response}}
  </div>
</template>

<script>


export default {
  name: 'Home',
  components: {
    
  },
  data() {
    return {
      response : '',
      date : '',
    }
  },
  methods: {
    async fetchData() {
      fetch( "/api/", { //`http://greglit.pythonanywhere.com/`,{ //`http://192.168.178.25:5000/?penis=${this.date}&`, {
      })
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data)
        this.response = data;
      })
      .catch(function(error) {
        console.log(error);
      });
    },
  }
}
</script>
