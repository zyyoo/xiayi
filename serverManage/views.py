from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import serializers
from serverManage.models import DbServerInfo
from Util.Response import BaseResponse


# Create your views here.

def server_html(request):
    return render(request,'ServerManage/index.html')


class ServerInfo(APIView):
    def get(self, request):
        res = BaseResponse()
        info = request.GET.get('info', '').strip()
        if ',' in info:
            info = info.split(',')
            print(info)
        if info:
            if isinstance(info,str):
                info_obj = DbServerInfo.objects.filter(Q(domain__icontains=info) | Q(user__icontains=info)).values()[:100]
            else:
                info_obj = DbServerInfo.objects.filter(Q(domain__in=info) | Q(user__in=info)).values()[
                           :100]
            if info_obj:
                for i in info_obj:
                    res.data.append(i)
            else:
                res.msg = '请求信息为空..'
        else:
            info_obj = DbServerInfo.objects.values()
            if info_obj:
                for i in info_obj:
                    res.data.append(i)
        #print(res.dict())
        return JsonResponse(res.dict())