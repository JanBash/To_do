from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoListView.as_view()),
    path('detail/<int:pk>/', views.TodoDetailView.as_view()),
    path('create/', views.TodoCreateView.as_view())
]