from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/',views.LCSchoolApi.as_view()),
    path('school/<int:pk>/',views.RUDSchoolApi.as_view()),
    path('classes/',views.LCClasssesApi.as_view()),
    path('classes/<int:pk>/',views.RUDClassesApi.as_view()),
    path('department/',views.LCDepartmentApi.as_view()),
    path('department/<int:pk>/',views.RUDDepartmentApi.as_view()),
    path('designation/',views.LCDesignationApi.as_view()),
    path('designation/<int:pk>/',views.RUDDesignationApi.as_view()),
    path('staff/',views.LCStaffApi.as_view()),
    path('staff/<int:pk>/',views.RUDStaffApi.as_view()),
    path('section/',views.LCSectionApi.as_view()),
    path('section/<int:pk>/',views.RUDSectionApi.as_view()),
    path('student/',views.LCStudentApi.as_view()),
    path('student/<int:pk>/',views.RUDStudentApi.as_view()),
    path('syllabus/',views.LCSyllabusApi.as_view()),
    path('syllabus/<int:pk>/',views.RUDSyllabusApi.as_view()),
]
