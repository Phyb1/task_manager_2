from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})
    
    def post(self, request):
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, pk=task_id)
        task.completed = not task.completed
        task.save()
        return redirect('task-list')
    
        
class TaskCreateView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_form.html', {'form':form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        return render(request, 'task_form.html', {'form':form})


