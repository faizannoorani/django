
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse, JsonResponse
from rest_framework import status  
from rest_framework.response import Response
    
from django.db.models import Q 
from datetime import date

from django.http import JsonResponse

from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from .models import Department
from .serializers import DepartmentSerializer
from .models import Teacher

from .serializers import TeacherSerializer
from .models import Cources
from .serializers import CourcesSerializer 
from .serializers import StudentPOSTserializer
from .serializers import TeacherPOSTserializer
from .serializers import DepartmentPOSTserializer
from .serializers import CourcesPOSTserializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Teacher, Department, Cources
from .serializers import StudentSerializer, TeacherSerializer, DepartmentSerializer, CourcesSerializer, StudentResponseSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])

def Student_data(request,id=None): 
 if request.method=='GET':
     name=request.GET.get('name')
     age=request.GET.get('age')
     stu=Student.objects.select_related("dep","teacher").prefetch_related("cources_set").all()
     if name :
        stu=stu.filter(name=name) 
     if age:
        stu=stu.filter(age=age) 
    
     serializer=StudentSerializer(stu,many=True)
     return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
 elif request.method=='POST':
    stu=StudentSerializer(data=request.data)
    if stu.is_valid(): 
       teacher_obj = Teacher.objects.filter(id=request.data.get('teacher')).first() 
       depart_obj = Department.objects.filter(id=request.data.get('dep')).first()
       response = Student.objects.create(name=stu.validated_data.get('name'), 
                              date_of_birth=stu.validated_data.get('date_of_birth'),
                              dep=depart_obj,
                              teacher=teacher_obj      
                              )         
       serialized_data = StudentResponseSerializer(response).data
       return JsonResponse(serialized_data, status=status.HTTP_201_CREATED, safe=False)
    
    return  JsonResponse(stu.errors,status=status.HTTP_400_BAD_REQUEST) 
 
 
 elif request.method=='PUT':
    stu=Student.objects.get(id=id)
    serializer=StudentPOSTserializer(stu,data=request.data) 
    if serializer.is_valid():
       serializer.save()
       return JsonResponse(serializer.data,safe=False,status=status.HTTP_202_ACCEPTED) 
    return JsonResponse(serializer.errors,status=status.HTTP_401_UNAUTHORIZED) 
 

 elif request.method=='PATCH':
    stu=Student.objects.get(id=id)
    serializer=StudentPOSTserializer(stu,data=request.data,partial=True) 
    if serializer.is_valid():
       serializer.save()
       return JsonResponse(serializer.data,safe=False,status=status.HTTP_202_ACCEPTED) 
    return JsonResponse(serializer.errors,status=status.HTTP_401_UNAUTHORIZED) 
 
 elif request.method=='DELETE':
    try:
     stu=Student.objects.get(id=id) 
    
     stu.delete()
     return JsonResponse({'message':'DELETED SUCCESFULLY'},status=status.HTTP_200_OK)
    except Student.DoesNotExist:
     return JsonResponse({'error':'STUDENT DOES NOT EXIST'},status=status.HTTP_400_BAD_REQUEST) 


 


 ##                 TEACHER DETAILS
 
 

@api_view(['GET','POST','PUT','PATCH','DELETE'])

