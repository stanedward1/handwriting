<template>
  <div class="video">
    <Header></Header>
    <div class="main">
      <!-- 筛选条件 -->
      <div class="condition">
        <ul class="cate-list">
          <li class="title">视频分类:</li>
          <li :class="filter.video_category==0?'this':''" @click="filter.video_category=0">全部</li>
          <li :class="filter.video_category==category.id?'this':''" v-for="category in category_list"
              @click="filter.video_category=category.id" :key="category.name">{{ category.name }}
          </li>
        </ul>

        <div class="ordering">
          <ul>
            <li class="title">筛&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;选:</li>
            <li class="default" :class="(filter.ordering=='id' || filter.ordering=='-id')?'this':''"
                @click="filter.ordering='-id'">默认
            </li>
            <li class="hot" :class="(filter.ordering=='students' || filter.ordering=='-students')?'this':''"
                @click="filter.ordering=(filter.ordering=='-students'?'students':'-students')">人气
            </li>
            <li class="time"
                :class="filter.ordering=='updated_time'?'updated_time_up this':(filter.ordering=='-updated_time'?'updated_time_down this':'')"
                @click="filter.ordering=(filter.ordering=='-updated_time'?'updated_time':'-updated_time')">最新
            </li>
          </ul>
          <p class="condition-result">共{{ video_total }}个视频</p>
        </div>

      </div>
      <!-- 视频列表 -->
      <div class="video-list">
        <div class="video-item" v-for="video in video_list" :key="video.name">
          <div class="video-image">
            <img :src="video.video_img" alt="">
          </div>
          <div class="video-info">
            <h3>
              <router-link :to="'/video/detail/'+video.id">{{ video.name }}</router-link>
              <span><img src="@/assets/img/icon.svg" alt="">{{ video.students }}人已加入学习</span></h3>
            <p class="organization-info">
              {{ video.organization.name }} {{ video.organization.title }} &nbsp;&nbsp;&nbsp;
              {{ video.organization.signature }}
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
      <!--分页部分-->
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
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'

export default {
  name: 'video',
  data () {
    return {
      category_list: [], // 视频分类列表
      video_list: [], // 视频列表
      video_total: 2, // 当前视频的总数量
      filter: {
        video_category: 0, // 当前用户选择的视频分类，刚进入页面默认为全部，值为0
        ordering: '-id', // 数据的排序方式，默认值是-id，表示对于id进行降序排列
        page_size: 2, // 单页数据量
        page: 1
      }
    }
  },
  created () {
    this.get_category()
    this.get_video()
  },
  components: {
    Header,
    Footer
  },
  watch: {
    'filter.video_category': function () {
      this.filter.page = 1
      this.get_video()
    },
    'filter.ordering': function () {
      this.get_video()
    },
    'filter.page_size': function () {
      this.get_video()
    },
    'filter.page': function () {
      this.get_video()
    }
  },
  methods: {
    handleSizeChange(val) {
      // 每页数据量发生变化时执行的方法
      this.filter.page = 1
      this.filter.page_size = val
    },
    handleCurrentChange(val) {
      // 页码发生变化时执行的方法
      this.filter.page = val
    },
    get_category() {
      // 获取视频分类信息
      this.$axios.get(`${this.$settings.base_url}/video/categories/`).then(response => {
        this.category_list = response.data
      }).catch(() => {
        this.$message({
          message: '获取视频分类信息有误，请联系客服工作人员'
        })
      })
    },
    get_video() {
      // 排序
      let filters = {
        ordering: this.filter.ordering // 排序
      }
      // 判决是否进行分类视频的展示
      if (this.filter.video_category > 0) {
        filters.video_category = this.filter.video_category
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

      // 获取视频列表信息
      this.$axios.get(`${this.$settings.base_url}/video/video/`, {
        params: filters
      }).then(response => {
        // console.log(response.data);
        this.video_list = response.data.results
        this.video_total = response.data.count
        // console.log(this.video_list);
      }).catch(() => {
        this.$message({
          message: '获取视频信息有误，请联系客服工作人员'
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
  border-radius: 10px;
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
  border-radius: 10px;
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

.video .ordering ul handwriting {
  margin: auto;
  font-size: 30px;
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

.video .ordering .time {
  position: relative;
}

.video .ordering .time::before,
.video .ordering .time::after {
  cursor: pointer;
  content: "";
  display: block;
  width: 0px;
  height: 0px;
  border: 5px solid transparent;
  position: absolute;
  right: 0;
}

.video .ordering .time::before {
  border-bottom: 5px solid #aaa;
  margin-bottom: 2px;
  top: 2px;
}

.video .ordering .time::after {
  border-top: 5px solid #aaa;
  bottom: 2px;
}

.video .ordering .time_up::before {
  border-bottom-color: #ffc210;
}

.video .ordering .time_down::after {
  border-top-color: #ffc210;
}

.video .video-item:hover {
  box-shadow: 4px 6px 16px rgba(0, 0, 0, .5);
}

.video .video-item {
  background: #fff;
  padding: 20px 30px 20px 20px;
  margin-bottom: 35px;
  border-radius: 10px;
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

.video-item .video-info .organization-info {
  font-size: 14px;
  color: #9b9b9b;
  margin-bottom: 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
}

.video-item .video-info .organization-info span {
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
  /* background: url("路径") 是否平铺 x轴位置 y轴位置 */
  /*background: url("./src/assets/img/play.svg") no-repeat left 4px;*/
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
  /*background-image: url("./src/assets/img/play.svg");*/
  color: #ffc210;
}

.video-item .sections-list li .video {
  width: 34px;
  height: 20px;
  color: #fd7b4d;
  vertical-align: super;
  margin-left: 10px;
  border: 1px solid #fd7b4d;
  border-radius: 10px;
  text-align: center;
  font-size: 13px;
  white-space: nowrap;
}

.video-item .sections-list li:hover .video {
  color: #ffc210;
  border-color: #ffc210;
}

.video-item {
  position: relative;
}

.video .video_pagination {
  margin-bottom: 60px;
  text-align: center;
}
</style>
