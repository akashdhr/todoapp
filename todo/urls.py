from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<item_id>', views.completeTodo, name='completeitem')
]