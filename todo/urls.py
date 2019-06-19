from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<item_id>', views.completeTodo, name='completeitem'),
    path('add/', views.add_todo, name='addtodo'),
    path('delete/', views.delete_crossed, name='delete'),
    path('clear/', views.clear_all, name="clearall")
]