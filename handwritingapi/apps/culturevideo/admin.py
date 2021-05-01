from django.contrib import admin
from culturevideo import models

admin.site.register(models.Video)
admin.site.register(models.CultureVideoCategory)
admin.site.register(models.CultureVideoChapter)
admin.site.register(models.CultureVideoSection)
admin.site.register(models.Organization)
