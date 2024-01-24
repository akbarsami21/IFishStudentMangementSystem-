from django.shortcuts import render
from .models import Student
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentForm

# Create your views here.
def index(request):
    student=Student.objects.all()
    return render(request,'student/index.html',{'students':student})

def view_student(request,id):
    student=Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            return render(request, 'student/add.html', {'form': StudentForm(), 'success': True})
    else:
        form = StudentForm()
    return render(request, 'student/add.html', {'form': form})

def edit(request,id):
    if request.method == "POST":
        student=Student.objects.get(pk=id)
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            new_student=form.save()
            return render(request,'student/edit.html',{'form':StudentForm(),'success':True})
    else:
      student=Student.objects.get(pk=id)
      form=StudentForm(instance=student)
    return render(request,'student/edit.html',{'form':form})

def delete(request,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect(reverse('index'))
   
   

