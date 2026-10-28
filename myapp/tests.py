from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status


class StudentAPITest(APITestCase):

    def test_get_students(self):
        response = self.client.get("/api/students/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertIsInstance(response.data, list)

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Student


class StudentAPITestPost(APITestCase):

    def test_create_student(self):
        data = {
            "name": "Arun",
            "email": "arun@example.com",
            "phone": "9876543210",
            "age": 22,
            "gender": "Male",
            "city": "Coimbatore",
            "qualification": "B.E",
            "is_active": True,
            "courses": []
        }

        response = self.client.post(
            "/api/students/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(Student.objects.count(), 1)



    def test_create_student_with_invalid_data(self):
        data = {}

        response = self.client.post(
            "/api/students/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


    def test_update_student(self):
        student = Student.objects.create(
            name="Arun",
            email="arun@example.com",
            phone="9876543210",
            age=22,
            gender="Male",
            city="Coimbatore",
            qualification="B.E",
            is_active=True
        )

        data = {
            "name": "Kumar",
            "email": "kumar@example.com",
            "phone": "9876543211",
            "age": 23,
            "gender": "Male",
            "city": "Chennai",
            "qualification": "M.E",
            "is_active": True,
            "courses": []
        }

        response = self.client.put(
            f"/api/students/{student.id}/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        student.refresh_from_db()
        self.assertEqual(student.name, "Kumar")


    def test_patch_student(self):
        student = Student.objects.create(
            name="Arun",
            email="arun@example.com",
            phone="9876543210",
            age=22,
            gender="Male",
            city="Coimbatore",
            qualification="B.E",
            is_active=True
        )

        data = {
            "city": "Chennai"
        }

        response = self.client.patch(
            f"/api/students/{student.id}/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        student.refresh_from_db()
        self.assertEqual(student.city, "Chennai")
        self.assertEqual(student.name, "Arun")

    def test_delete_student(self):
        student = Student.objects.create(
            name="Arun",
            email="arun@example.com",
            phone="9876543210",
            age=22,
            gender="Male",
            city="Coimbatore",
            qualification="B.E",
            is_active=True
        )

        student_id = student.id

        response = self.client.delete(
            f"/api/students/{student_id}/"
        )

        self.assertEqual(response.status_code, 200)

        self.assertFalse(
            Student.objects.filter(id=student_id).exists()
        )
# | Assertion | What it checks | Example |
# |---|---|---|
# | `assertEqual()` | Two values are equal | `self.assertEqual(response.status_code, 200)` |
# | `assertTrue()` | A condition is true | `self.assertTrue(student.is_active)` |
# | `assertFalse()` | A condition is false | `self.assertFalse(Student.objects.filter(id=student.id).exists())` |
# | `assertIsInstance()` | A value has a particular type | `self.assertIsInstance(response.data, list)` |