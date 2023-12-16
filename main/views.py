from django.shortcuts import render
from .models import VideoTutorial

def home_view(request):
    return render(request, 'index.html')

def courses_view(request):
    return render(request, 'courses.html')

def teachers_view(request):
    return render(request, 'teachers.html')

def videos_view(request):
    return render(request, 'videos.html')

# def video_tutorial_list(request):
#     video_tutorials = VideoTutorial.objects.all()
#     return render(request, 'main/templates/index.html', {'video_tutorials': video_tutorials})
