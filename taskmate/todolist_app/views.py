from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def todolist(request):
    # return HttpResponse ("amr apumoni")
    # context = {
    #     "todolist_text" : "Todolist Html" 
    # }

    # all_tasks = TaskList.objects.all

    # return render(request, 'todolist.html', { 'all_tasks' : all_tasks })

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Added Successfully !"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', { 'all_tasks' : all_tasks })

# Url = todolist/delete/1 
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

# Url = todolist/edit/1 
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited Successfully !"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', { 'task_obj' : task_obj })

# Url = todolist/complete/1 
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')

# Url = todolist/complete/1 
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')


def home(request):
    # return HttpResponse ("amr apumoni")
    context = {
        "home_text" : "Welcome to Taskmate Dashboard" 
    }
    return render(request, 'home.html', context)


def about(request):
    # return HttpResponse ("amr apumoni")
    context = {
        "about_text" : "About Html" 
    }
    return render(request, 'about.html', context)

def contact(request):
    # return HttpResponse ("amr apumoni")
    context = {
        "contact_text" : "Contact Html" 
    }
    return render(request, 'contact.html', context)
