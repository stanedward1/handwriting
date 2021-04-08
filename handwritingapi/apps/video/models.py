from django.db import models

# Create your models here.
from utils.models import BaseModel


class VideoCategory(BaseModel):
    """分类"""
    name = models.CharField(max_length=64, unique=True, verbose_name="视频分类")

    class Meta:
        db_table = "video_category"
        verbose_name = "视频分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    """视频教程"""
    name = models.CharField(max_length=128, verbose_name="视频名称")
    video_img = models.ImageField(upload_to="video", max_length=255, verbose_name="封面图片", blank=True, null=True)
    brief = models.TextField(max_length=2048, verbose_name="详情介绍", null=True, blank=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    attachment_path = models.FileField(upload_to="attachment", max_length=128, verbose_name="附件路径", blank=True,
                                       null=True)
    video_category = models.ForeignKey("VideoCategory", on_delete=models.SET_NULL, db_constraint=False, null=True,
                                       blank=True,
                                       verbose_name="视频分类")
    students = models.IntegerField(verbose_name="学习人数", default=0)
    sections = models.IntegerField(verbose_name="总课时数量", default=0)
    pub_sections = models.IntegerField(verbose_name="视频更新数量", default=0)
    organization = models.ForeignKey("Organization", on_delete=models.DO_NOTHING, null=True, blank=True,
                                     verbose_name="机构或个人名称")

    class Meta:
        db_table = "video_video"
        verbose_name = "视频"
        verbose_name_plural = "视频"

    @property
    def video_section(self):
        ll = []
        # 根据课程取出所有章节
        video_chapter_list = self.videochapters.all()
        for video_chapter in video_chapter_list:
            video_sections_list = video_chapter.videosections.all()
            for video_sections in video_sections_list:
                ll.append({
                    'name': video_sections.name,
                    'link': video_sections.section_link,
                    'section_type': video_sections.section_type,
                    'duration': video_sections.duration,
                    'pub_date': video_sections.pub_date,
                })
                if len(ll) >= 6:
                    return ll
        return ll

    def __str__(self):
        return self.name


class CultureVideo(BaseModel):
    """文化趣事视频"""
    name = models.CharField(max_length=128, verbose_name="文化趣事视频名称")
    video_img = models.ImageField(upload_to="video", max_length=255, verbose_name="封面图片", blank=True, null=True)
    brief = models.TextField(max_length=2048, verbose_name="详情介绍", null=True, blank=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    attachment_path = models.FileField(upload_to="attachment", max_length=128, verbose_name="附件路径", blank=True,
                                       null=True)
    # 暂定2类，书法教程和文化趣事视频
    video_category = models.ForeignKey("VideoCategory", on_delete=models.SET_NULL, db_constraint=False, null=True,
                                       blank=True,
                                       verbose_name="视频分类")
    students = models.IntegerField(verbose_name="观看人数", default=0)
    sections = models.IntegerField(verbose_name="总课时数量", default=0)
    pub_sections = models.IntegerField(verbose_name="视频更新数量", default=0)
    organization = models.ForeignKey("Organization", on_delete=models.DO_NOTHING, null=True, blank=True,
                                     verbose_name="机构或个人名称")

    class Meta:
        db_table = "video_culture"
        verbose_name = "文化趣事视频名称"
        verbose_name_plural = "文化趣事视频名称"

    def __str__(self):
        return self.name


class Organization(BaseModel):
    """机构或个人名称"""
    name = models.CharField(max_length=32, verbose_name="机构或个人名称")
    signature = models.CharField(max_length=255, verbose_name="机构或个人签名", help_text="机构或个人签名", blank=True, null=True)
    image = models.ImageField(upload_to="teacher", null=True, verbose_name="机构或个人自选封面")
    brief = models.TextField(max_length=1024, verbose_name="机构或个人描述")

    class Meta:
        db_table = "video_organization"
        verbose_name = "机构或个人名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VideoChapter(BaseModel):
    """视频章节"""
    video = models.ForeignKey("Video", related_name='videochapters', on_delete=models.CASCADE, verbose_name="视频名称")
    chapter = models.SmallIntegerField(verbose_name="章节排序", default=1)
    name = models.CharField(max_length=128, verbose_name="章节标题")
    summary = models.TextField(verbose_name="章节介绍", blank=True, null=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)

    class Meta:
        db_table = "video_chapter"
        verbose_name = "视频章节名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VideoSection(BaseModel):
    """每个小节"""
    section_type_choices = (
        (0, '文档'),
        (1, '视频')
    )
    chapter = models.ForeignKey("VideoChapter", related_name='videosections', on_delete=models.CASCADE,
                                verbose_name="视频章节")
    name = models.CharField(max_length=128, verbose_name="小节标题")
    orders = models.PositiveSmallIntegerField(verbose_name="小节排序")
    section_type = models.SmallIntegerField(default=1, choices=section_type_choices, verbose_name="小节种类")
    section_link = models.CharField(max_length=255, blank=True, null=True, verbose_name="小节链接",
                                    help_text="若是video，填vid,若是文档，填link")
    duration = models.CharField(verbose_name="视频时长", blank=True, null=True, max_length=32)  # 仅在前端展示使用
    pub_date = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)

    class Meta:
        db_table = "video_Section"
        verbose_name = "小节标题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.chapter, self.name)

    @property
    def section_type_name(self):
        return self.get_section_type_display()
