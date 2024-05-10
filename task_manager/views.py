from django.shortcuts import redirect, render 
from django.contrib.auth.decorators import login_required
from .import forms
from django.contrib.auth import authenticate,login ,logout
from django.http import HttpResponse
from .import models

# Create your views here.
@login_required
def home (request):
    tasks = models.Task.objects.filter(user=request.user)

    if request.method=="POST":
        add_task_form_data = forms.AddTaskForm(data=request.POST)
        # print(add_task_form_data)
        if add_task_form_data.is_valid():
            print(type(add_task_form_data.cleaned_data))
            
            # add_task_form_data.cleaned_data['user'] = request.user
            # add_task_form_data.save()
            # print(add_task_form_data.cleaned_data)
            cleaned_data = add_task_form_data.cleaned_data
            task_title = cleaned_data.get('title')
            task_desc = cleaned_data.get('desc')
            task_deadline = cleaned_data.get('deadline')
            task_user = request.user

            models.Task.objects.create(
                user = task_user,
                title = task_title,
                desc = task_desc,
                deadline = task_deadline
            )

            return redirect("task_manager:home")

        else:
            return HttpResponse("Invalid Form Data")
        
    else:
        context = {
            'user':request.user,
            'add_task_form':forms.AddTaskForm,
            'tasks':tasks[::-1],


        }
        return render(request, 'task_manager/home.html', context)
  


def login_view(request):
    if request.method == 'POST' :
        form =forms.LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username ,password = password)

            if user is not None:
                login(request,user)
                return redirect('task_manager:home')

    else:
        login_form = forms.LoginForm()
    return render(request, "task_manager/login.html",{'login_form': login_form})


def update_task(request, id):

    if request.method=="POST":
        add_task_form_data = forms.UpdateTaskForm(data=request.POST)
        if add_task_form_data.is_valid():
            cleaned_data = add_task_form_data.cleaned_data
            task = models.Task.objects.get(id=id)
            task.title = cleaned_data.get('title')
            task.desc = cleaned_data.get('desc')
            task.deadline = cleaned_data.get('deadline')
            task.status = cleaned_data.get('status')
            task.save()
            return redirect('task_manager:home')
        else:
            return HttpResponse("Invalid Form Data")
    else:
        task = models.Task.objects.get(id=id)

        context = {
        
            'add_task_form':forms.UpdateTaskForm(instance=task),

        }
        return render(request, 'task_manager/update.html', context)
    

def delete_task(request , id):
    task = models.Task.objects.get(id=id)
    task.delete()
    return redirect('task_manager:home')