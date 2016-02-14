from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login

from forms import LoginForm


# Create your views here.


def index(request):

    template = loader.get_template('dotworksServer/landingPage.html')
    loginForm = LoginForm()
    context = {
        'loginForm':loginForm
    }
    return HttpResponse(template.render(context, request))



def user_login(request):
	state = "Please log in below..."
	email = ''
	password = ''
	context = {

    }
	


	if request.POST:
		form = LoginForm(request.POST)

		print(email)
		print(password)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None: #login succesfull
				login(request, user)
				template = loader.get_template('dotworksServer/home.html')
				return HttpResponse(template.render(context, request))
			else:
				return HttpResponseRedirect(reverse('index'))
		else:
			return HttpResponseRedirect(reverse('index'))	

		


	