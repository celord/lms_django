from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from lms_local.utils.models import BaseModel

class Course(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses_author')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_student', blank=True)
    tag = models.ManyToManyField('Tag', related_name='courses', blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='courses')
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)


    def __str__(self):
        return self.name

class Class(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes')
    name = models.CharField(max_length=255)
    length = models.DurationField()
    current_time = models.DurationField()
    video_files = models.FileField(upload_to='class_videos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.course.name})"

class Subject(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
