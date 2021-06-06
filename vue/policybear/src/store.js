import Vue from 'vue';

var private_datasets = null;

function private_apiURL() {
  const url = String(window.location)
    if (Vue.config.devtools || url.includes('dev')) {
      //return 'http://192.168.178.22:5000/';//'https://policybear.herokuapp.com/';//'http://192.168.178.25:5000/'
      return 'https://dev-policybear.herokuapp.com/';
    } else {
      return 'https://policybear.herokuapp.com/';
    }
}

export default Vue.observable({
  cardRequest: {
    data : {
      param : null,
      station : null,
      startDateYear : null,
      startDateMonth: null,
      endDateYear : null,
      endDateMonth : null,
      dateFormat : 'annual',
    },
    styling : {
      wording : 'difference',
      theme : 'classic',
      compareTo : null,
    }
  },
  async datasets() {
    if (private_datasets) {
      return private_datasets
    } else {
      return await this.fetchDatasets();
    }
  },
  async fetchDatasets() {
    console.log(`${private_apiURL()}datasets/`);
    const response = await fetch(`${private_apiURL()}datasets/`, {})

    if (!response.ok) {
      console.log(error);
      setTimeout(()=>{
        this.fetchDataSets();
      }, 5000)
    } else {
      const data = await response.json()
      console.log(data);
      private_datasets = data;
      return data
    }
  },
  apiURL() {
    return private_apiURL();
  },
});