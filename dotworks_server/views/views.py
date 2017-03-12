from datetime import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template import loader

from django.core.urlresolvers import reverse, reverse_lazy

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from django.shortcuts import redirect

from ..forms import LoginForm, StudentRegisterForm, InternshipCreationForm, StudentEditProfile, InternshipEditForm
from ..forms import InscriptionAddForm, ChangePasswordForm
from ..models import Student, Internship, Inscription

from datetime import datetime


# Util functions

def inscription_belongs_to_user(student_id_, inscription_id_):
    '''
    Checks if the inscription belongs to the user
    '''
    user_inscriptions = Inscription.objects.filter(student_id=student_id_)

    for inscription in user_inscriptions:
        if int(inscription.id) == int(inscription_id_):
            return True
    return False


def student_is_already_enrolled_in_internship(student_id, inscriptions_in_internship):
    '''
    Checks if student is already inrolled in internship
    '''
    for inscription in inscriptions_in_internship:
        if inscription.student.id == student_id:
           return True
    return False


def get_available_internship_list(filter):
    '''
    Retrieve all available internships
    '''
    arguments = {}
    today = datetime.now()
    for key, value in filter.items():
        if value is not None:
            arguments[key] = value
    return Internship.objects.filter(
        **arguments,
        application_deadline__gte=today
    )


def filter_available_internships(available_internships, category_):
    internship_list = []
    if category_ == '1':
        internship_list = Internship.objects.filter(category='VER')
    elif category_ == '2':
        internship_list = Internship.objects.filter(category='CUR')
    elif category_ == '3':
        internship_list = Internship.objects.filter(category='PRO')
    else:
        internship_list = Internship.objects.all()
    return internship_list


# Validations for the views

def is_company(user):
    '''
    Validates wheter the user is a company
    '''
    if user.is_superuser:
        return True
    if user.is_authenticated():
        try:
            return not not user.company
        except:
            pass
    return False


def is_student(user):
    '''
    Validates wheter the user is a student
    '''
    if user.is_superuser:
        return True
    if user.is_authenticated():
        try:
            return not not user.student
        except:
            pass
        return False


def index(request):
    if request.user.is_authenticated():
        company = is_company(request.user)
        template = loader.get_template('base.html')
        # FILTERS
        filter = {
            'category': request.GET.get('category', None),
            'area': request.GET.get('area', None),
        }
        internship_list = get_available_internship_list(filter)
        internship_list = internship_list.order_by('company__name')
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


