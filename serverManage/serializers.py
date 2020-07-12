"""
@ Author : zdoubley 
@ Date : 2020/7/11
@ Usage: 
"""
from rest_framework import serializers
from serverManage.models import DbServerInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DbServerInfo
        fields = ('domain', 'ip', 'user', 'user_type')
