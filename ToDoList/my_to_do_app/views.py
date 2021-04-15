from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here. MVC - controller


def index(request):
    # DB read
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, 'my_to_do_app/index.html',content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    # DB save
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo must be " + user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("complete todo ifd : ", done_todo_id)
    # DB select and delete
    todo = Todo.objects.get(id=done_todo_id)
    todo.isDone = True
    todo.save()
    # todo.delete()
    return HttpResponseRedirect(reverse('index'))

