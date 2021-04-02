from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/',views.TestView.as_view())
]
