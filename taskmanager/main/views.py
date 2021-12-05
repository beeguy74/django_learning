from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


# Create your views here.
#return page from taskmanager/main/templates
def index(request):
    tasks = Task.objects.order_by('-id')
    return  render(request, 'main/index.html', {'title': 'Website\'s main page', 'tasks': tasks})


def about(request):
    return  render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Form is invalid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return  render(request, 'main/create.html', context)


