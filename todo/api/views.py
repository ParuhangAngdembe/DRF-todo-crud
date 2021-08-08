import re
from rest_framework import serializers
from .models import Task
from .serializers import TaskSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverView(requst):
    api_urls = {
		'List':'/tasklist/',
		'Detail View':'/taskdetail/<str:pk>/',
		'Create':'/taskcreate/',
		'Update':'/taskupdate/<str:pk>/',
		'Delete':'/taskdelete/<str:pk>/',
		}
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    #this means do we want to serialize oine object or many objects
    return Response(serializer.data)
    #this will now query our database, serialize the data and return the data in our api response

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id= pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id= pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id= pk)
   
    task.delete()
    return Response("data deleted")
        
    