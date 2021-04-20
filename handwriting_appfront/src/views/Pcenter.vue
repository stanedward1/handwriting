<template>
  <div>
    <Header/>
    <el-avatar :size="50" :src="circleUrl"></el-avatar>
    <Footer/>
  </div>
</template>

<script>
import Header from '../components/Header';
import Footer from '../components/Footer';

export default {
  name: "Pcenter",
  components: {Footer, Header},
  data() {
    return {
      circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
    }
  }
}
</script>

<style scoped>

</style>
