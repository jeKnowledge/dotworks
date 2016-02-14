from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login


# Create your views here.


def index(request):

    template = loader.get_template('dotworksServer/landingPage.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))



def user_login(request):
	state = "Please log in below..."
	email = ''
	password = ''
	context = {

    }
	


	if request.POST:
		email = request.POST.get('username')
		password = request.POST.get('password')

		print(email)
		print(password)

		user = authenticate(username=email, password=password)

		if user is not None: #login succesfull
			login(request, user)
			template = loader.get_template('dotworksServer/home.html')
			return HttpResponse(template.render(context, request))
		else:
			return HttpResponseRedirect(reverse('index'))

		


	
