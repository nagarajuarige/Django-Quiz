from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.homepageadmin, name='homepageadmin'),
    url(r'^addquizhome$', views.addquizhome, name='addquizhome'),
    url(r'^addquiz$', views.addquiz, name='addquiz'),
    url(r'^addquestionhome$', views.addquestionhome, name='addquestionhome'),
    url(r'^addquestion$', views.addquestion, name='addquestion'),
    url(r'^addquestiontoexistinghome$', views.addquestiontoexistinghome, name='addquestiontoexistinghome'),
    url(r'^addquestiontoexisting$', views.addquestiontoexisting, name='addquestiontoexisting'),
]