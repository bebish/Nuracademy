from django.urls import path
from .views import *
from .views import video_lessons
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home_view, name='home'),
    path('/courses', courses_view, name='courses'),
    path('/teachers', teachers_view, name='teachers'),
    path('/videos', videos_view, name='videos'),
    path('register/', register_view, name='register'),
    path('video_lessons/', video_lessons, name='video_lessons')

    # path('video_tutorials/', video_tutorial_list, name='video_tutorial_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)