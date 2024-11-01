from django.shortcuts import render
from .models import  School,Classes,Syllabus,Department,Staff,Student,Designation,Section
from .serializers import SchoolSerializer,ClassesSerializer,SyllabusSerializer,DepartmentSerializer,StaffSerializer,StudentSerializer,DesignationSerializer,SectionSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.
from rest_framework import status
from rest_framework.response import Response

class LCSchoolApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUDSchoolApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class LCClasssesApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUDClassesApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class LCDepartmentApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUDDepartmentApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class LCDesignationApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUDDesignationApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class LCStaffApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUDStaffApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class LCStudentApi(GenericAPIView):
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    # lookup_field = 'pk'
    def get(self,request,*args,**kwargs):
        std = self.request.GET.get('std', 0)
        try:
            student_obj = Student.objects.get(id=std)
        except Student.DoesNotExist:
            return Response({"error": "student not found"})

        data = {
            "id": student_obj.id,
            "name": student_obj.first_name,
            "city": student_obj.city
        }
        return Response(data)


class RUDStudentApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class LCSectionApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUDSectionApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class LCSyllabusApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUDSyllabusApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)




