# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ClassroomSerializer,ClassroomOrderSerializer
from course.models import Classroom,ClassroomOrder

from .filters import ClassroomFilter


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated,]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [IsAuthenticated,]


class ClassroomViewSet(viewsets.ModelViewSet):
    """
    课室列表
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    authentication_classes = [BasicAuthentication,JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated,]

    filter_backends = (DjangoFilterBackend,)
    filter_class = ClassroomFilter

class ClassroomOrderViewSet(viewsets.ModelViewSet):
    """
    已预约课室列表
    """
    queryset = ClassroomOrder.objects.all()
    serializer_class = ClassroomOrderSerializer
    authentication_classes = [BasicAuthentication,JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated,]