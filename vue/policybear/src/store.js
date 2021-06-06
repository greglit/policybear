import Vue from 'vue';

const state = Vue.observable({
  init() {
    fetchDatasets();
  },
  datasets: null,
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
});

const fetchDatasets = async () => {
  console.log(`${apiURL()}datasets/`);
  const response = await fetch(`${apiURL()}datasets/`, {})
  if (!response.ok) {
    console.log(error);
    setTimeout(()=>{
      this.fetchDataSets();
    }, 5000)
  } else {
    const data = await response.json();
    console.log(data);
    //console.log('store datasets', this.datasets)
    state.datasets = data;
    return data
  }
}

export const apiURL = () => {
  const url = String(window.location)
    if (Vue.config.devtools || url.includes('dev')) {
      //return 'http://192.168.178.22:5000/';//'https://policybear.herokuapp.com/';//'http://192.168.178.25:5000/'
      return 'https://dev-policybear.herokuapp.com/';
    } else {
      return 'https://policybear.herokuapp.com/';
    }
}

export default state;