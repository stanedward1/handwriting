from django.contrib import admin
from video import models

admin.site.register(models.Video)
admin.site.register(models.VideoCategory)
admin.site.register(models.VideoChapter)
admin.site.register(models.VideoSection)
admin.site.register(models.Organization)
