from django.urls import path
from . import views

# app_name = 'mainapp'

urlpatterns = [
    path("", views.home, name="task-list"),
    path("task/new/", views.create_task, name="task-create"),
    path("task/<int:pk>/edit/", views.edit_task, name="task-edit"),
    path("task/<int:pk>/delete/", views.delete_task, name="task-delete"),
    path('invitation/<int:pk>/send/', views.send_invitation_admin, name='send_invitation'),  # Removed "admin" prefix
]
