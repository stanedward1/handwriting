from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('video/', include('video.urls')),
    path('goods/', include('goods.urls')),
    path('trade/', include('trade.urls')),
    path('openapi/', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
    # 打开media文件夹的路径

    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        # path('api-token-auth/', views.obtain_auth_token)
]
