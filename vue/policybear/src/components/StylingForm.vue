<template>
    <b-form>
      <label for="pick-wording">Change wording</label>
      <b-form-select id="pick-wording" v-model="d_requestStyling.wording" :options="wordingOptions" class="mb-2" /> <br>
      <label for="starting-date">Add everyday size to compare to</label>
      <b-form-select id="starting-date" v-model="d_requestStyling.compareTo" :options="compareToOptions" class="mb-2" :disabled="d_requestStyling.wording == 'absolute'"/> <br>
      <label for="end-date">Change theme</label>
      <b-form-select id="end-date" v-model="d_requestStyling.theme" :options="themeOptions" class="mb-2" />
    </b-form>
</template>

<script>

export default {
  name: 'StylingForm',
  components: {
  },
  props: ['requestStyling', 'requestData', 'meta'],
  data() {
    return {
      d_requestStyling : this.requestStyling,

      wordingOptions : [
        {value: 'absolute', text: 'Compare absolute values'},
        {value: 'difference', text: 'Show absolute difference'},
        {value: 'relative', text: 'Show difference in percent'},
      ],
      themeOptions : [
        {value: 'classic', text: 'Classic theme'},
        {value: 'drastic', text: 'Typerwriter theme'},
        {value: 'news', text: 'Newspaper theme'},
      ],
    }
  },
  watch: {
    d_requestStyling: {
     handler(val){
       this.$emit('update:requestStyling', this.d_requestStyling);
     },
     deep: true
  	}
  },
  computed: {
    compareToOptions()  {
      var options = [ { value: null, text: 'Select an everyday size', disabled: true }, ];
      if (this.requestData.selectedParameter != null && this.meta != null) {
        for (const compare of this.meta[this.requestData.selectedParameter].compareTo) {
          options.push({ value: compare, text: this.capitFirstChar(compare) });
        }
      }
      return options;
    },
  },
  methods: {
    
  },
}
</script>

<style lang="scss" scoped>

</style>
