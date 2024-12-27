# courses/urls.py
from django.urls import path
from .views import user_courses

app_name = 'courses'
urlpatterns = [
    path('my-courses/', user_courses, name='user_courses'),
]
