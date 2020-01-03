from django.urls import path
from todolist_app import views
# from .views import todolist

urlpatterns = [
    path('', views.todolist, name = "todolist"),
    # path('', todolist, name = "todolist")
]
