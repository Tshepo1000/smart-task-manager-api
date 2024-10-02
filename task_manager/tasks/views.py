from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse
from rest_framework.decorators import action

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Custom endpoint for task suggestions
    @action(detail=False, methods=['post'], url_path='suggest')
    def suggest(self, request):
        user_input = request.data.get('input', '')
        # Simple suggestion logic (you can enhance it with AI later)
        suggested_title = f"Suggested Title based on: {user_input}"
        return Response({"suggested_title": suggested_title})

    # Custom endpoint for due date prediction
    @action(detail=True, methods=['get'], url_path='predict-due-date')
    def predict_due_date(self, request, pk=None):
        task = self.get_object()
        # Simple prediction logic (enhance with actual logic)
        predicted_date = task.due_date  # Example: use existing due_date
        return Response({"predicted_due_date": predicted_date})

    def task_suggest(request):
        suggestions = ["Task 1", "Task 2", "Task 3"]
        return JsonResponse(suggestions, safe=False)