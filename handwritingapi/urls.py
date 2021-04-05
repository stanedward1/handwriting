from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('course/', include('course.urls')),
    # 打开media文件夹的路径
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
