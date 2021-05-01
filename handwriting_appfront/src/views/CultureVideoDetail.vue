<template>
    <div class="detail">
        <Header/>
        <div class="main">
            <div class="video-info">
                <div class="wrap-left">
                    <videoPlayer class="video-player vjs-custom-skin"
                                 ref="videoPlayer"
                                 :playsinline="true"
                                 :options="playerOptions"
                                 @play="onPlayerPlay($event)"
                                 @pause="onPlayerPause($event)">
                    </videoPlayer>
                </div>
                <div class="wrap-right">
                    <h3 class="video-name">{{video_info.name}}</h3>
                    <p class="data">{{video_info.students}}人在学&nbsp;&nbsp;&nbsp;&nbsp;视频总时长：{{video_info.sections}}小节/{{video_info.pub_sections}}小时</p>
                    <div class="sale-time">
                        <p class="sale-type">更新时间 <span class="video.info.updated_time">{{video_info.updated_time}}</span></p>
                    </div>
                </div>
            </div>
            <div class="video-tab">
                <ul class="tab-list">
                    <li :class="tabIndex==1?'active':''" @click="tabIndex=1">详情介绍</li>
                    <li :class="tabIndex==2?'active':''" @click="tabIndex=2">视频章节</li>
                    <li :class="tabIndex==3?'active':''" @click="tabIndex=3">用户评论</li>
                    <li :class="tabIndex==4?'active':''" @click="tabIndex=4">常见问题</li>
                </ul>
            </div>
            <div class="video-content">
                <div class="video-tab-list">
                    <div class="tab-item" v-if="tabIndex==1">
                        <div class="video-brief" v-html="video_info.brief"></div>
                    </div>
                    <div class="tab-item" v-if="tabIndex==2">
                        <div class="tab-item-title">
                            <p class="chapter">视频章节</p>
                            <p class="chapter-length">共{{video_chapters.length}}章 {{video_info.sections}}个小节</p>
                        </div>
                        <div class="chapter-item" v-for="chapter in video_chapters" :key="chapter.name">
                            <p class="chapter-title">第{{chapter.chapter}}章·{{chapter.name}}
                            </p>
                            <ul class="section-list">
                                <li class="section-item" v-for="section in chapter.videosections" :key="section.name">
                                    <p class="name"><span class="index">{{chapter.chapter}}-{{section.orders}}</span>
                                        {{section.name}}<span class="free" v-if="section.free_trail">免费</span></p>
                                    <p class="time">{{section.duration}} </p>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="tab-item" v-if="tabIndex==3">
                        用户评论
                    </div>
                    <div class="tab-item" v-if="tabIndex==4">
                        常见问题
                    </div>
                </div>
                <div class="video-side">
                    <div class="organization-info">
                        <h4 class="side-title"><span>视频所属机构或个人</span></h4>
                        <div class="organization-content">
                            <div class="cont1">
                                <img :src="video_info.organization.image">
                                <div class="name">
                                    <p class="organization-name">{{video_info.organization.name}}
                                        {{video_info.organization.title}}</p>
                                    <p class="organization-title">{{video_info.organization.signature}}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
import Header from '@/components/Header'
// eslint-disable-next-line no-unused-vars
import Footer from '../components/Footer'

// 加载组件
import {videoPlayer} from 'vue-video-player'

export default {
  name: 'CultureVideoDetail',
  data () {
    return {
      tabIndex: 2, // 当前选项卡显示的下标
      video_id: 0, // 当前视频信息的ID
      video_info: {
        name: {},
        organization: {}
      }, // 视频信息
      video_chapters: [], // 视频的章节小节列表
      playerOptions: {
        aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        sources: [{ // 播放资源和资源格式
          type: 'video/mp4',
          src: 'http://img.ksbbs.com/asset/Mon_1703/05cacb4e02f9d9e.mp4' // 你的视频地址（必填）
        }]
      }
    }
  },
  created () {
    this.get_video_id()
    this.get_video_data()
    this.get_chapter()
  },
  methods: {
    onPlayerPlay () {
      // 当视频播放时，执行的方法
      console.log('视频开始播放')
    },
    onPlayerPause () {
      // 当视频暂停播放时，执行的方法
      console.log('视频暂停，可以打开广告了')
    },
    get_video_id () {
      // 获取地址栏上面的视频ID
      this.video_id = this.$route.params.id || this.$route.query.id
      if (this.video_id < 1) {
        let _this = this
        _this.$alert('对不起，当前视频不存在！', '警告', {
          callback () {
            _this.$router.go(-1)
          }
        })
      }
    },
    get_video_data () {
      // ajax请求视频信息
      this.$axios.get(`${this.$settings.base_url}/culturevideo/culturevideo/${this.video_id}/`).then(response => {
        // window.console.log(response.data);
        this.video_info = response.data
        console.log(this.video_info)
      }).catch(() => {
        this.$message({
          message: '对不起，访问页面出错！请联系客服工作人员！'
        })
      })
    },

    get_chapter () {
      // 获取当前视频对应的章节小节信息
      this.$axios.get(`${this.$settings.base_url}/culturevideo/culturevideochapter/`, {
        params: {
          'video': this.video_id
        }
      }).then(response => {
        this.video_chapters = response.data
      }).catch(error => {
        window.console.log(error.response)
      })
    }
  },
  components: {
    Header,
    Footer,
    videoPlayer // 注册组件
  }
}
</script>

<style scoped>
    .main {
        background: #fff;
        padding-top: 30px;
    }

    .video-info {
        width: 1200px;
        margin: 0 auto;
        overflow: hidden;
    }

    .wrap-left {
        float: left;
        width: 690px;
        height: 388px;
        background-color: #000;
    }

    .wrap-right {
        float: left;
        position: relative;
        height: 388px;
    }

    .video-name {
        font-size: 20px;
        color: #333;
        padding: 10px 23px;
        letter-spacing: .45px;
    }

    .data {
        padding-left: 23px;
        padding-right: 23px;
        padding-bottom: 16px;
        font-size: 14px;
        color: #9b9b9b;
    }

    .sale-time {
        width: 464px;
        background: #fa6240;
        font-size: 14px;
        color: #4a4a4a;
        padding: 10px 23px;
        overflow: hidden;
    }

    .sale-type {
        font-size: 16px;
        color: #fff;
        letter-spacing: .36px;
        float: left;
    }

    .sale-time .expire {
        font-size: 14px;
        color: #fff;
        float: right;
    }

    .sale-time .expire .second {
        width: 24px;
        display: inline-block;
        background: #fafafa;
        color: #5e5e5e;
        padding: 6px 0;
        text-align: center;
    }

    .video-tab {
        width: 100%;
        background: #fff;
        margin-bottom: 30px;
        box-shadow: 0 2px 4px 0 #f0f0f0;

    }

    .video-tab .tab-list {
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

    .video-content {
        width: 1200px;
        margin: 0 auto;
        background: #FAFAFA;
        overflow: hidden;
        padding-bottom: 40px;
    }

    .video-tab-list {
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
        white-space:pre-wrap;
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

    .video-side {
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
