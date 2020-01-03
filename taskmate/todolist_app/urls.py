from django.urls import path
from todolist_app import views
# from .views import todolist

urlpatterns = [
    path('', views.todolist, name = "todolist"),
    # path('', todolist, name = "todolist")

    path('about/', views.about, name = "about"),
    # path('', about, name = "about")
    
    path('contact/', views.contact, name = "contact"),
    # path('', contact, name = "contact")
]
