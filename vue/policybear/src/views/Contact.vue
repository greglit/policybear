<template>
  <div>
      <b-container class="text-left mb-5">
        <navbar showIcon sm/>
        <h1>About us</h1>
        <div class="d-flex my-4 justify-content-around flex-wrap">
          <contact-card
            :imageSrc="require('@/assets/img/profileGregor.jpg')"
            :firstName="'Gregor'" :lastName="'Wolf'"
            :description="'I am a Computer Scientist with a focus on Human-Machine Interaction and some years of experience in full stack web development. I am especially interested in modern data-driven user interfaces that close the gap between advanced tech like Big Data or Artificial Intelligence and the people who should benefit from such technical advancements.'"
            :github="'https://github.com/greglit'"
            :homepage="'https://gregl.it'"
          />
          <contact-card
            :imageSrc="require('@/assets/img/profileFiete.jpg')"
            :firstName="'Friedrich'" :lastName="'Röseler'"
            :description="'I am a Physical Geographer with expertise in remote sensing based data analysis and Geographic Information Systems (GIS). The topics I find most attractive include soils in particular and land cover dynamics coupled with interaction processes between pedosphere, plants and the atmosphere on a global scale.'"
            :github="'https://github.com/greglit'"
          />
        </div>
        <h1>Contact Information</h1>
        <p>If you are interested in any kind of collaboration or if you have any questions or suggestions, feel free to conatct us!</p>
        <h5><b-icon-envelope-fill class="mr-2"/>policybear@gregl.it <b-icon-github class="ml-3 mr-2"/><a href="https://github.com/greglit/policybear">policybear</a></h5>

        <h1>Imprint</h1>
        <h4>Gregor Wolf</h4>
        <h5>Bergstraße 30<br/>82131 Gauting<br/>policybear@gregl.it</h5>
      </b-container>
  </div>
</template>

<script>
import ContactCard from '../components/ContactCard.vue'
import Navbar from '../components/Navbar.vue'

export default {
  name: 'Contact',
  components: {
    Navbar,
    ContactCard,
  },
  props: [],
  data() {
    return {
    }
  },
  mounted () {
    window.scrollTo(0, 0)
  },
}
</script>

<style lang="scss" scoped>
h1 {
  margin-top: 20px;
}
</style>
