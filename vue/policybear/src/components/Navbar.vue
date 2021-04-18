<template>
    <b-navbar type="primary" class="rubik-medium">
      <b-container>
        <b-navbar-brand class="brand d-flex align-items-center" to="/">
          <img v-if="showIcon != undefined" src="../../public/policybear_icon.png" class="d-inline-flex logo mr-3" alt="rudiboard">
          <component :is="sm != undefined ? 'h3':'h1'" 
            :class="[bgDark != undefined ? 'txt-nord6':'txt-nord3', 'd-inline-flex m-0']"
          >
            Policy Bear
          </component>
        </b-navbar-brand>
        
        <!--<b-navbar-nav class="ml-auto">
          <b-nav-text right>
            <b-button variant="border-0" class="nord-btn">
              <b-icon-moon/>
            </b-button>
          </b-nav-text>-->
          <!--<b-nav-item right class="nav-item">
            <b-button variant="border-0" size="sm" v-b-modal.shareModal>
              <b-icon-share-fill/>
            </b-button>
          </b-nav-item>
        </b-navbar-nav>-->
      </b-container>
      <b-modal hide-footer size="lg" id="shareModal" title="Share Policy Bear with others">
        
      </b-modal>
    </b-navbar>
</template>

<script>

export default {
  name: 'Navbar',
  props: ['showIcon', 'bgDark', 'sm'],
  components: {
  },
  data() {
    return {
      
    }
  },
  computed: {
  },
  methods: {
    copyToClipboard(value) {
      let container = this.$refs.container
      this.$copyText(value, container).then((e) => {
        this.makeToast(`Copied "${value}" to the clipboard!`);
      }, (error) => {
        console.log('failed to copy:'+e)
      })
    },
  },
}
</script>

<style lang="scss" scoped>

.logo {
  height: 35px;
  width: 35px;
}

.abs-center-x {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
</style>
