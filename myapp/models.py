from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    courses = models.ManyToManyField(
        "Course",
        related_name="students",
        blank=True
    )

    def __str__(self):
        return f"{self.name}--{self.courses}--{self.email}"


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    duration = models.PositiveIntegerField(help_text="Duration in months")
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name