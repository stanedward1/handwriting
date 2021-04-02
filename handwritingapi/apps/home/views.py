from django.shortcuts import render

# Create your views here.

from user import models
from rest_framework.views import APIView
from handwritingapi.utils.response import APIResponse


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        dic = {'name': 'lqa'}
        print(dic['age'])
        return
