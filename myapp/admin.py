from django.contrib import admin
from .models import Student
# Register your models here.

class StudentList(admin.ModelAdmin):
    list_display = ('Student_ID','Student_Name','Student_Class','Student_Section','Student_Age','Student_Sex')



admin.site.register(Student, StudentList)