@user_passes_test(is_student, login_url=reverse_lazy('no_permission_error'))
def info(request):
    '''
    Render page with info about .works
    '''
    template = loader.get_template('info.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url=reverse_lazy('index'))
def edit_profile(request, student_id):
    '''
    Edit the profile
    '''
    user = request.user
    student = Student.objects.get(pk=student_id)

    if request.method == 'POST':
        form = StudentEditProfile(request.POST, instance=student)

        if form.is_valid():
            # Student editing and saving 
            student.name = form.cleaned_data['name']
            student.e_mail = form.cleaned_data['e_mail']
            student.github = form.cleaned_data['github']
            student.linkedin = form.cleaned_data['linkedin']
            student.behance = form.cleaned_data['behance']
            student.phone = form.cleaned_data['phone_number']
            student.city = form.cleaned_data['city']
            student.birth_date = form.cleaned_data['birth_date']
            student.degree = form.cleaned_data['degree']
            student.description = form.cleaned_data['description']
            student.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            template = loader.get_template('profile.html')
            student_id_ = int(student.id)
            list_of_inscriptions = Inscription.objects.filter(student_id=student_id_)
            change_password_form = ChangePasswordForm()
            context = {
                'id': student_id_,
                'editStudentForm': form,
                'changePasswordForm': change_password_form,
                'list_of_inscriptions': list_of_inscriptions
            }
            return HttpResponse(template.render(context, request))
    return HttpResponseRedirect(reverse('profile'))


@login_required(login_url=reverse_lazy('index'))
def profile(request):
    '''
    Opens profile page
    '''
    template = loader.get_template('profile.html')
    user_id_ = int(request.user.id)
    # Unsafe if query doesnt return anything, need to change this after completion
    student = Student.objects.filter(user_id=user_id_)[0]
    student_id_ = int(student.id)
    list_of_inscriptions = Inscription.objects.filter(student_id=student_id_)
    edit_student_form = StudentEditProfile(instance=student)
    change_password_form = ChangePasswordForm()
    context = {
        'id': student_id_,
        'editStudentForm': edit_student_form,
        'changePasswordForm': change_password_form,
        'list_of_inscriptions': list_of_inscriptions
    }
    return HttpResponse(template.render(context, request))


def filter_internship(request, category_):
    '''
    Filter internships by category
    '''
    template = loader.get_template('base.html')
    filter = {
        'category': request.GET.get('category', None),
        'area': request.GET.get('area', None),
    }
    internship_list = get_available_internship_list(filter)
    internship_list = filter_available_internships(internship_list, category_)
    internship_list = internship_list.order_by('company__name')
    company = is_company(request.user)
    context = {
        'internship_list': internship_list,
        'is_company': company,
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
                messages.error(request, 'Email ou Password inválida')
                return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Email ou Password inválida')
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
    if request.POST:
        form = StudentRegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.clean_email()
            password = form.cleaned_data['password']
            description = form.cleaned_data['description']
            github = form.cleaned_data['github']
            linkedin = form.cleaned_data['linkedin']
            behance = form.cleaned_data['behance']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
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
                linkedin=linkedin,
                behance=behance,
                phone_number=phone,
                city=city,
                birth_date=birth_date,
                degree=degree
            )
            student.save()

            user = authenticate(username=email, password=password)
            company = is_company(user)
            arguments = {}
            filter = {
                'category': request.GET.get('category', None),
                'area': request.GET.get('area', None),
            }

            internship_list = get_available_internship_list(filter)
            context = {
                'internship_list': internship_list,
                'is_company': company,
            }
            if user is not None:
                login(request, user)
                template = loader.get_template('base.html')
                return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('studentRegister.html')
            context = {
                'studentRegisterForm': form
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('index'))


def student_register(request):
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
            beginning_date = form.cleaned_data['beginning_date']
            duration = form.cleaned_data['duration']
            working_time = form.cleaned_data['working_time']
            payment = form.cleaned_data['payment']
            location = form.cleaned_data['location']
            n_positions = form.cleaned_data['n_positions']

            internship = Internship(
                title=title,
                company=company,
                description=description,
                application_deadline=application_deadline,
                beginning_date=beginning_date,
                duration=duration,
                working_time=working_time,
                payment=payment,
                location=location,
                n_positions=n_positions,
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
def edit_internship(request, internship_id):
    internship = Internship.objects.get(pk=internship_id)

    if request.method == 'POST':
        form = InternshipEditForm(request.POST)
        if form.is_valid():
            internship.title = form.cleaned_data['title']
            internship.description = form.cleaned_data['description']
            internship.beginning_date = form.cleaned_data['beginning_date']
            internship.duration = form.cleaned_data['duration']
            internship.working_time = form.cleaned_data['working_time']
            internship.application_deadline = form.cleaned_data['application_deadline']
            internship.payment = form.cleaned_data['payment']
            internship.location = form.cleaned_data['location']
            internship.n_positions = form.cleaned_data['n_positions']
            internship.save()
    return HttpResponseRedirect(reverse('index'))


@user_passes_test(is_company, login_url=reverse_lazy('no_permission_error'))
def open_edit_internship_page(request, internship_id):
    template = loader.get_template('edit_internship.html')
    internship = Internship.objects.get(pk=internship_id)
    edit_internship_form = InternshipEditForm(instance=internship)
    context = {
        'edit_internship_form': edit_internship_form,
        'internship': internship
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
    user_id_ = int(request.user.id)
    student_id_ = int(Student.objects.filter(user_id=user_id_)[0].id)
    student_inscriptions = Inscription.objects.filter(student_id=student_id_)
    inscriptions_in_internship = Inscription.objects.filter(internship_id=internship_id)

    if len(student_inscriptions) >= 3:
        messages.error(request, 'Limite de 3 inscrições atingido')
        return HttpResponseRedirect(reverse('index'))
    elif student_is_already_enrolled_in_internship(student_id_, inscriptions_in_internship):
        messages.error(request, 'Já estás inscrito neste estágio')
        return HttpResponseRedirect(reverse('index'))

    template = loader.get_template('inscription_addition.html')
    inscription_add_form = InscriptionAddForm()
    context = {
        'internship': Internship.objects.get(pk=internship_id),
        'InscriptionAddForm': inscription_add_form
    }
    return HttpResponse(template.render(context, request))


@user_passes_test(is_student, login_url=reverse_lazy('no_permission_error'))
def inscription_add_action(request, internship_id):
    if request.POST:
        form = InscriptionAddForm(request.POST)
        if form.is_valid():
            internship = Internship.objects.get(pk=internship_id)
            student = Student.objects.get(pk=request.user.student.id)
            answers = [
                form.cleaned_data['first_answer'],
                form.cleaned_data['second_answer']
            ]

            inscription = Inscription(
                internship=internship,
                student=student,
                answers=answers
            )
            inscription.save()
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url=reverse_lazy('no_permission_error'))
def inscription_removal(request, inscription_id_):
    '''
    Removes inscription
    '''
    user_id_ = int(request.user.id)
    student_id_ = int(Student.objects.filter(user_id=user_id_)[0].id)
    student_inscriptions = Inscription.objects.filter(student_id=student_id_)

    if len(student_inscriptions) == 0 or not inscription_belongs_to_user(student_id_, inscription_id_):
       return no_permission_error(request) 

    Inscription.objects.filter(id=int(inscription_id_)).delete()
    return redirect('profile')


def no_permission_error(request):
    context = {}
    template = loader.get_template('no_permission.html')
    return HttpResponse(template.render(context, request))


def change_password_page(request):
    change_password_form = ChangePasswordForm()
    context = {
        'changePasswordForm': change_password_form
    }
    template = loader.get_template('change_password_page.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url=reverse_lazy('index'))
def change_password(request):
    if request.POST:
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']

            if user.check_password(old_password):
                if new_password == confirm_new_password:
                    username = user.username #to login after the password is changed
                    user.set_password(new_password)
                    user.save()
                    user = authenticate(username=username, password=new_password)
                    login(request, user)
                else:
                    messages.error(request, 'A nova password não coincide')
            else:
                messages.error(request, 'Password antiga incorreta')
    return HttpResponseRedirect(reverse('profile'))
