from django.shortcuts import render, redirect
from .models import Video, Teacher
from .forms import CustomUserForm

def home_view(request):
    return render(request, 'index.html')

def courses_view(request):
    return render(request, 'courses.html')

def teachers_view(request):
    return render(request, 'teachers.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('register_success')  # Перенаправление на страницу успешной регистрации
    else:
        form = CustomUserForm()

    return render(request, 'register.html', {'form': form})

def video_lessons(request):
    videos = Video.objects.all()
    return render(request, 'video_lessons.html', {'videos': videos})

def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})


def register_success(request):
    return render(request, 'register_success.html')