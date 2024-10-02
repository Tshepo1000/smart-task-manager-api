from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/suggest/', TaskViewSet.as_view({'post': 'suggest'}), name='task-suggest'),
    path('tasks/<int:pk>/predict-due-date/', TaskViewSet.as_view({'post': 'predict_due_date'}), name='predict-due-date'),
]