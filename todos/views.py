from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse 
from .models import Task

# This function creates a new task and saves it to the database
def addTask(request):
    # Get the task from the request
    task = request.POST['task']
    # Create a new task object with the given task
    Task.objects.create(task=task, )
    # Redirect the user to the home page
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return  redirect('home')


def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
       context = {
           'get_task': get_task,
       }
       return render(request, 'edit_task.html', context)
   
   
def delete_task(request, pk):
   task = get_object_or_404(Task, pk=pk)
   task.delete()
   return redirect('home')
  
