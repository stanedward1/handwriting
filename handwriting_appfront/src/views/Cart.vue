<template>
  <div class="mall">
    <Header/>
    <div class="main">
      <el-table
        :data="carts_list"
        ref="multipleTable"
        tooltip-effect="dark"
        style="width: 100%"
        @selection-change="handleSelectionChange">
        <el-table-column
          type="selection"
          width="55">
        </el-table-column>
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="商品名称">
                <span>{{ props.row.goods.name }}</span>
              </el-form-item>
              <el-form-item label="商品 ID">
                <span>{{ props.row.goods.id }}</span>
              </el-form-item>
              <el-form-item label="商品分类">
                <span>{{ props.row.goods.category.name }}</span>
              </el-form-item>
              <el-form-item label="商品描述">
                <span>{{ props.row.goods.desc }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column
          label="商品 ID"
          prop="goods.id">
        </el-table-column>
        <el-table-column
          label="商品名称"
          prop="goods.name">
        </el-table-column>
        <el-table-column
          label="商品价格"
          prop="goods.goods_price">
        </el-table-column>
        <el-table-column
          label="购买数量"
          prop="nums">
        </el-table-column>
        <el-table-column
          label="描述"
          prop="goods.desc">
        </el-table-column>
      </el-table>
      <div style="margin-top: 20px">
        <el-button @click="toggleSelection()">取消选择</el-button>
        <el-button @click="buy_now()">购买选择的商品</el-button>
        <br><br>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'

export default {
  name: 'Cart',
  data() {
    return {
      carts_list: [], // 购物车列表
      goods_total: 0, // 当前商品的总数量
    }
  },
  created() {
    this.get_carts()
  },
  components: {
    Header,
    Footer
  },
  methods: {
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    get_carts() {
      let token = this.$cookies.get('token')
      if (!token) {
        this.$message({
          message: '您还没登录，请登录！'
        })
        return false
      }
      // 获取商品列表信息
      this.$axios.get(`${this.$settings.base_url}/trade/shopcarts/`, {
        headers: {
          Authorization: 'jwt ' + token
        },
      }).then(response => {
        console.log(response.data);
        this.carts_list = response.data
        this.goods_total = response.data.count
        // console.log(this.goods_list);
      }).catch(() => {
        this.$message({
          message: '获取购物车信息有误，请联系客服工作人员'
        })
      })
    },
    buy_now() {
      let token = this.$cookies.get('token')
      if (!token) {
        this.$message({
          message: '您还没登录，请登录！'
        })
        return false
      }
      this.$axios({
        url: this.$settings.base_url + '/trade/pay/',
        method: 'post',
        headers: {
          Authorization: 'jwt ' + token
        },
        data: {
          subject: "test",
          total_amount: 12,
          pay_type: 1, // 现在只能默认1，为支付宝
          goods: [1, 2]
        }
      }).then(response => {
        // eslint-disable-next-line camelcase
        let pay_url = response.data
        // console.log(pay_url)
        // 本页面标签调整：可以选择 _self 或 _blank
        open(pay_url, '_self')
      }).catch(error => {
        console.log(error.response.data)
      })
    }
  }
}
</script>

<style scoped>
.main {
  width: 1100px;
  margin: 35px auto 0;
}

.demo-table-expand {
  font-size: 0;
  text-align: center;
}

.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}

.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>
