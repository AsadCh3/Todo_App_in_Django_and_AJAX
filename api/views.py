from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers

# Create your views here.

@api_view(['GET', 'POST'])
def apiOverview(request):
    return JsonResponse('API Response', safe=False)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializers(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(data=request.data, instance=task)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('item deleted')
