from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.FrontPageView,name = 'FrontPageView'),
    url(r'^login/$', views.LoginView, name='LoginView'),
    url(r'^logout/$', views.LogoutView, name='LogoutView'),
]
