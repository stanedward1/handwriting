from django.shortcuts import render

# Create your views here.

from user import models
from rest_framework.views import APIView
from handwritingapi.utils.response import APIResponse
from handwritingapi.utils.logger import logger


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        # logger.info('xxxxx')
        dic = {'name': 'lqa'}
        print('xxxxx')
        return APIResponse(headers={'Access-Control-Allow-Origin':'*'})
