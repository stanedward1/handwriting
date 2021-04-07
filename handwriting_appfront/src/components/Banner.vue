<template>
    <div class="banner">
        <el-carousel height="400px">
            <el-carousel-item v-for="item in banner_list" :key="item">
<!--                <img src="../assets/img/banner3.jpg" alt="">-->
              <router-link :to="item.link">
                <img :src="item.img" :alt="name">
              </router-link>
            </el-carousel-item>
        </el-carousel>
    </div>
</template>

<script>
export default {
  name: 'Banner',
  data () {
    return {
      banner_list: []
    }
  },
  created () {
    // 当组件一创建，就向后台发请求，拿回轮播图数据
    this.$axios.get(this.$settings.base_url + '/home/banner/').then(response => {
      console.log(response.data)
      this.banner_list = response.data
      // eslint-disable-next-line handle-callback-err
    }).catch(error => {
      console.log(error)
    })
  }
}
</script>

<style scoped>
    .el-carousel-item {
        height: 400px;
        min-width: 1200px;
    }
    .el-carousel__item img {
        height: 400px;
        margin-left: calc(50% - 1920px / 2);
    }
</style>
