from django.contrib import admin
from .models import Video, Teacher, CustomUser

# Register your models here.
admin.site.register(Video)
admin.site.register(Teacher)
admin.site.register(CustomUser)