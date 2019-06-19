from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
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

def add_todo(request):
    form = TextForm(request.POST)
    if form.is_valid():
        Todo(text=request.POST['text']).save()
    return redirect('index')

def delete_crossed(request):
    Todo.objects.filter(completed=True).delete()
    return redirect('index')

def clear_all(request):
    Todo.objects.all().delete()
    return redirect('index')


    