<template>
  <div class="detail">
    <Header/>
    <div class="main">
      <div class="goods-item">
        <div class="goods-info">
          <div class="goods-image">
            <img :src="goods_info.goods_img" alt="">
          </div>
          <div class="wrap-right">
            <h3 class="goods-name">{{ goods_info.name }}</h3>
            <p class="data">{{ goods_info.sold_num }}人买过,{{ goods_info.fav_num }}人想买</p>
            <p class="data-fav">{{ goods_info.click_num }}人浏览过该商品，剩余{{ goods_info.goods_num }}件商品</p>
            <div class="desc"><span>简介:{{ goods_desc }}</span>
            </div>
            <div class="pay-box">
              <span class="goods_price">￥{{ goods_info.goods_price }}</span>
              <span class="buy-now">立即购买</span>
              <span class="buy-now">加入购物车</span>
            </div>
          </div>
        </div>
        <div class="goods-tab">
          <ul class="tab-list">
            <li :class="tabIndex==1?'active':''" @click="tabIndex=1">详情介绍</li>
            <li :class="tabIndex==2?'active':''" @click="tabIndex=2">用户评论</li>
            <li :class="tabIndex==3?'active':''" @click="tabIndex=3">常见问题</li>
          </ul>
        </div>
        <div class="goods-content">
          <div class="goods-tab-list">
            <div class="tab-item" v-if="tabIndex==1">
              <div class="goods-desc" v-html="goods_info.desc"></div>
              <img :src="goods_info.detail_img" alt="">
            </div>
            <div class="tab-item" v-if="tabIndex==2">
              用户评论
            </div>
            <div class="tab-item" v-if="tabIndex==3">
              常见问题
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
  name: 'GoodsDetail',
  data() {
    return {
      tabIndex: 2,
      goods_id: 0,
      goods_info: {
        name: {},
        desc: {},
        sold_num: {},
        fav_num: {},
        goods_img: {},
        goods_price: {}
      }
    }
  },
  created() {
    this.get_goods_id()
    this.get_goods_data()
  },
  components: {
    Header,
    Footer
  },
  methods: {
    get_goods_id() {
      this.goods_id = this.$route.params.id || this.$route.query.id
      if (this.goods_id < 1) {
        let _this = this
        _this.$alert('对不起，当前商品不存在！', '警告', {
          callback() {
            _this.$router.go(-1)
          }
        })
      }
    },
    get_goods_data() {
      this.$axios.get(`${this.$settings.base_url}/goods/goods/${this.goods_id}/`).then(response => {
        // window.console.log(response.data);
        this.goods_info = response.data
        this.goods_desc = response.data.desc.substring(0, 255) + "--------"
        console.log(this.goods_info)
      }).catch(() => {
        this.$message({
          message: '对不起，访问页面出错！请联系客服工作人员！'
        })
      })
    }
  }
}
</script>

<style scoped>
.main {
  background: #fff;
  padding-top: 30px;
}

.goods-info {
  width: 1200px;
  margin: 0 auto;
  overflow: hidden;
}

.goods-image {
  float: left;
}

.wrap-right {
  position: relative;
  height: 300px;
}

.goods-name {
  font-size: 20px;
  text-align: center;
  color: #333;
  padding: 10px 23px;
  letter-spacing: .45px;
}

.data {
  padding-left: 23px;
  text-align: center;
  padding-right: 23px;
  padding-bottom: 16px;
  font-size: 14px;
  color: #9b9b9b;
}

.data-fav {
  background: #fa6240;
  font-size: 14px;
  color: #4a4a4a;
  padding: 10px 23px;
  overflow: hidden;
}

