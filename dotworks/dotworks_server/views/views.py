from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template import loader

from django.core.urlresolvers import reverse, reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from ..forms import LoginForm, StudentRegisterForm, InternshipCreationForm
from ..forms import InscriptionAddForm
from ..models import Student, Internship, Inscription


# Tests for the views

# Tests whether the user is a company
def is_company(user):
    if user.is_authenticated():
        try:
            return not not user.company
        except:
            pass
    return False


# Tests whether a user is a student
def is_student(user):
    if user.is_authenticated():
        try:
            return not not user.student
        except:
            pass
        return False


# Create your views here

def index(request):
    if request.user.is_authenticated():
        company = is_company(request.user)
        template = loader.get_template('home.html')
        # FILTERS
        filter = {
            "category": request.GET.get('category', None),
            "area": request.GET.get('area', None),
        }
        arguments = {}
        for key, value in filter.items():
            if value is not None:
                arguments[key] = value
        internship_list = Internship.objects.filter(**arguments)
        context = {
            'internship_list': internship_list,
            'is_company': company,
        }
    else:
        template = loader.get_template('landingPage.html')
        login_form = LoginForm()
        context = {
            'loginForm': login_form
        }
    return HttpResponse(template.render(context, request))


def user_login(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:  # Login succesfull
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))


# Reverse_lazy must be used
# instead of reverse because reverse hasnt been loaded at this point
@login_required(login_url=reverse_lazy('index'))
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register_action(request):
    context = {}

    if request.POST:
        form = StudentRegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            description = form.cleaned_data['description']
            github = form.cleaned_data['github']
            linkdin = form.cleaned_data['linkdin']
            facebook = form.cleaned_data['facebook']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            birth_date = form.cleaned_data['birth_date']
            degree = form.cleaned_data['degree']

            # Create new user and student with that user
            user = User.objects.create_user(
                username=email,
                password=password
            )
            student = Student(
                user=user,
                name=name,
                e_mail=email,
                description=description,
                github=github,
                linkdin=linkdin,
                facebook=facebook,
                phone_number=phone,
                city=city,
                country=country,
                birth_date=birth_date,
                degree=degree
            )
            student.save()
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                template = loader.get_template('home.html')
                return HttpResponse(template.render(context, request))
        else:
            print(form.errors.as_data())
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))


def student_register(request):
    print(reverse('index'))
    template = loader.get_template('studentRegister.html')
    student_register_form = StudentRegisterForm()
    context = {
        'studentRegisterForm': student_register_form
    }
    return HttpResponse(template.render(context, request))


@user_passes_test(is_company, login_url=reverse_lazy('no_permission_error'))
def internship_creation(request):
    template = loader.get_template('internship_creation.html')
    internship_creation_form = InternshipCreationForm()
    context = {
        'internshipCreationForm': internship_creation_form
    }
    return HttpResponse(template.render(context, request))


@user_passes_test(is_company, login_url=reverse_lazy('no_permission_error'))
def internship_creation_action(request):
    if request.POST:
        form = InternshipCreationForm(request.POST)
        if form.is_valid():
            company = request.user.company
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            application_deadline = form.cleaned_data['application_deadline']
            internship = Internship(
                title=title,
                company=company,
                description=description,
                application_deadline=application_deadline
            )
            internship.save()
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url=reverse_lazy('no_permission_error'))
def internship_details(request, internship_id):
    internship = Internship.objects.get(pk=internship_id)
    template = loader.get_template('internship_details.html')
    context = {
        'internship': internship,
    }
    return HttpResponse(template.render(context, request))


@user_passes_test(is_company, login_url=reverse_lazy('no_permission_error'))
def company_area(request):
    company_internships = Internship.objects.filter(company=request.user.company)
    template = loader.get_template('company_area.html')
    context = {
        'company_internships': company_internships,
    }
    return HttpResponse(template.render(context, request))


@user_passes_test(is_student, login_url=reverse_lazy('no_permission_error'))
def inscription_addition(request, internship_id):
    context = {
        'internship': Internship.objects.get(pk=internship_id),
    }
    template = loader.get_template('inscription_addition.html')
    return HttpResponse(template.render(context, request))


@user_passes_test(is_student, login_url=reverse_lazy('no_permission_error'))
def inscription_add_action(request, internship_id):
    if request.POST:
        form = InscriptionAddForm(request.POST)
        if form.is_valid():
            internship = Internship.objects.get(pk=internship_id)
            student = Student.objects.get(pk=request.user.student.id)
            inscription_exists = not not Inscription.objects.filter(
                internship=internship, student=student)
            if inscription_exists:
                return internship_details(request, internship_id)
            inscription = Inscription(internship=internship, student=student)
            inscription.save()
    return internship_details(request, internship_id)


def no_permission_error(request):
    context = {}
    template = loader.get_template('no_permission.html')
    return HttpResponse(template.render(context, request))
