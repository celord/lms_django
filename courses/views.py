from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course, Subject
from django.contrib.auth import get_user_model


@login_required
def user_courses(request):
    user = request.user

    courses = Course.objects.filter(students=user)

    instructors = get_user_model().objects.filter(courses_author__in=courses)
    subjects = Subject.objects.filter(courses__in=courses)

    instructor_id = request.GET.get("instructor")
    subject_id = request.GET.get("subject")

    if instructor_id:
        courses = courses.filter(author=instructor_id)
    if subject_id:
        courses = courses.filter(subject=subject_id)

    return render(
        request,
        "user_courses.html",
        {"courses": courses, "instructors": instructors, "subjects": subjects},
    )
