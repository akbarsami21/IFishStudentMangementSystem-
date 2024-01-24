from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['student_number','first_name','last_name','email','field_of_study','gpa']
    search_fields=['first_name','last_name']
    list_filter=['student_number']


