from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task

@login_required
def index(request):
    tasks = Task.objects.filter(id_user=request.user)
    return render(request, 'index.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.id_user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('index')
    else:
        form = TaskRegistrationForm()
    return render(request, 'addTask.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to home after editing
    else:
        form = TaskRegistrationForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')  # Redirect to home after deletion
    return render(request, 'delete_task.html', {'task': task})