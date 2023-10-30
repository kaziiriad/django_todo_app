from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Task
from django.db.models import F
from .forms import TaskForm

# Create your views here.


def index(request):

    queryset = Task.objects.all()

    context = {'queryset': queryset}

    return render(request, 'todo_app/index.html', context)

def create(request):

    if request.method == 'POST':
    
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect(reverse('home'))

    form = TaskForm()

    return render(request, 'todo_app/create.html', {"form" : form})

def view_tasks(request, id):

    queryset = Task.objects.get(id=id)

    context = {'queryset': queryset}

    return render(request, 'todo_app/view_tasks.html', context)

def update_task(request, id):
    if request.method == 'POST':

        task = Task.objects.get(id=id)
        
        task.status = True  # Toggle the status
        task.save()

    return redirect('home')

def delete_task(request, id):
    
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.is_delete = True
        print(task.is_delete)
        task.save()    

    return redirect('home')
