from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

class TaskUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, task_id):
        try:
            # Fetch the task for the authenticated user
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the task is already completed
        if task.status == 'Completed' and request.data.get('status') == 'Pending':
            task.status = 'Pending'
            task.completed_at = None  # Clear the timestamp
            task.save()
            return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

        if task.status == 'Pending' and request.data.get('status') == 'Completed':
            task.status = 'Completed'
            task.completed_at = timezone.now()  # Set timestamp for completion
            task.save()
            return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid operation or status.'}, status=status.HTTP_400_BAD_REQUEST)
