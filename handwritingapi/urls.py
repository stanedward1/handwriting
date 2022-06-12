from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('v1/api/admin/', admin.site.urls),
    path('v1/api/home/', include('home.urls')),
    path('v1/api/user/', include('user.urls')),
    path('v1/api/video/', include('video.urls')),
    path('v1/api/culturevideo/', include('culturevideo.urls')),
    path('v1/api/goods/', include('goods.urls')),
    path('v1/api/trade/', include('trade.urls')),
    path('v1/api/docs/', include_docs_urls(title='handwriting project')),
    path('v1/api/openapi/', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
    # 打开media文件夹的路径
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('api-token-auth/', views.obtain_auth_token)
]
