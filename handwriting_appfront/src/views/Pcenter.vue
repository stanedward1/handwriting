<template>
  <div class="home">
    <Header/>
    <br><br>
    <div v-for="item in user" :key="user.username">
      {{item}}
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'

export default {
  name: 'Home',
  data() {
    return {
      user: {}
    }
  },
  created() {
    this.get_user()
  },
  components: {
    Header,
    Footer,
  },
  methods: {
    get_user() {
      let token = this.$cookies.get('token')
      if (!token) {
        this.$message({
          message: '您还没登录，请登录！'
        })
        return false
      }
      this.$axios.get(`${this.$settings.base_url}/user/user/`, {
      headers: {
          Authorization: 'jwt ' + token
        },
      }).then(response => {
        console.log(response.data)
        this.user = response.data
      }).catch((error) => {
        console.log(error)
        this.$message({
          message: '获取用户信息有误，请联系客服工作人员'
        })
      })
    }
  }
}
</script>

<style>

</style>
