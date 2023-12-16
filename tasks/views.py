from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})
    

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


