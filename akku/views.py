from django.shortcuts import render,HttpResponse,redirect
from  .models import Student

# Create your views here.
from .forms import StudentForm

def forms(request):
    ob=StudentForm()
    return render(request,'forms.html',{'ob':ob})

def forminsert(request):
    if request.method=='GET':
        ob=StudentForm()
        return render(request,'forms.html',{'ob':ob})
    else:
        ob=StudentForm(request.POST)
        if ob.is_valid():
            ob.save()
            return HttpResponse("inserted")
        return redirect('forminsert')