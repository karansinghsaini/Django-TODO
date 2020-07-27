from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

from .forms import TaskForm, UpdateTaskForm
# Create your views here.

@login_required
def home(request):
    user = request.user
    tasks = Task.objects.filter(author=user)

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = user
            new_form.save()
        return redirect('/')
    
    context = {
        'tasks': tasks,
        'form': form
    }    
    return render(request, 'tasks/home.html', context)

@login_required
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = UpdateTaskForm(instance=task)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'tasks/update_task.html', context)

@login_required
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    context = {
        'item': task
    }

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'tasks/delete_task.html', context)