from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course

@login_required
def user_courses(request):
    courses = Course.objects.filter(students=request.user)
    return render(request, 'user_courses.html', {'courses': courses})
