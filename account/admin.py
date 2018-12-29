from django.contrib import admin
from .models import School,Department,Student,Teacher,Subject

# Register your models here.
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
