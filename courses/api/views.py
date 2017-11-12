# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route
from .serializers import SubjectSerializer, CourseSerializer
from ..models import Course, Subject 
from .permissions import IsEnrolled
from .serializers import CourseWithContentsSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

'''
class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, id, format=None):
        course = get_object_or_404(Course, id=id)
        course.students.add(request.user)
        return Response({'enrolled': True})
'''

class CourseViewSet(viewsets.ReadOnlyModelViewSet):  #contains list() and retrieve()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    @detail_route(methods=['post'], authentication_classes=[BasicAuthentication],
                  permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})
    #detail_route装饰器指定这个类是一个在单独对象上执行的操作

    @detail_route(methods=['get'],
                  serializer_class=CourseWithContentsSerializer,
                  authentication_classes=[BasicAuthentication],
                  permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)