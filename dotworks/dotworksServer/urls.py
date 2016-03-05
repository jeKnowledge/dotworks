from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='student_register'),
    url(r'^register/$', views.student_register, name='register'),
    url(r'^register_action/$', views.register_action, name='register_action'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]