from django.contrib import admin
from .models import Videos,Question,Choice,Exam
# Register your models here.

admin.site.register(Videos)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Exam)
