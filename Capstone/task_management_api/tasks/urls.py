from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
]

from django.urls import path
from tasks import views

urlpatterns = [
    # Task management
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    
    # User management
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/register/', views.UserRegisterView.as_view(), name='user-register'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
