<template>
  <div class="mall">
    <Header/>
    <div class="main">
      <!-- 筛选条件 -->
      <div class="condition">
        <ul class="cate-list">
          <li class="title">商品分类:</li>
          <li :class="filter.goods_category==0?'this':''" @click="filter.goods_category=0">全部</li>
          <li :class="filter.goods_category==category.id?'this':''" v-for="category in category_list"
              @click="filter.goods_category=category.id" :key="category.name">{{ category.name }}
          </li>
        </ul>
        <div class="ordering">
          <ul>
            <ul>
              <li class="title">筛&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;选:</li>
              <li class="default" :class="(filter.ordering=='id' || filter.ordering=='-id')?'this':''"
                  @click="filter.ordering='-id'">默认
              </li>
              <li class="hot" :class="(filter.ordering=='sold_num' || filter.ordering=='-sold_num')?'this':''"
                  @click="filter.ordering=(filter.ordering=='-sold_num'?'sold_num':'-sold_num')">人气
              </li>
              <li class="time"
                  :class="filter.ordering=='updated_time'?'updated_time_up this':(filter.ordering=='-updated_time'?'updated_time_down this':'')"
                  @click="filter.ordering=(filter.ordering=='-updated_time'?'updated_time':'-updated_time')">最新
              </li>
            </ul>
          </ul>
          <p class="condition-result">共{{ goods_total }}个商品</p>
        </div>
      </div>
      <!--商品-->
      <div class="goods-list">
        <div class="goods-item" v-for="goods in goods_list" :key="goods.name">
          <div class="goods-image">
            <router-link :to="'/mall/detail/'+goods.id">
              <img :src="goods.goods_img" alt="">
            </router-link>
          </div>
          <div class="goods-info">
            <h3>
              <router-link :to="'/mall/detail/'+goods.id">{{ goods.name }}</router-link>
              <span><img src="@/assets/img/icon.svg" alt="">{{ goods.sold_num }}人买过</span>
            </h3>
            <p goods-other-info>
              <span>{{ goods.click_num }}人看过,{{ goods.fav_num }}人喜欢,剩余{{ goods.goods_num }}件</span>
            </p>
            <br>
            <p goods-desc>
              <span>{{ goods.desc.substring(0,149)+"--------" }}</span>
            </p>
            <div class="pay-box">
              <span class="goods_price">￥{{ goods.goods_price }}</span>
              <span class="buy-now">立即购买</span>
              <span class="buy-now">加入购物车</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'

export default {
  name: 'mall',
  data () {
    return {
      category_list: [], // 商品分类列表
      goods_list: [], // 商品列表
      goods_total: 2, // 当前商品的总数量
      filter: {
        goods_category: 0, // 当前用户选择的商品分类，刚进入页面默认为全部，值为0
        ordering: '-id', // 数据的排序方式，默认值是-id，表示对于id进行降序排列
        page_size: 2, // 单页数据量
        page: 1
      }
    }
  },
  created () {
    this.get_category()
    this.get_goods()
  },
  components: {
    Header,
    Footer
  },
  watch: {
    'filter.goods_category': function () {
      this.filter.page = 1
      this.get_goods()
    },
    'filter.ordering': function () {
      this.get_goods()
    },
    'filter.page_size': function () {
      this.get_goods()
    },
    'filter.page': function () {
      this.get_goods()
    }
  },
  methods: {
    handleSizeChange (val) {
      // 每页数据量发生变化时执行的方法
      this.filter.page = 1
      this.filter.page_size = val
    },
    handleCurrentChange (val) {
      // 页码发生变化时执行的方法
      this.filter.page = val
    },
    get_category() {
      // 获取商品分类信息
      this.$axios.get(`${this.$settings.base_url}/goods/categories/`).then(response => {
        this.category_list = response.data
      }).catch(() => {
        this.$message({
          message: '获取商品分类信息有误，请联系客服工作人员'
        })
      })
    },
    get_goods () {
      // 排序
      let filters = {
        ordering: this.filter.ordering // 排序
      }
      // 判决是否进行分类商品的展示
      if (this.filter.goods_category > 0) {
        filters.goods_category = this.filter.goods_category
      }

      // 设置单页数据量
      if (this.filter.page_size > 0) {
        filters.page_size = this.filter.page_size
      } else {
        filters.page_size = 5
      }

      // 设置当前页码
      if (this.filter.page > 1) {
        filters.page = this.filter.page
      } else {
        filters.page = 1
      }

      // 获取商品列表信息
      this.$axios.get(`${this.$settings.base_url}/goods/goods/`, {
        params: filters
      }).then(response => {
        // console.log(response.data);
        this.goods_list = response.data.results
        this.goods_total = response.data.count
        // console.log(this.goods_list);
      }).catch(() => {
        this.$message({
          message: '获取商品信息有误，请联系客服工作人员'
        })
      })
    }
  }
}
</script>

<style scoped>
.mall {
  background: #f6f6f6;
}

.mall .main {
  width: 1100px;
  margin: 35px auto 0;
}

