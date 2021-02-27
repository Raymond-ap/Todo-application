from django.urls import path
from .views import *

urlpatterns = [
    path('', todosPage, name='todos'),
    path('update/<slug:slug>', updateTOdo, name='update'),
    path('delete/<slug:slug>', deleteTodo, name='delete'),
    path('clear', clearCompleted, name='clear'),
]
