from django.shortcuts import render
from todos .models import Task

# This function renders the home page and passes the tasks that are not completed to the template
def home(request):
    # Get all the tasks that are not completed and order them by updated_at in descending order
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    
    # Get all the tasks that are completed and order them by updated_at in ascending order
    completed_tasks = Task.objects.filter(is_completed=True).order_by('updated_at') 
    
    # Create a context dictionary with the tasks
    context = {
        'tasks' : tasks,
        'completed_tasks': completed_tasks,
    }
    
    # Render the home template with the context
    return render(request, 'home.html', context)