from django.contrib import admin

from .models import Department
from .models import Teacher
admin.site.register(Department)
admin.site.register(Teacher)
from .models import Student
admin.site.register(Student)   
from .models import Cources
admin.site.register(Cources)   

admin.site.site_header = "UNIVERSITY MANAGMENT SYSTEM"
admin.site.site_title = "University Admin Portal"
admin.site.index_title = "Welcome to College Management System"



