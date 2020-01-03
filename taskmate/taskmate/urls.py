from django.contrib import admin
from django.urls import path, include
from todolist_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('todolist/', include('todolist_app.urls')),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact")
]
