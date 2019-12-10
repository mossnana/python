from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(req):
    return HttpResponse('Hello World Response')

def template_render(req):
    if req.method == 'POST':
        form = TaskForm(req.POST)
        form.save()
        return redirect('/tasks')
    else:
        context = _task_render(req)
        return render(req, 'tasks/list.html', context)

def task_edit(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = not task.complete
    task.save()
    return redirect('/tasks', pk=task.pk)

def task_delete(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/tasks', pk=task.pk)

def _task_render(req):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form
    }
    return context