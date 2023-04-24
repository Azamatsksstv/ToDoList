from django.urls import path
from todo.views import DetailTodo, DeleteTodo, ListTodo, CreateTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create/', CreateTodo.as_view()),
    path('delete/<int:pk>/', DeleteTodo.as_view()),
]
