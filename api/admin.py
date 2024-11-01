from django.contrib import admin
from .models import School,Classes,Syllabus,Department,Staff,Student,Designation,Section
# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','name','owner_name','email','phone_number','country','province_or_state','city','bank_account','address']

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['id','name','section']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name','school']

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['id','name','school']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','father_name','cnic','gender','marital_status','blood_group','email','date_of_birth','phone','address','department','designation','date_of_joining','zip_code','country','province_or_state','city','qualification','experience','basic_monthly_salary','medical_allowance','rent_allowance','transport_allowance']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =  ['id','first_name','last_name','father_name','gender','previous_registration','new_registration','email','contact_number','date_of_birth','zip_code','country','province_or_state','city','section']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id','classes','name']

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ['id','department','post_name','qualification_required','job_description']