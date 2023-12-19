from django.contrib import admin
from .models import Video, Teacher, CustomUser, Courses

# Register your models here.
admin.site.register(Video)
admin.site.register(Teacher)
admin.site.register(CustomUser)
admin.site.register(Courses)