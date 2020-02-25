from django.shortcuts import render
from .models import Todo
import data

# Create your views here.
def todos_list(request):
    todos = Todo.objects.all()
    return render(request, 'core/todos_list.html', {'todos': todos})

def todos_detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'core/todos_detail.html', {'todo': todo})