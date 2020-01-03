from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages

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
        all_tasks = TaskList.objects.all
        return render(request, 'todolist.html', { 'all_tasks' : all_tasks })

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
