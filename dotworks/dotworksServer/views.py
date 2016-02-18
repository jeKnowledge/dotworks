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


	if request.POST:
		form = LoginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			print(username)
			print(password)

			user = authenticate(username=username, password=password)

			if user is not None: #login succesfull
				login(request, user)
				template = loader.get_template('dotworksServer/home.html')
				return HttpResponse(template.render({}, request))
			else:
				return HttpResponseRedirect(reverse('index'))
		else:
			return HttpResponseRedirect(reverse('index'))	

		


	