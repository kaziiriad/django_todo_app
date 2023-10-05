from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task

# Create your views here.


def index(request):

    queryset = Task.objects.order_by('priority', 'created_at', 'status')

    context = {'queryset': queryset}

    return render(request, 'todo_app/index.html', context)

def create(request):

    if request.method == 'POST':
    
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST.get('priority')

        task = Task(
            title = title,
            description = description,
            priority = priority
        )
        task.save()

        return redirect('home')

    return render(request, 'todo_app/create.html')

def view_tasks(request, id):

    queryset = Task.objects.get(id=id)

    context = {'queryset': queryset}

    return render(request, 'todo_app/view_tasks.html', context)

def update_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        
        task.order = Task.objects.count()
        task.status = True  # Toggle the status
        task.save()

        Task.objects.filter(status=False).exclude(id=task.id).update(order=models.F('order') - 1)
        
    return redirect('home')

# def delete_task(request, id):
    
    # if request.method == 'POST':
    #     task = Task.objects.filter(id=id)
    #     task.is_delete = True
    #     task.save()    

