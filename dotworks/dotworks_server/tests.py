import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from dotworks_server.models import Student, Company, Internship


class StudentTestCases(TestCase):
    '''
    Student creation tests
    '''

    def create_valid_student(self):
        '''
        Create student that should pass tests
        '''
        name = 'Machado'
        email = 'machado@machado.com'
        password = 'test'
        test_student = User.objects.create_user(name, email, password)
        description = 'This is a test'
        phone_number = '987654321'
        city = 'Lisbon'
        country = 'Portugal'
        birth_date = datetime.datetime.now().date()
        degree = 'SECUNDARIO'
        return Student.objects.create(
            user=test_student,
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
        student = self.create_valid_student()
        self.assertTrue(isinstance(student, Student))


class CompanyTestCases(TestCase):
    '''
    Company creation tests
    '''

    def create_valid_company(self):
        '''
        Create company that should pass tests
        '''
        name = 'Faber'
        email = 'faber@faber.com'
        password = 'this_is_faber_password'
        user = User.objects.create_user(name, email, password)
        description = 'Summer Internship'
        website = 'faber.com'
        phone_number = '987654321'
        return Company.objects.create(
            user=user,
            name=name,
            e_mail=email,
            description=description,
            website=website,
            phone_number=phone_number
        )

    def test_company(self):
        '''
        Test company attributes
        '''
        company = self.create_valid_company()
        self.assertTrue(isinstance(company, Company))


class InternshipTestCases(TestCase):
    '''
    Internship creation tests
    '''

    def create_company(self):
        name = 'Faber'
        email = 'faber@faber.com'
        password = 'this_is_faber_password'
        user = User.objects.create_user(name, email, password)
        description = 'Summer Internship'
        website = 'faber.com'
        phone_number = '987654321'
        return Company.objects.create(
            user=user,
            name=name,
            e_mail=email,
            description=description,
            website=website,
            phone_number=phone_number
        )
 

    def create_valid_internship(self):
        '''
        Create valid internship
        '''
        title = 'Amazing internship'
        company = self.create_company()
        category = 'CUR'
        description = 'This is an amazing internship'
        beginning_date = datetime.datetime.now().date()
        duration = 2
        working_time = 'F_T'
        application_deadline = datetime.datetime.now().date()
        payment = '600'
        location = 'Coimbra'
        n_positions = 3
        return Internship.objects.create(
            title=title,
            company=company,
            category=category,
            description=description,
            beginning_date=beginning_date,
            duration=duration,
            working_time=working_time,
            application_deadline=application_deadline,
            payment=payment,
            location=location,
            n_positions=n_positions
        )

    def test_internship(self):
        '''
        Test internship attributes
        '''
        internship = self.create_valid_internship()
        self.assertTrue(isinstance(internship, Internship))
