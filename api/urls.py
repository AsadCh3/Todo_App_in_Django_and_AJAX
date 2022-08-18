from . import views
from django.urls import path

urlpatterns = [
    path('apioverview', views.apiOverview),
    path('task-list', views.taskList),
    path('task-details/<str:pk>/', views.taskDetails),
    path('task-create', views.taskCreate),
    path('task-update/<str:pk>/',views.taskUpdate),
    path('task-delete/<str:pk>/',views.taskDelete),
    
]