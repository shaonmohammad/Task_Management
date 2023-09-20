from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_tasks/', views.add_tasks, name='add_tasks'),
    path('task_details/<int:id>/', views.task_details, name='task_details'),
    path('task_delete/<int:id>/', views.task_delete, name='task_delete'),
    path('task_edit/<int:id>/', views.task_edit, name='task_edit')
]
