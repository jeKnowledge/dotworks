from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .forms import LoginForm, StudentRegisterForm
from .models import Company, Student




# Create your views here.


def index(request):

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
			print("%s %s" %(username, password))

			print(username)
			print(password)

			user = authenticate(username=username, password=password)
			print(user)

			if user is not None: #login succesfull
				login(request, user)
				template = loader.get_template('dotworksServer/home.html')
				return HttpResponseRedirect(reverse('show home'))
			else:
				return HttpResponseRedirect(reverse('index'))

		else:
			return HttpResponseRedirect(reverse('index'))

	else:
		return HttpResponseRedirect(reverse('index'))

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

	

def index(request):

    template = loader.get_template('dotworksServer/home.html')
    return HttpResponse(template.render({}, request))


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
			user = User.objects.create_user(username = email, password=password)
			student = Student(user=user, name = name, e_mail=email, description=description, github=github,linkdin=linkdin, facebook=facebook,
				phone_number=phone, city=city, country=country, birth_date=birth_date, degree=degree)
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
