from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views
from registration.views import activate
from registration.views import register
from college.registrationz.formsz import RegistrationFormZ
urlpatterns = patterns('',
    # Activation keys get matched by w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^activate/(?Pw+)/$', activate, name='registration_activate'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),
    url(r'^password/change/$', auth_views.password_change, name='auth_password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset, name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P[0-9A-Za-z]+)-(?P.+)/$', auth_views.password_reset_confirm, name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='auth_password_reset_complete'),
    url(r'^password/reset/done/$', auth_views.password_reset_done, name='auth_password_reset_done'),
    url(r'^register/$', register, {'form_class' : RegistrationFormZeta}, name='registration_register'),
    url(r'^register/complete/$', direct_to_template, {'template': 'registration/registration_complete.html'}, name='registration_complete'),
)
