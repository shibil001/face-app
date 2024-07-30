from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Department(models.Model):
    DepartmentName=models.CharField(max_length=100)


class Course(models.Model):

    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE)
    CourseName=models.CharField(max_length=100)
    TotalSem = models.CharField(max_length=100)

class Subject(models.Model):
    COURSE=models.ForeignKey(Course,on_delete=models.CASCADE)
    SubjectName=models.CharField(max_length=100)
    Semester=models.CharField(max_length=100)

class Student(models.Model):

    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    COURSE=models.ForeignKey(Course,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Image=models.CharField(max_length=250)
    Gender=models.CharField(max_length=100)
    DOB=models.DateField()
    Pin=models.IntegerField()
    Post=models.CharField(max_length=100)
    Phone=models.BigIntegerField()
    HouseName=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    ParentName=models.CharField(max_length=100)
    ParentPhone=models.BigIntegerField()
    Email = models.CharField(max_length=100)
    Sem = models.CharField(max_length=100,default="1")

class Timetable(models.Model):
    SUBJECT=models.ForeignKey(Subject,on_delete=models.CASCADE)
    Day=models.CharField(max_length=100)
    Hour=models.CharField(max_length=100)

class Attendance(models.Model):
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    Time=models.TimeField()
    Date=models.DateField()
    Attendance=models.CharField(max_length=100, default='Present')
    Hour=models.CharField(max_length=100)



