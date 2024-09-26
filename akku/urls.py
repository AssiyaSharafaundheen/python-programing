from django.urls import path
from .import views

urlpatterns=[
path("forms/", views.forms, name='forms'),
    path("insert/",views.forminsert,name='forminsert'),

]