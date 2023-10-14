from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializers
from tasks.models import Task


class TaskAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Task.objects.get(id=id)
            serializers = TaskSerializers(stu)
            return Response(serializers.data)

        stu = Task.objects.all()
        serializers = TaskSerializers(stu, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = TaskSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'mag': "Task Created"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        stu = Task.objects.get(id=id)
        serializers = TaskSerializers(stu, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        id = pk
        stu = Task.objects.get(id=id)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
