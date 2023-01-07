from django.shortcuts import render

from todolist.models import Todolist

# Create your views here.

def index(request):
    todo_item = Todolist.objects.order_by('id')
    context={'todo_item': todo_item}
    return render(request,'todolist/index.html',context)
