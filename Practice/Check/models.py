from django.db import models
from datetime import datetime 



class Department(models.Model):
    name = models.CharField(max_length=40)
    
    class Meta:
        db_table = "Department" 

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    salary = models.CharField(max_length=40)
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Teacher" 

    def __str__(self):
        return self.name


class Student(models.Model): 
    name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(default=datetime(2000, 1, 1))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    dep = models.ForeignKey(Department, on_delete=models.CASCADE) 
    

    class Meta:
        db_table = "Student" 
    
    def __str__(self):
        return self.name           
    


class Cources(models.Model):
    course_name = models.CharField(max_length=40)
    student = models.ManyToManyField(Student, blank=True)
    teacher = models.ManyToManyField(Teacher, blank=True)
       
    class Meta:
        db_table = "Cources"

    def __str__(self):
        return self.course_name              
