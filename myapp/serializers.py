from rest_framework.serializers import ModelSerializer
from .views import *


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseStudentSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','course_name','fee']

class StudentSerializer(ModelSerializer):
    courses = CourseStudentSerializer(read_only=True, many=True)
    class Meta:
        model = Student
        fields = '__all__'

class StudentPostSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

