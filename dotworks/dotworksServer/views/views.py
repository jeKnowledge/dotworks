from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from ..forms import LoginForm, StudentRegisterForm, InternshipCreationForm
from ..models import Company, Student, Internship




# Create your views here.


def index(request):
    if request.user.is_authenticated():
        internship_list = Internship.objects.order_by('-application_deadline')
        template = loader.get_template('dotworksServer/home.html')
        context = {
            'internship_list': internship_list,
        }
    else:
        template = loader.get_template('dotworksServer/landingPage.html')
        loginForm = LoginForm()
        context = {
            'loginForm':loginForm
        }
    return HttpResponse(template.render(context, request))



def user_login(request):
    context = { }


    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None: #login succesfull
                login(request, user)
                template = loader.get_template('dotworksServer/home.html')
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))

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

            #create new user and student with that user
            user = User.objects.create_user(
                username = email, password=password)
            student = Student(
                user=user, name = name, e_mail=email, 
                description=description, github=github,linkdin=linkdin, 
                facebook=facebook, 
                phone_number=phone, city=city, country=country, 
                birth_date=birth_date, degree=degree)
            student.save()
            user = authenticate(username = email, password = password)
            if user is not None:
                login(request, user)
                template = loader.get_template('dotworksServer/home.html')
                return HttpResponse(template.render(context, request))
        else:
            print(form.errors.as_data())
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))

def student_register(request):
    template = loader.get_template('dotworksServer/studentRegister.html')
    studentRegisterForm = StudentRegisterForm()
    context = {
        'studentRegisterForm':studentRegisterForm
    }
    return HttpResponse(template.render(context, request))        

def internship_creation(request):
    template = loader.get_template('dotworksServer/internship_creation.html')
    internshipCreationForm = InternshipCreationForm()
    context = {
        'internshipCreationForm': internshipCreationForm
    }
    return HttpResponse(template.render(context, request))

def internship_creation_action(request):
    context = {}
    if request.POST:
        form = InternshipCreationForm(request.POST)
        if form.is_valid():
            company = request.user.company
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            application_deadline = form.cleaned_data['application_deadline']
            internship = Internship(title = title, company = company, 
                description = description, 
                application_deadline=application_deadline)
            internship.save()
    return HttpResponseRedirect(reverse('index'))