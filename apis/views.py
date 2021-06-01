from django.shortcuts import render

# Create your views here.


from django.http import *
from django.shortcuts import *
from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import status
from .serializers import *
from .models import *



class ProjectFetch(APIView):
    def get(self,req):
        projects = Project.objects.all()
        projectser=ProjectSer(projects,many=True)
        return Response(projectser.data)

class ProjectAdd(APIView):
    def post(self,req):
        project = Project()
        project.project_name=req.data["project_name"]
        project.project_deadline=req.data["project_deadline"]
        project.project_image=req.data["avatar"]
        project.save()
        projectser=ProjectSer(project,many=False)
        return Response(projectser.data)
class ProjectDelete(APIView):
    def delete(self,req,id):
        project = Project.objects.get(id=id)
        project.delete()
        return Response({"message":"DONE","action":"DELETED"})
class ProjectUpdate(APIView):
    def put(self,req):
        project =Project.objects.get(id=req.data["id"])
        
        project.project_name=req.data["project_name"]
        project.project_deadline=req.data["project_deadline"]
        project.save()
        return Response({"message":"DONE","action":"UPDATED"})



class TaskFetch(APIView):
    def get(self,req,projectid):
        Tasks = Task.objects.filter(project=projectid)
        Taskser=TaskSer(Tasks,many=True)
        return Response(Taskser.data)

class TaskAdd(APIView):
    def post(self,req):
        task = Task()
        task.Task_name=req.data["Task_name"]
        task.Task_details=req.data["Task_details"]
        task.project=req.data["project_id"]
        task.save()
        Taskser=TaskSer(task,many=False)
        return Response(Taskser.data)
        
class TaskDelete(APIView):
    def delete(self,req,id):
        task = Task.objects.get(id=id)
        task.delete()
        return Response({"message":"DONE","action":"DELETED"})
       
class TaskUpdate(APIView):
    def put(self,req):
        task =Task.objects.get(id=req.data["id"])
        
        task.Task_name=req.data["Task_name"]
        task.Task_details=req.data["Task_details"]
        task.save()
        return Response({"message":"DONE","action":"UPDATED"})
        
