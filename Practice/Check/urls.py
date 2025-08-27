
from . import views



from .views import Student_data
from .views import teacher_detail
from .views import department_detail
from .views import courses_detail

from django.urls import path
from .views import *

urlpatterns = [
    path("student/",Student_data),
    path("student/<int:id>/",Student_data),
    path("teacher/",teacher_detail),
    path("teacher/<int:id>/",teacher_detail),
    path("department/",department_detail),
    path("department/<int:id>/",department_detail),
    
    path("courses/",courses_detail),
    path("courses/<int:id>/",courses_detail),
]
