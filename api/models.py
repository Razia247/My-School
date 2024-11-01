from django.db import models

# Create your models here.
class School(models.Model):
    bank_account_choices = [
        ('HBL','HBL'),('UBL','UBL'),('MCB','MCB'),('MEEZAN','MEEZAN'),('ALFALAH','ALFALAH')
    ]
    name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11,unique=True)
    country = models.CharField(max_length=50)
    province_or_state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=50,choices=bank_account_choices)

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=20)
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=20)
    classes= models.ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Syllabus(models.Model):
    name = models.CharField(max_length=30)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=30)
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    post_name = models.CharField(max_length=50)
    qualification_required = models.CharField(max_length=100)
    job_description = models.CharField(max_length=150)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.post_name
    
class Staff(models.Model):
    gender_choice = [
        ('M','MALE'),('F','FEMALE')
    ]
    blood_group_choice = [
        ('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-')
    ] 
    marital_status_choice = [
        ('SINGLE','SINGLE'),('MARRIED','MARRIED'),('DIVORCED','DIVORCED'),('WIDOW','WIDOW')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    cnic = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=30,unique=True)
    gender = models.CharField(max_length=10,choices=gender_choice)
    marital_status = models.CharField(max_length=10,choices=marital_status_choice)
    blood_group = models.CharField(max_length=30,choices=blood_group_choice)
    address = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,null=True,blank=True)
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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    gender_choice = [
        ('M','MALE'),('F','FEMALE')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=gender_choice)
    previous_registration = models.CharField(max_length=50)
    new_registration = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=50)
    province_or_state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    