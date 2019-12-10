from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(req):
    return HttpResponse('Hello World Response')

def template_render(req):
    print('>>>>>>>>>>>>> Request', req)
    if req.method == 'POST':
        form = TaskForm(req.POST)
        form.save()
        return redirect('/tasks')
    else:
        context = _task_render(req)
        return render(req, 'tasks/list.html', context)

def _task_render(req):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form
    }
    return context