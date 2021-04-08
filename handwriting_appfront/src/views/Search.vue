<template>
  <div class="search-video video">
    <Header/>

    <!-- 视频列表 -->
    <div class="main">
      <div v-if="video_list.length > 0" class="video-list">
        <div class="video-item" v-for="video in video_list" :key="video.name">
          <div class="video-image">
            <img :src="video.video_img" alt="">
          </div>
          <div class="video-info">
            <h3>
              <router-link :to="'/video/detail/'+video.id">{{ video.name }}</router-link>
              <span><img src="" alt="">{{ video.students }}人已加入学习</span></h3>
            <p class="teather-info">
              {{ video.organization.name }} {{ video.organization.title }} {{ video.organization.signature }}
              <span
                v-if="video.sections>video.pub_sections">共{{ video.sections }}小节/已更新{{ video.pub_sections }}小节</span>
              <span v-else>共{{ video.sections }}小节/更新完成</span>
            </p>
            <ul class="sections-list">
              <li v-for="(section,i) in video.video_section" :i="section.name">
                <span class="sections-title">0{{ i + 1 }}&nbsp;|&nbsp;{{ section.name }}</span>
              </li>
            </ul>
            <p class="handwriting">字之纵横,犹屋之楹梁,宜平直,不宜倾欹。</p>
          </div>
        </div>
      </div>
      <div v-else style="text-align: center; line-height: 60px">
        没有搜索结果
      </div>
      <div class="video_pagination block">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page.sync="filter.page"
          :page-sizes="[2, 3, 5, 10]"
          :page-size="filter.page_size"
          layout="sizes, prev, pager, next"
          :total="video_total">
        </el-pagination>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/components/Header'
// eslint-disable-next-line no-unused-vars
import Footer from '../components/Footer'


export default {
  name: "Searchvideo",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      video_list: [],
      video_total: 0,
      filter: {
        page_size: 10,
        page: 1,
        search: '',
      }
    }
  },
  created() {
    this.get_video()
  },
  watch: {
    '$route.query'() {
      this.get_video()
    }
  },
  methods: {
    handleSizeChange(val) {
      // 每页数据量发生变化时执行的方法
      this.filter.page = 1;
      this.filter.page_size = val;
    },
    handleCurrentChange(val) {
      // 页码发生变化时执行的方法
      this.filter.page = val;
    },
    get_video() {
      // 获取搜索的关键字
      this.filter.search = this.$route.query.name || this.$route.query.wd;

      // 获取视频列表信息
      this.$axios.get(`${this.$settings.base_url}/video/search/`, {
        params: this.filter
      }).then(response => {
        // 如果后台不分页，数据在response.data中；如果后台分页，数据在response.data.results中
        this.video_list = response.data.results;
        this.video_total = response.data.count;
      }).catch(() => {
        this.$message({
          message: "获取视频信息有误，请联系客服工作人员"
        })
      })
    }
  }
}
</script>

<style scoped>
.video {
  background: #f6f6f6;
}

.video .main {
  width: 1100px;
  margin: 35px auto 0;
}

