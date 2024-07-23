from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
