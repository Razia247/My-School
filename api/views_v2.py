from django.shortcuts import render
from .models import  School,Classes,Syllabus,Department,Staff,Student,Designation,Section
from .serializers import SchoolSerializer,ClassesSerializer,SyllabusSerializer,DepartmentSerializer,StaffSerializer,StudentSerializer,DesignationSerializer,SectionSerializer
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.views import APIView

class SchoolApi1(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
class SchoolApi2(RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class Classes1(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class Classes2(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Syllabus1(ListCreateAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
class Syllabus2(RetrieveUpdateDestroyAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer 

class Department1(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
class Department2(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class Staff1(ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
class Staff2(RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class Section1(ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
class Section2(RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class Student1(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class Student2(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Designation1(ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
class Designation2(RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
