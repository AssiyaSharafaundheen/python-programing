from django.urls import path
from .import views

urlpatterns=[
    path('master/',views.master,name='master'),
    path("m",views.insert,name='home'),
    path("readall/",views.readall,name='readall'),
    path("readget/<int:val>", views.readget, name='readget'),
    path("readfilter/<place>", views.readfiler, name='filter'),
    path("delete/<int:id>",views.del2,name='del2'),
    path("update/<int:id>", views.update, name='update'),
    path("user/",views.user,name='user'),
    path("login/", views.login, name='login'),
    path("email/", views.email, name='email'),

]