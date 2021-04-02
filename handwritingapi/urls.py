from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # 打开media文件夹的路径
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_URL}),
]