def teacher_detail(request,id=None):  
 if request.method=='GET':
     name=request.GET.get('name')
     salary=request.GET.get('salary')
     teacher=Teacher.objects.select_related("dep").prefetch_related("student_set").all()
     if name :
        teacher=teacher.filter(name=name) 
     if salary:
        teacher=teacher.filter(salary__gte=salary)
    
     serializer=TeacherSerializer(teacher,many=True)

     return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
    

 elif request.method=='POST':
     teacher=TeacherPOSTserializer(data=request.data)
     if teacher.is_valid():
       teacher.save()
       return JsonResponse(teacher.data,status=status.HTTP_201_CREATED)
    
     return  JsonResponse(teacher.errors,status=status.HTTP_400_BAD_REQUEST) 

 elif request.method=='PUT':
    teacher=Teacher.objects.get(id=id)
    serializer=TeacherPOSTserializer(teacher,data=request.data) 
    if serializer.is_valid():
       serializer.save()
       return JsonResponse(serializer.data,safe=False,status=status.HTTP_202_ACCEPTED) 
    return JsonResponse(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
 
 elif request.method=='PATCH':
    teacher =Teacher.objects.get(id=id)
    serializer=TeacherPOSTserializer(teacher ,data=request.data,partial=True) 
    if serializer.is_valid():
       serializer.save()
       return JsonResponse(serializer.data,safe=False,status=status.HTTP_202_ACCEPTED) 
    return JsonResponse(serializer.errors,status=status.HTTP_401_UNAUTHORIZED) 
 elif request.method=='DELETE':
    try:
     teacher=Teacher.objects.get(id=id) 
     
     teacher.delete()
     return JsonResponse({'message':'DELETED SUCCESFULLY'},status=status.HTTP_200_OK)
    except Teacher.DoesNotExist:
     return JsonResponse({'error':'Teacher  DOES NOT  EXIST'},status=status.HTTP_400_BAD_REQUEST) 



    
##                 DEPARTMENT DETAILS

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def department_detail(request,id=None):
    if request.method == 'GET':
        name=request.GET.get('name')
        department = Department.objects.prefetch_related("teacher_set","student_set").all()
        if name :
         department=department.filter(name=name)

        serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DepartmentPOSTserializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PUT':
     department=Department.objects.get(id=id)
     serializer=DepartmentPOSTserializer(department,data=request.data) 
     if serializer.is_valid():
       serializer.save()
       return JsonResponse(serializer.data,safe=False,status=status.HTTP_202_ACCEPTED) 
     return JsonResponse(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)

    elif request.method=='PATCH':
      department =Department.objects.get(id=id)
      serializer=DepartmentPOSTserializer(department,data=request.data,partial=True) 
      if serializer.is_valid():
       serializer.save()
       return JsonResponse(serializer.data,safe=False,status=status.HTTP_202_ACCEPTED) 
      return JsonResponse(serializer.errors,status=status.HTTP_401_UNAUTHORIZED) 
    
    elif request.method=='DELETE':
     try:
       department=Department.objects.get(id=id) 
    
       department.delete()
       return JsonResponse({'message':'DELETED SUCCESFULLY'},status=status.HTTP_200_OK)
     except Department.DoesNotExist:
      return JsonResponse({'error':'department  DOES NOT EXIST'},status=status.HTTP_400_BAD_REQUEST) 

       
    


  ##                     COURCES DETAILS 
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def courses_detail(request,id=None):
    if request.method == 'GET':
        course_name=request.GET.get('course_name')
        courses = Cources.objects.prefetch_related("student","teacher").all()
        if course_name:
           courses=courses.filter(course_name=course_name)
        serializer = CourcesSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CourcesPOSTserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PUT':
       courses=Cources.objects.get(id=id)
       serializer=CourcesPOSTserializer(courses,data=request.data) 
       if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_202_ACCEPTED) 
       return JsonResponse(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
       
    
    elif request.method=='PATCH':
        courses =Cources.objects.get(id=id)
        serializer=CourcesPOSTserializer(courses,data=request.data,partial=True) 
        if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data,safe=False,status=status.HTTP_202_ACCEPTED) 
        return JsonResponse(serializer.errors,status=status.HTTP_401_UNAUTHORIZED) 
    
    elif request.method=='DELETE':
     try:
      courses=Cources.objects.get(id=id) 
    
      courses.delete()
      return JsonResponse({'message':'DELETED SUCCESFULLY'},status=status.HTTP_200_OK)
     except Cources.DoesNotExist:
      return JsonResponse({'error':'course DOES NOT EXIST'},status=status.HTTP_400_BAD_REQUEST) 

       
