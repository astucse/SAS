from django.contrib import admin
from .models import Video,Question,Choice,Exam,Slide,Handout
# Register your models here.

admin.site.register(Video)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Exam)
admin.site.register(Slide)
admin.site.register(Handout)
