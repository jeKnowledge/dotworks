import datetime
from django.test import TestCase
from dotworks_server.models import Student


class StudentTestCase(TestCase):
    """
    Student creation tests
    """
    def create_student(self):
        """
        Creates a student
        """
        user_id = 7
        name = 'Machado'
        email = 'machado@machado.com'
        description = 'This is a test'
        phone_number = '987654321'
        city = 'Lisbon'
        country = 'Portugal'
        birth_date = datetime.datetime.now().date()
        degree = 'SECUNDARIO'
        return Student.objects.create(
            user_id=0,
            name=name,
            e_mail=email,
            description=description,
            phone_number=phone_number,
            city=city,
            country=country,
            birth_date=birth_date,
            degree=degree
        )

    def test_student(self):
        student = self.create_student()
        self.assertTrue(isinstance(student, Student))
