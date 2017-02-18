from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='student_register'),
    url(r'^register/$', views.student_register, name='register'),
    url(r'^register_action/$', views.register_action, name='register_action'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^create_internship$', views.internship_creation, name='internship_creation'),
    url(r'^internship_creation_action$', views.internship_creation_action, name='internship_creation_action'),
    url(r'^internship/(?P<internship_id>[0-9]+)/$', views.internship_details, name='internship_details'),
    url(r'^edit_internship/(?P<internship_id>[0-9]+)/$', views.open_edit_internship_page, name='open_edit_internship_page'),
    url(r'^edit_internship_action/(?P<internship_id>[0-9]+)/$', views.edit_internship, name='edit_internship'),
    url(r'^filter_internship/(?P<category_>[0-9]+)/$', views.filter_internship, name='filter_internship'),
    url(r'^company_area$', views.company_area, name="company_area"),
    url(r'^internship_addition/(?P<internship_id>[0-9]+)/$', views.inscription_addition, name='inscription_addition'),
    url(r'^inscription_add_action/(?P<internship_id>[0-9]+)/$', views.inscription_add_action, name='inscription_add_action'),
    url(r'^no_permission_error/$', views.no_permission_error, name='no_permission_error'),
    url(r'^change_password_page/$', views.change_password_page, name='change_password_page'),
    url(r'^change_password/$', views.change_password, name='change_password'),
]
