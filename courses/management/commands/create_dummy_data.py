# courses/management/commands/create_dummy_data.py
import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from courses.models import Course, Class, Subject, Tag
from datetime import timedelta
from faker import Faker

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Create dummy data for courses app'

    def handle(self, *args, **kwargs):
        self.clear_data()
        self.create_subjects()
        self.create_tags()
        self.create_users()
        self.create_courses()
        self.create_classes()

    def clear_data(self):
        Class.objects.all().delete()
        Course.objects.all().delete()
        Subject.objects.all().delete()
        Tag.objects.all().delete()
        User.objects.filter(email__endswith='@example.com').delete()
        self.stdout.write(self.style.SUCCESS('Data cleared'))

    def create_subjects(self):
        subjects = ['Python', 'Java', 'Scala', 'Javascript', 'Music']
        for name in subjects:
            Subject.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Subjects created'))

    def create_tags(self):
        tags = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
        for name in tags:
            Tag.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Tags created'))

    def create_users(self):
        for _ in range(10):
            User.objects.get_or_create(
                name=fake.name(),
                defaults={'email': fake.email(), 'password': 'password'}
            )
        self.stdout.write(self.style.SUCCESS('Users created'))

    def create_courses(self):
        subjects = list(Subject.objects.all())
        users = list(User.objects.all())
        tags = list(Tag.objects.all())
        for _ in range(10):
            course_name = fake.sentence(nb_words=3)
            course = Course.objects.create(
                name=course_name,
                description=fake.text(),
                publication_date=now(),
                author=random.choice(users),
                slug=slugify(course_name),
                subject=random.choice(subjects)
            )
            course.tag.set(random.sample(tags, k=random.randint(1, len(tags))))
            course.students.set(random.sample(users, k=random.randint(1, len(users))))
        self.stdout.write(self.style.SUCCESS('Courses created'))

    def create_classes(self):
        courses = list(Course.objects.all())
        for course in courses:
            for _ in range(5):
                Class.objects.create(
                    course=course,
                    name=fake.sentence(nb_words=4),
                    length=timedelta(minutes=random.randint(10, 20)),
                    current_time=timedelta(minutes=random.randint(10, 20))
                )
        self.stdout.write(self.style.SUCCESS('Classes created'))
