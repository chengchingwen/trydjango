from django.shortcuts import render
from todo.models import TodoTask
# Create your views here.

def index(request):
    '''
    The index page
    '''
    return render(request, "index.html")

def list_tasks(request):
    '''
    list all tasks
    '''
    if(request.POST.get('check')):
        task = TodoTask.objects.get(title=request.POST.get('check'))
        task.done = False if task.done else True
        task.save()
        
    return render(request, "list.html", context={
        'tasks':TodoTask.objects.all(),
    })