.video .condition {
  margin-bottom: 35px;
  padding: 25px 30px 25px 20px;
  background: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.video .cate-list {
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
  padding-bottom: 18px;
  margin-bottom: 17px;
}

.video .cate-list::after {
  content: "";
  display: block;
  clear: both;
}

.video .cate-list li {
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

.video .cate-list .title {
  color: #888;
  margin-left: 0;
  letter-spacing: .36px;
  padding: 0;
  line-height: 28px;
}

.video .cate-list .this {
  color: #ffc210;
  border: 1px solid #ffc210 !important;
  border-radius: 30px;
}

.video .ordering::after {
  content: "";
  display: block;
  clear: both;
}

.video .ordering ul {
  float: left;
}

.video .ordering ul::after {
  content: "";
  display: block;
  clear: both;
}

.video .ordering .condition-result {
  float: right;
  font-size: 14px;
  color: #9b9b9b;
  line-height: 28px;
}

.video .ordering ul li {
  float: left;
  padding: 6px 15px;
  line-height: 16px;
  margin-left: 14px;
  position: relative;
  transition: all .3s ease;
  cursor: pointer;
  color: #4a4a4a;
}

.video .ordering .title {
  font-size: 16px;
  color: #888;
  letter-spacing: .36px;
  margin-left: 0;
  padding: 0;
  line-height: 28px;
}

.video .ordering .this {
  color: #ffc210;
}

.video .ordering .price {
  position: relative;
}

.video .ordering .price::before,
.video .ordering .price::after {
  cursor: pointer;
  content: "";
  display: block;
  width: 0px;
  height: 0px;
  border: 5px solid transparent;
  position: absolute;
  right: 0;
}

.video .ordering .price::before {
  border-bottom: 5px solid #aaa;
  margin-bottom: 2px;
  top: 2px;
}

.video .ordering .price::after {
  border-top: 5px solid #aaa;
  bottom: 2px;
}

.video .ordering .price_up::before {
  border-bottom-color: #ffc210;
}

.video .ordering .price_down::after {
  border-top-color: #ffc210;
}

.video .video-item:hover {
  box-shadow: 4px 6px 16px rgba(0, 0, 0, .5);
}

.video .video-item {
  width: 1100px;
  background: #fff;
  padding: 20px 30px 20px 20px;
  margin-bottom: 35px;
  border-radius: 2px;
  cursor: pointer;
  box-shadow: 2px 3px 16px rgba(0, 0, 0, .1);
  /* css3.0 过渡动画 hover 事件操作 */
  transition: all .2s ease;
}

.video .video-item::after {
  content: "";
  display: block;
  clear: both;
}

/* 顶级元素 父级元素  当前元素{} */
.video .video-item .video-image {
  float: left;
  width: 423px;
  height: 210px;
  margin-right: 30px;
}

.video .video-item .video-image img {
  max-width: 100%;
  max-height: 210px;
}

.video .video-item .video-info {
  float: left;
  width: 596px;
}

.video-item .video-info h3 a {
  font-size: 26px;
  color: #333;
  font-weight: normal;
  margin-bottom: 8px;
}

.video-item .video-info h3 span {
  font-size: 14px;
  color: #9b9b9b;
  float: right;
  margin-top: 14px;
}

.video-item .video-info h3 span img {
  width: 11px;
  height: auto;
  margin-right: 7px;
}

.video-item .video-info .teather-info {
  font-size: 14px;
  color: #9b9b9b;
  margin-bottom: 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
}

.video-item .video-info .teather-info span {
  float: right;
}

.video-item .sections-list::after {
  content: "";
  display: block;
  clear: both;
}

.video-item .sections-list li {
  float: left;
  width: 44%;
  font-size: 14px;
  color: #666;
  padding-left: 22px;
  margin-bottom: 15px;
}

.video-item .sections-list li .sections-title {
  /* 以下3句，文本内容过多，会自动隐藏，并显示省略符号 */
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  display: inline-block;
  max-width: 200px;
}

.video-item .sections-list li:hover {
  color: #ffc210;
}

.video-item .sections-list li .video {
  width: 34px;
  height: 20px;
  color: #fd7b4d;
  vertical-align: super;
  margin-left: 10px;
  border: 1px solid #fd7b4d;
  border-radius: 2px;
  text-align: center;
  font-size: 13px;
  white-space: nowrap;
}

.video-item .sections-list li:hover .video {
  color: #ffc210;
  border-color: #ffc210;
}

.video-item .section-list li:hover .video {
  color: #ffc210;
  border-color: #ffc210;
}

.video-item {
  position: relative;
}

.video-item .pay-box {
  position: absolute;
  bottom: 20px;
  width: 600px;
}

.video-item .pay-box::after {
  content: "";
  display: block;
  clear: both;
}

.video-item .pay-box .discount-type {
  padding: 6px 10px;
  font-size: 16px;
  color: #fff;
  text-align: center;
  margin-right: 8px;
  background: #fa6240;
  border: 1px solid #fa6240;
  border-radius: 10px 0 10px 0;
  float: left;
}

.video-item .pay-box .discount-price {
  font-size: 24px;
  color: #fa6240;
  float: left;
}

.video-item .pay-box .original-price {
  text-decoration: line-through;
  font-size: 14px;
  color: #9b9b9b;
  margin-left: 10px;
  float: left;
  margin-top: 10px;
}

.video-item .pay-box .buy-now {
  width: 120px;
  height: 38px;
  background: transparent;
  color: #fa6240;
  font-size: 16px;
  border: 1px solid #fd7b4d;
  border-radius: 3px;
  transition: all .2s ease-in-out;
  float: right;
  text-align: center;
  line-height: 38px;
  position: absolute;
  right: 0;
  bottom: 5px;
}

.video-item .pay-box .buy-now:hover {
  color: #fff;
  background: #ffc210;
  border: 1px solid #ffc210;
}

.video .video_pagination {
  margin-bottom: 60px;
  text-align: center;
}
</style>
