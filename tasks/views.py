from django.shortcuts import render
from django.views import View
from .models import Task

# Create your views here.
class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})