.mall .condition {
  margin-bottom: 35px;
  padding: 25px 30px 25px 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.mall .cate-list {
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
  padding-bottom: 18px;
  margin-bottom: 17px;
}

.mall .cate-list::after {
  content: "";
  display: block;
  clear: both;
}

.mall .cate-list li {
  float: left;
  font-size: 16px;
  padding: 6px 15px;
  line-height: 16px;
  margin-left: 14px;
  position: relative;
  transition: all .3s ease;
  cursor: pointer;
  color: #4a4a4a;
  border: 1px solid transparent; /* transparent 透明 */
}

.mall .cate-list .title {
  color: #888;
  margin-left: 0;
  letter-spacing: .36px;
  padding: 0;
  line-height: 28px;
}

.mall .ordering .title {
  font-size: 16px;
  color: #888;
  letter-spacing: .36px;
  margin-left: 0;
  padding: 0;
  line-height: 28px;
}

.mall .cate-list .this {
  color: #ffc210;
  border: 1px solid #ffc210 !important;
  border-radius: 10px;
}

.mall .ordering::after {
  content: "";
  display: block;
  clear: both;
}

.mall .ordering ul {
  float: left;
}

.mall .ordering ul::after {
  content: "";
  display: block;
  clear: both;
}

.mall .ordering .condition-result {
  float: right;
  font-size: 14px;
  color: #9b9b9b;
  line-height: 28px;
}


.mall .ordering ul li {
  float: left;
  padding: 6px 15px;
  line-height: 16px;
  margin-left: 14px;
  position: relative;
  transition: all .3s ease;
  cursor: pointer;
  color: #4a4a4a;
}

.mall .ordering .title {
  font-size: 16px;
  color: #888;
  letter-spacing: .36px;
  margin-left: 0;
  padding: 0;
  line-height: 28px;
}

.mall .ordering .this {
  color: #ffc210;
}

.mall .ordering .time {
  position: relative;
}

.mall .ordering .time::before,
.mall .ordering .time::after {
  cursor: pointer;
  content: "";
  display: block;
  width: 0px;
  height: 0px;
  border: 5px solid transparent;
  position: absolute;
  right: 0;
}

.mall .ordering .time::before {
  border-bottom: 5px solid #aaa;
  margin-bottom: 2px;
  top: 2px;
}

.mall .ordering .time::after {
  border-top: 5px solid #aaa;
  bottom: 2px;
}

.mall .ordering .time_up::before {
  border-bottom-color: #ffc210;
}

.mall .ordering .time_down::after {
  border-top-color: #ffc210;
}

.mall .goods-item .goods-info {
  float: left;
  width: 596px;
}

.mall .goods-item:hover {
  box-shadow: 4px 6px 16px rgba(0, 0, 0, .5);
}

.mall .goods-item {
  background: #fff;
  padding: 20px 20px 20px 20px;
  margin-bottom: 35px;
  border-radius: 10px;
  cursor: pointer;
  box-shadow: 2px 3px 16px rgba(0, 0, 0, .1);
  /* css3.0 过渡动画 hover 事件操作 */
  transition: all .2s ease;
}

.mall .goods-item::after {
  content: "";
  display: block;
  clear: both;
}

/* 顶级元素 父级元素  当前元素{} */
.mall .goods-item .goods-image {
  float: left;
  width: 423px;
  height: 210px;
  margin-right: 30px;
}

.mall .goods-item .goods-image img {
  max-width: 100%;
  max-height: 210px;
}

.goods-item {
  position: relative;
}

.mall .goods-item .goods-info {
  float: left;
  width: 596px;
}

.goods-item .goods-info h3 a {
  font-size: 26px;
  color: #333;
  font-weight: normal;
  margin-bottom: 8px;
}

.goods-item .goods-info h3 span {
  font-size: 14px;
  color: #9b9b9b;
  float: right;
  margin-top: 14px;
}

.goods-item .goods-info h3 span img {
  width: 11px;
  height: auto;
  margin-right: 7px;
}

.goods-item .goods-info .goods-other-info {
  font-size: 14px;
  color: #9b9b9b;
  margin-bottom: 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
}

.goods-item .goods-info .goods-other-info span {
  float: left;
}

.goods-item .pay-box {
  position: absolute;
  bottom: 20px;
  width: 600px;
}

.goods-item .pay-box::after {
  content: "";
  display: block;
  clear: both;
}

.goods-item .pay-box .goods_price {
  font-size: 24px;
  color: #fa6240;
  float: left;
}

.goods-item .pay-box .original-price {
  text-decoration: line-through;
  font-size: 14px;
  color: #9b9b9b;
  margin-left: 10px;
  float: left;
  margin-top: 10px;
}

.goods-item .pay-box .buy-now {
  width: 120px;
  height: 38px;
  background: transparent;
  color: #fa6240;
  font-size: 16px;
  border: 1px solid #fd7b4d;
  border-radius: 10px;
  transition: all .2s ease-in-out;
  float: right;
  text-align: center;
  line-height: 38px;
  right: 0;
  bottom: 5px;
}

.goods-item .pay-box .buy-now:hover {
  color: #fff;
  background: #ffc210;
  border: 1px solid #ffc210;
}

.goods .goods_pagination {
  margin-bottom: 60px;
  text-align: center;
}
</style>