.pay-box .buy-now {
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

.pay-box .buy-now:hover {
  color: #fff;
  background: #ffc210;
  border: 1px solid #ffc210;
}

.goods_price {
  font-size: 24px;
  color: #fa6240;
  float: left;
}

.pay-box::after {
  content: "";
  display: block;
  clear: both;
}

.goods-tab {
  width: 100%;
  background: #fff;
  margin-bottom: 30px;
  box-shadow: 0 2px 4px 0 #f0f0f0;

}

.goods-tab .tab-list {
  width: 1200px;
  margin: auto;
  color: #4a4a4a;
  overflow: hidden;
}

.tab-list li {
  float: left;
  margin-right: 15px;
  padding: 26px 20px 16px;
  font-size: 17px;
  cursor: pointer;
}

.tab-list .active {
  color: #ffc210;
  border-bottom: 2px solid #ffc210;
}

.tab-list .free {
  color: #fb7c55;
}

.goods-content {
  width: 1200px;
  margin: 0 auto;
  background: #FAFAFA;
  overflow: hidden;
  padding-bottom: 40px;
}

.goods-tab-list {
  width: 880px;
  height: auto;
  padding: 20px;
  background: #fff;
  float: left;
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.tab-item {
  background: #fff;
  white-space: pre-wrap;
  padding-bottom: 20px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.tab-item-title {
  justify-content: space-between;
  padding: 25px 20px 11px;
  border-radius: 4px;
  margin-bottom: 20px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
  overflow: hidden;
}

.chapter {
  font-size: 17px;
  color: #4a4a4a;
  float: left;
}

.chapter-length {
  float: right;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
}

.chapter-title {
  font-size: 16px;
  color: #4a4a4a;
  letter-spacing: .26px;
  padding: 12px;
  background: #eee;
  border-radius: 2px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}

.chapter-title img {
  width: 18px;
  height: 18px;
  margin-right: 7px;
  vertical-align: middle;
}

.section-list {
  padding: 0 20px;
}

.section-list .section-item {
  padding: 15px 20px 15px 36px;
  cursor: pointer;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
}

.section-item .name {
  font-size: 14px;
  color: #666;
  float: left;
}

.section-item .index {
  margin-right: 5px;
}

.section-item .free {
  font-size: 12px;
  color: #fff;
  letter-spacing: .19px;
  background: #ffc210;
  border-radius: 100px;
  padding: 1px 9px;
  margin-left: 10px;
}

.section-item .time {
  font-size: 14px;
  color: #666;
  letter-spacing: .23px;
  opacity: 1;
  transition: all .15s ease-in-out;
  float: right;
}

.section-item .time img {
  width: 18px;
  height: 18px;
  margin-left: 15px;
  vertical-align: text-bottom;
}

.section-item .try {
  width: 86px;
  height: 28px;
  background: #ffc210;
  border-radius: 4px;
  font-size: 14px;
  color: #fff;
  position: absolute;
  right: 20px;
  top: 10px;
  opacity: 0;
  transition: all .2s ease-in-out;
  cursor: pointer;
  outline: none;
  border: none;
}

.section-item:hover {
  background: #fcf7ef;
  box-shadow: 0 0 0 0 #f3f3f3;
}

.section-item:hover .name {
  color: #333;
}

.section-item:hover .try {
  opacity: 1;
}

.goods-side {
  width: 300px;
  height: auto;
  margin-left: 10px;
  margin-right: 10px;
  float: right;
}

.organization-info {
  background: #fff;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.side-title {
  font-weight: normal;
  font-size: 17px;
  color: #4a4a4a;
  padding: 18px 14px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
}

.side-title span {
  display: inline-block;
  border-left: 2px solid #ffc210;
  padding-left: 12px;
}

.organization-content {
  padding: 30px 20px;
  box-sizing: border-box;
}

.organization-content .cont1 {
  margin-bottom: 12px;
  overflow: hidden;
}

.organization-content .cont1 img {
  width: 54px;
  height: 54px;
  margin-right: 12px;
  float: left;
}

.organization-content .cont1 .name {
  float: right;
}

.organization-content .cont1 .organization-name {
  width: 188px;
  font-size: 16px;
  color: #4a4a4a;
  padding-bottom: 4px;
}

.organization-content .cont1 .organization-title {
  width: 188px;
  font-size: 13px;
  color: #9b9b9b;
}
</style>
