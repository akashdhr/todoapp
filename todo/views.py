from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TextForm
from .models import Todo
# Create your views here.

def index(request):
    todo_list = Todo.objects.order_by('id')
    todo_form = TextForm()
    context={'todo_list':todo_list, 'todo_form': todo_form}
    return render(request, 'todo/index.html', context)

def completeTodo(request, item_id):
    todo = Todo.objects.get(pk=item_id)
    todo.completed = True
    todo.save()
    return redirect('index')
