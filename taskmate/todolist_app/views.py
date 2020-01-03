from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def todolist(request):
    # return HttpResponse ("amr apumoni")
    context = {
        "todolist_text" : "Todolist Html" 
    }
    return render(request, 'todolist.html', context)

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
