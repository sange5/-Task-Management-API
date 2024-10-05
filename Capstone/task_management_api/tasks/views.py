from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

from rest_framework.authentication import TokenAuthentication

class TaskListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    ...

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework import permissions

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = super().get_object()
        if self.request.user == user or self.request.user.is_superuser:
            return user
        else:
            raise permissions.PermissionDenied("You can only manage your own account.")

from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

# List and create tasks (only for authenticated users, and tasks should be user-specific)
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter tasks by the authenticated user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Associate task with the authenticated user
        serializer.save(user=self.request.user)

# Retrieve, update, and delete tasks (only the owner of the task can perform these actions)
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure only the owner can manage their own task
        return Task.objects.filter(user=self.request.user)
