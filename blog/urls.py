from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^write/$', views.write, name='write'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.delete, name='post_delete'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.edit, name='post_edit'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
]
