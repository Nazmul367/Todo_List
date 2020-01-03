from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList

# Create your views here.

def todolist(request):
    # return HttpResponse ("amr apumoni")
    # context = {
    #     "todolist_text" : "Todolist Html" 
    # }

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
