from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
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
	context = {
	
	}
	if request.POST:
		form = LoginForm(request.POST)
	
	if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			print("%s %s" %(username, password))

			user = authenticate(username=username, password=password)
			print(user)

			if user is not None: #login succesfull
				login(request, user)
				template = loader.get_template('dotworksServer/home.html')
				return HttpResponse(template.render(context, request))
			else:
				return HttpResponseRedirect(reverse('index'))
	else:
		return HttpResponseRedirect(reverse('index'))

def user_register(request):
	context = {

	}
	if request.POST:
		form = RegisterForm(request.POST)

	if form.is_valid():
		name = form.cleaned_data['name']
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		description = form.cleaned_data['description']
		github = form.cleaned_data['github']
		linkdin = form.cleaned_data['linkdin']
		facebook = form.cleaned_data['facebook']
		phone = form.cleaned_data['phone']
		city = form.cleaned_data['city']
		country = form.cleaned_data['country']
		age = form.cleaned_data['age']
		degree = form.cleaned_data['degree']

	new_user = User(username = username, password = password)
	new_user.save()
	new_student = Student(user = new_user, name = name, description = description, github = github, linkdin = linkdin,
		facebook = facebook, phone = phone, city = city, country = country, age = age, degree = degree)
	new_student.save()
	login(request, new_user)
	template = loader.get_template('dotworksServer/home.html') 		
	return HttpResponse(template.render(context, request))

		