
from rest_framework import serializers
from .models import Department, Teacher, Student, Cources
from datetime import date

class StudentSerializer(serializers.ModelSerializer):
    dep = serializers.StringRelatedField(read_only=True)
    teacher = serializers.StringRelatedField(read_only=True)
    courses = serializers.StringRelatedField(
        source='cources_set', many=True, read_only=True
    )
    age=serializers.SerializerMethodField() 

    class Meta:
        model = Student
        fields = ["id", "name", "age","date_of_birth", "teacher", "dep", "courses"]

    def get_age(self,obj):
        today=date.today()
        dob=obj.date_of_birth 
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))




class StudentResponseSerializer(serializers.ModelSerializer):
    age=serializers.SerializerMethodField() 

    class Meta:
        model = Student
        fields = ["id", "name", "age", "teacher", "dep"]
    def get_age(self,obj):
        today=date.today()  
        dob=obj.date_of_birth 
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

class StudentPOSTserializer(serializers.ModelSerializer):
     teacher=serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all()) 
     dep=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
     courses=serializers.PrimaryKeyRelatedField(queryset=Cources.objects.all(),many=True) 
    
     class Meta:
        model=Student
        fields=["name","age","teacher","dep","courses"] 


    


class TeacherSerializer(serializers.ModelSerializer):
    dep = serializers.StringRelatedField()  
    students = serializers.StringRelatedField(source="student_set", many=True, read_only=True)  

    class Meta:
        model = Teacher
        fields = ["id", "name", "salary", "dep", "students"]
class TeacherPOSTserializer(serializers.ModelSerializer):
    
    dep=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    students=serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),many=True) 

    class Meta:
        model=Teacher
        fields=["name","salary","dep","students"]  




class DepartmentSerializer(serializers.ModelSerializer):
    teachers =serializers.StringRelatedField(source="teacher_set", many=True, read_only=True)  
    students = serializers.StringRelatedField(source="student_set", many=True, read_only=True)  

    class Meta:
        model = Department
        fields = ["id", "name", "teachers", "students"]

class DepartmentPOSTserializer(serializers.ModelSerializer):


    class Meta:
        model = Department
        fields = [ "name"]
 



class CourcesSerializer(serializers.ModelSerializer):
    student= serializers.StringRelatedField(many=True, read_only=True)  
    teacher= serializers.StringRelatedField(many=True, read_only=True)  
    class Meta:
        model = Cources 
        fields = ["id", "course_name", "student", "teacher"] 

class CourcesPOSTserializer(serializers.ModelSerializer):
    
    
    student=serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),many=True) 
    teacher=serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(),many=True)
 
    class Meta:
        model=Cources
        fields=["course_name","teacher","student"]  





