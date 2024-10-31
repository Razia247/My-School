from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=50)
    school_owner_name = models.CharField(max_length=50)
    school_email = models.EmailField(unique=True)
    school_phone_number = models.CharField(max_length=11,unique=True)
    country = models.CharField(max_length=50)
    province_or_state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    school_address = models.CharField(max_length=100)
    school_bank_account = models.CharField(max_length=50)

    def __str__(self):
        return self.school_name

class Classes(models.Model):
    class_name = models.CharField(max_length=20)
    school_name = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.class_name

class Section(models.Model):
    section_name = models.CharField(max_length=20)
    class_name = models.ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.section_name
    
class Syllabus(models.Model):
    syllabus_name = models.CharField(max_length=30)
    class_name = models.ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)
    section_name = models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)
    school_name = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.syllabus_name
    
class Department(models.Model):
    department_name = models.CharField(max_length=30)

    def __str__(self):
        return self.department_name

class Designation(models.Model):
    post_name = models.CharField(max_length=50)
    qualification_required = models.CharField(max_length=100)
    job_description = models.CharField(max_length=150)
    department_name = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.post_name
    
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    cnic = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=30,unique=True)
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    department_name = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    post_name = models.ForeignKey(Designation,on_delete=models.CASCADE,null=True,blank=True)
    date_of_joining =models.DateField()
    country = models.CharField(max_length=50)
    province_or_state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    basic_monthly_salary = models.IntegerField()
    medical_allowance = models.IntegerField()
    rent_allowance = models.IntegerField()
    transport_allowance = models.IntegerField()
    syllabus = models.ForeignKey(Syllabus,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    previous_registration = models.CharField(max_length=50)
    new_registration = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=50)
    province_or_state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    class_name = models.ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)
    section_name = models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    