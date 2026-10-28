
from django.urls import path
from .views import (
    CourseListCreateView,
    CourseDetailView,
    StudentListCreateView,
    StudentDetailView,
    StudentCourses,
    StudentByCourseAPIView,
    StudentFilterAPIView
)

urlpatterns = [
    # Course URLs
    path("courses/", CourseListCreateView.as_view()),
    path("courses/<int:pk>/", CourseDetailView.as_view()),

    # Student URLs
    path("students/", StudentListCreateView.as_view()),
    path("students/<int:pk>/", StudentDetailView.as_view()),
    path('students/courses/',StudentCourses.as_view()),
    path('students/filter/',StudentFilterAPIView.as_view())
]
