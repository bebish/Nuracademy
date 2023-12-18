from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    number = models.CharField(max_length=13)
    check_photo = models.ImageField(upload_to='check_photos/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'