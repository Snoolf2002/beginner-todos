from django.urls import path
from .views import TaskView

urlpatterns = [
    path('todos/', TaskView.as_view()),
]