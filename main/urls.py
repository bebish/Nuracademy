from django.urls import path
from .views import *
from .views import video_lessons, register_view, register_success
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home_view, name='home'),
    path('/courses', courses_view, name='courses'),
    path('/teachers', teachers_list, name='teachers'),
    path('register/', register_view, name='register'),
    path('video_lessons/', video_lessons, name='video_lessons'),
    path('register_success/', register_success, name='register_success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)