from django.shortcuts import render,redirect
from todolist import form

from todolist.form import TodolistForm

from todolist.models import Todolist

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    todo_item = Todolist.objects.order_by('id')
    context={'todo_item': todo_item, 'form' : form}
    return render(request,'todolist/index.html',context)

@require_POST
def addTodoItem(request):
    form=TodolistForm(request.POST)
    if form.is_valid():
        new_todo=Todolist(request.POST['text'])
        new_todo.save()
    
    return redirect('index')


def completedTodo(request,todo_id):
    todo= Todolist.object.get(pk=todo_id)
    todo.completed=True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')


    
