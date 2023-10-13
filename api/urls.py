from django.urls import path
from . import views
urlpatterns = [
    path('tasks/', views.TaskAPI.as_view()),
    path('tasks/<int:pk>/', views.TaskAPI.as_view()),
]
