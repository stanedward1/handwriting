<template>
  <div class="home">
    <Header/>
    <br><br>
    <div class="main">
      <div v-for="item in user" :key="user.username" style="text-align: center">
        <el-avatar :size="size" :src="item.icon"></el-avatar>
        <br>
        <p>用户名：{{ item.username }}</p>
        <p>收货地址: {{ item.address }}</p>
        <br>
        <!--      <img :src="item.icon" height="50px" width="50px">-->
        <hr>
        <div>
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="头像">
              <el-input v-model="icon"></el-input>
            </el-form-item>
            <el-form-item label="用户id">
              <el-input v-model="id"></el-input>
            </el-form-item>
            <el-form-item label="用户名">
              <el-input v-model="username"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="password"></el-input>
            </el-form-item>
            <el-form-item label="收货地址">
              <el-input v-model="address"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="updata_user">立即修改</el-button>
            </el-form-item>
          </el-form>
        </div>
        <hr>
      </div>
      <div style="text-align: center">
        <h1>我的订单</h1>
        <el-table
          :data="order"
          style="text-align: center">
          <el-table-column
            prop="subject"
            label="订单名称"
            width="180">
          </el-table-column>
          <el-table-column
            prop="total_amount"
            label="总价格"
            width="180">
          </el-table-column>
          <el-table-column
            prop="pay_type"
            label="支付类型">
          </el-table-column>
        </el-table>
      </div>
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
      user: {},
      username: '',
      password: '',
      address: '',
      icon: '',
      id: '',
      subject: '',
      total_amount: '',
      pay_type: 1
    }
  },
  created() {
    this.get_user()
    this.updata_user()
    this.get_order()
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
    },
    get_order() {
      let token = this.$cookies.get('token')
      if (!token) {
        this.$message({
          message: '您还没登录，请登录！'
        })
        return false
      }
      this.$axios.get(`${this.$settings.base_url}/trade/order/`, {
        headers: {
          Authorization: 'jwt ' + token
        },
      }).then(response => {
        console.log(response.data)
        this.order = response.data
      }).catch((error) => {
        console.log(error)
        this.$message({
          message: '获取订单信息有误，请联系longbiu'
        })
      })
    },
    updata_user() {
      this.$axios.put(`${this.$settings.base_url}/user/user/` + this.id + '/', {
        headers: {
          Authorization: 'jwt ' + this.$cookies.get('token'),
        },
        username: this.username,
        password: this.password,
        id: this.id,
        icon: this.icon,
        address: this.address,
      }).then(response => {
        console.log(response.data)
        // this.uuser = response.data
      }).catch((error) => {
        console.log(error)
      })
    }
  },
}
</script>

<style>
.main {
  width: 1100px;
  margin: 35px auto 0;
}
</style>
