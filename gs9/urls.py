from django.contrib import admin
from django.urls import path
from api import views_v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/',views_v2.SchoolApi1.as_view()),
    path('school/<int:pk>/',views_v2.SchoolApi2.as_view()),
    path('classes/',views_v2.Classes1.as_view()),
    path('classes/<int:pk>/',views_v2.Classes2.as_view()),
    path('department/',views_v2.Department1.as_view()),
    path('department/<int:pk>/',views_v2.Department2.as_view()),
    path('designation/',views_v2.Designation1.as_view()),
    path('designation/<int:pk>/',views_v2.Designation2.as_view()),
    path('staff/',views_v2.Staff1.as_view()),
    path('staff/<int:pk>/',views_v2.Staff2.as_view()),
    path('section/',views_v2.Section1.as_view()),
    path('section/<int:pk>/',views_v2.Section2.as_view()),
    path('student/',views_v2.Student1.as_view()),
    path('student/<int:pk>/',views_v2.Student2.as_view()),
    path('syllabus/',views_v2.Syllabus1.as_view()),
    path('syllabus/<int:pk>/',views_v2.Syllabus2.as_view()),
]
