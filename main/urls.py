from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('/courses', courses_view, name='courses'),
    path('/teachers', teachers_view, name='teachers'),
    path('/videos', videos_view, name='videos'),
    # path('video_tutorials/', video_tutorial_list, name='video_tutorial_list'),
]
