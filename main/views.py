from django.shortcuts import render
from .models import VideoTutorial
from .models import Video, Teacher

def home_view(request):
    return render(request, 'index.html')

def courses_view(request):
    return render(request, 'courses.html')

def teachers_view(request):
    return render(request, 'teachers.html')

def videos_view(request):
    return render(request, 'videos.html')


def register_view(request):
    # Обработка запроса регистрации
    # Возможно, вам нужно проверить метод запроса (GET или POST) и обработать данные формы
    if request.method == 'POST':
        # Обработка данных формы регистрации
        pass
    else:
        # Отображение формы регистрации (GET запрос)
        return render(request, 'register.html')

# def video_tutorial_list(request):
#     video_tutorials = VideoTutorial.objects.all()
#     return render(request, 'main/templates/index.html', {'video_tutorials': video_tutorials})


# views.py

def video_lessons(request):
    videos = Video.objects.all()
    return render(request, 'video_lessons.html', {'videos': videos})

def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})
