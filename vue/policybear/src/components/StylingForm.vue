<template>
    <b-form>
      <label for="pick-wording">Text content</label>
      <b-form-select id="pick-wording" v-model="requestStyling.wording" :options="wordingOptions" class="mb-2" /> <br>
      <label for="starting-date">Compare to everyday size</label>
      <b-form-select id="starting-date" v-model="requestStyling.compareTo" :options="compareToOptions" class="mb-2" :disabled="requestStyling.wording == 'absolute'"/> <br>
      <label for="end-date">Theme</label>
      <b-form-select id="end-date" v-model="requestStyling.theme" :options="themeOptions" class="mb-2" />
    </b-form>
</template>

<script>
import store from '../store.js'

export default {
  name: 'StylingForm',
  components: {
  },
  data() {
    return {
      requestStyling : store.cardRequest.styling,
      requestData : store.cardRequest.data,
      meta: null,

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
  computed: {
    compareToOptions()  {
      var options = [ { value: null, text: 'Select an everyday size', disabled: true }, ];
      if (this.requestData.param != null && this.meta != null) {
        for (const compare of this.meta[this.requestData.param].param_specs.param_conversion) {
          options.push({ value: compare, text: this.capitFirstChar(compare) });
        }
      }
      return options;
    },
  },
  methods: {
    
  },
  async created() {
    this.meta = await store.datasets();
  }
}
</script>

<style lang="scss" scoped>

</style>
