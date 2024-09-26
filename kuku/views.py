from django.shortcuts import render,HttpResponse,redirect
from  .models import Student
# Create your views here.
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
def master(request):
    return render(request,'form.html')
def insert(request):
    if request.method=='GET':
        return render(request,'form.html')
    else:
        a=request.POST['name']
        b=request.POST['place']
        c=request.POST['phone']

        Student.objects.create(name=a,place=b,phone=c)
        return HttpResponse("inserted")
def readall(request):
    ob=Student.objects.all()
    return render(request,'table.html',{'ob':ob})



def readget(request,val):
    ob=Student.objects.get(id=val)
    return render(request,'table1.html',{'ob':ob})


def readfiler(request,place):
    ob=Student.objects.filter(place=place)
    return render(request,'table.html',{'ob':ob})


def del2(request,id):
    Student.objects.get(id=id).delete()
    return redirect ("readall")

def update(request,id):

   if request.method=='GET':
       ob=Student.objects.get(id=id)
       return render(request,'update.html',{'ob':ob})
   else:
       a = request.POST['name']
       b = request.POST['place']
       c = request.POST['phone']
       Student.objects.filter(id=id).update(name=a,place=b,phone=c)
       return redirect ("readall")
def user(request):
    if request.method=='GET':
        return render(request,"user.html")
    else:
        a=request.POST['username']
        b=request.POST['password']
        User.objects.create_user( username=a, password=b)
        return HttpResponse("user")

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        a = request.POST['username']
        b = request.POST['password']
        value=authenticate(username=a,password=b)
        if value is not None:
            return HttpResponse("user logined")
        else:
            return HttpResponse("invalid username or password")
def email(request):
    send_mail(
        "django project",
        "i hope you have a wonderful birthday coming up soon "
        " may your birthday bring you happiness ",
        settings.EMAIL_HOST_USER,
        ["amaldv117@gmail.com"],
        fail_silently=False,)
    return HttpResponse("emailsend")

