import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from dotworks_server.models import Student, Company, Internship, Inscription


class StudentCreationMethods:
    def create_valid_student(self):
        '''
        Create valid student
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


class CompanyCreationMethods:
    def create_valid_company(self):
        '''
        Create valid company
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


class InternshipCreationMethods:
    def create_valid_internship(self):
        '''
        Create valid internship
        '''
        company_methods = CompanyCreationMethods()
        title = 'Amazing internship'
        company = company_methods.create_valid_company()
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


class InscriptionCreationMethods:
    def create_valid_inscription(self):
        student_methods = StudentCreationMethods()
        internship_methods = InternshipCreationMethods()
        student = StudentCreationMethods.create_valid_student()
        internship = InternshipCreationMethods.create_valid_internship()
        answers = ['Mostly coding', 'Stuff']
        
        return Inscription.objects.create(
            student=student,
            internship=internship,
            answers=answers
        )


class StudentTestCases(TestCase):
    '''
    Student creation tests
    '''

    def setUp(self):
        student_methods = StudentCreationMethods()
        self.student = student_methods.create_valid_student() 

    def test_student(self):
        self.assertTrue(isinstance(self.student, Student))


class CompanyTestCases(TestCase):
    '''
    Company creation tests
    '''

    def setUp(self):
        company_methods = CompanyCreationMethods()
        self.company = company_methods.create_valid_company()
        
    def test_company(self):
        self.assertTrue(isinstance(self.company, Company))


class InternshipTestCases(TestCase):
    '''
    Internship creation tests
    '''

    def setUp(self):
        internship_methods = InternshipCreationMethods()
        self.internship = internship_methods.create_valid_internship()

    def test_internship(self):
        self.assertTrue(isinstance(self.internship, Internship))


class InscriptionTestCases(object):
    '''
    Inscription creation tests
    '''

    def setUp(self):
        inscription_methods = InscriptionCreationMethods()
        self.inscription = inscription_methods.create_valid_inscription()

    def test_inscription(self):
        self.assertTrue(isinstance(self.inscription, Inscription))
