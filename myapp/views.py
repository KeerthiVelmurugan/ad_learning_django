from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Course
from datetime import date

# # Create your views here.
# def create_data(request):
#     python_course = Course.objects.create(
#         course_name="Python Full Stack",
#         course_code="PY101",
#         duration=6,
#         fee=25000,
#         level="Intermediate",
#         description="Python, Django, REST API and MySQL",
#         start_date=date(2026, 11, 1),
#         end_date=date(2027, 4, 30),
#         is_available=True
#     )
#     django_course = Course.objects.create(
#         course_name="Django REST Framework",
#         course_code="DJ201",
#         duration=3,
#         fee=15000,
#         level="Advanced",
#         description="Building REST APIs using Django REST Framework",
#         start_date=date(2026, 11, 1),
#         end_date=date(2027, 1, 31),
#         is_available=True
#     )
#     react_course = Course.objects.create(
#         course_name="React JS",
#         course_code="RE101",
#         duration=4,
#         fee=18000,
#         level="Intermediate",
#         description="React components, hooks and routing",
#         start_date=date(2026, 11, 1),
#         end_date=date(2027, 2, 28),
#         is_available=True
#     )
#     student1 = Student.objects.create(
#         name="Arun",
#         email="arun@example.com",
#         phone="9876543210",
#         age=22,
#         gender="Male",
#         city="Coimbatore",
#         qualification="B.E",
#         is_active=True
#     )

#     student2 = Student.objects.create(
#         name="Priya",
#         email="priya@example.com",
#         phone="9876543211",
#         age=23,
#         gender="Female",
#         city="Chennai",
#         qualification="B.Tech",
#         is_active=True
#     )

#     student3 = Student.objects.create(
#         name="Kumar",
#         email="kumar@example.com",
#         phone="9876543212",
#         age=24,
#         gender="Male",
#         city="Salem",
#         qualification="B.Sc",
#         is_active=True
#     )
#     return HttpResponse("created")



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Course, Student
from .serializers import (
    CourseSerializer,
    StudentSerializer,
    StudentPostSerializer,
)


# ---------------- COURSE CRUD ----------------

class CourseListCreateView(APIView):

    # GET: List all courses
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    # POST: Create a course
    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CourseDetailView(APIView):

    # Get the course or return 404
    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)

    # GET: Retrieve one course
    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    # PUT: Update all required course fields
    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PATCH: Update selected course fields
    def patch(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(
            course,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE: Delete a course
    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()

        return Response(
            {"message": "Course deleted successfully"},
            status=status.HTTP_200_OK
        )


# ---------------- STUDENT CRUD ----------------

class StudentListCreateView(APIView):

    # GET: List all students with course details
    def get(self, request):
        students = Student.objects.prefetch_related("courses")
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    # POST: Create a student with course IDs
    def post(self, request):
        serializer = StudentPostSerializer(data=request.data)

        if serializer.is_valid():
            student = serializer.save()

            # Return nested course details in the response
            response_serializer = StudentSerializer(student)

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class StudentDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(
            Student.objects.prefetch_related("courses"),
            pk=pk
        )

    # GET: Retrieve one student with course details
    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # PUT: Update student details and course IDs
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentPostSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():
            student = serializer.save()
            response_serializer = StudentSerializer(student)
            return Response(response_serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PATCH: Update selected student fields
    def patch(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentPostSerializer(
            student,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            student = serializer.save()
            response_serializer = StudentSerializer(student)
            return Response(response_serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE: Delete a student
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()

        return Response(
            {"message": "Student deleted successfully"},
            status=status.HTTP_200_OK
        )




class StudentCourses(APIView):
    def get(self,request):
        students = Student.objects.prefetch_related('courses')
        # for student in students:
        #     print(student.name)

        #     for course in student.courses.all():
        #          print(course.course_name)
        # return HttpResponse(students)
        serializer = StudentSerializer(students, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class StudentByCourseAPIView(APIView):

    def get(self, request):
        course_name = request.query_params.get("course")

        students = Student.objects.all()

        if course_name:
            students = students.filter(
                courses__course_name__icontains=course_name
            ).distinct()

        students = students.prefetch_related("courses")

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentFilterAPIView(APIView):

    def get(self, request):
        city = request.query_params.get("city")
        course = request.query_params.get("course")

        students = Student.objects.all()

        if city:
            students = students.filter(city__iexact=city)

        if course:
            students = students.filter(
                courses__course_name__icontains=course
            ).distinct()

        students = students.prefetch_related("courses") 

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)