from django.contrib.auth.models import User, Group
from rest_framework import serializers

import time

from course.models import Classroom,ClassroomOrder


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ClassroomOrderSerializer(serializers.HyperlinkedModelSerializer):
    classroom = serializers.SerializerMethodField()
    class Meta:
        model = ClassroomOrder
        fields = ['classroom','usage_user','usage_curricula','usage_start_time', 'usage_end_time']
    def get_classroom(self,obj):
        return obj.classroom.room_number

class ClassroomSerializer(serializers.HyperlinkedModelSerializer):
    occupation_time = serializers.SerializerMethodField()
    class Meta:
        model = Classroom
        fields = ['room_number','room_address', 'room_load','occupation_time']

    def get_occupation_time(self, obj):
        data = obj.orders.all()
        return  [{"usage_start_time":  order.usage_start_time.strftime('%Y-%m-%d %H:%M:%S') , "usage_end_time": order.usage_end_time.strftime('%Y-%m-%d %H:%M:%S') } for order in data]
