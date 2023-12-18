from django.db import models

class VideoTutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.title
    
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