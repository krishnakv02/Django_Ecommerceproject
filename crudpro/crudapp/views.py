from django.shortcuts import render,redirect
from . forms import TaskForm
from . models import Task
from django.contrib import messages

# Create your views here.

def home(request):
    form=TaskForm()

    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'task created')
            return redirect("home")
        else:
            messages.error(request,'oops something went wrong')
            return redirect("home")
    task=Task.objects.all()
    
    context={'form':form,'task':task}
    return render(request,"home.html",context)

def deletetask(request,pk):
    deltask=Task.objects.get(id=pk)
    deltask.delete()
    return redirect("home")

def Taskupdate(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"updated")
            return redirect("home")
        
    context={'form':form }
    return render(request,'taskupdate.html',context)
    


    


