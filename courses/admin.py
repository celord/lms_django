from django.contrib import admin
from .models import Course, Class, Subject, Tag
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "publication_date", "author"]

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ["name", "course", "length"]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
