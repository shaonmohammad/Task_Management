from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def home(request):
    task = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': task})


def add_tasks(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_tasks.html', {'form': form})


def task_details(request, id):
    task = Task.objects.get(pk=id)
    return render(request, 'tasks/task_details.html', {'task': task})


def task_delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')


def task_edit(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('task_details', id=task.id)
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {
        "task": task,
        "form": form
    })
