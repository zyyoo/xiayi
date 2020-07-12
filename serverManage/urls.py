"""
@ Author : zdoubley 
@ Date : 2020/7/4
@ Usage: 
"""

from django.urls import path
from serverManage import views

app_name = 'ServerManage'
urlpatterns = [
    path('domain/', views.ServerInfo.as_view()),
]