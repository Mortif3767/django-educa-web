from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import SubjectSerializer
from ..models import Course, Subject 


class SubjectListView(generics.ListAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)
	def post(self, request, id, format=None):
		course = get_object_or_404(Course, id=id)
		course.students.add(request.user)
		return Response({'enrolled': True})