from . import models
from rest_framework import serializers


class ProjectSer(serializers.ModelSerializer):
    class Meta:
        model=models.Project
        fields='__all__'

class TaskSer(serializers.ModelSerializer):
    class Meta:
        model=models.Task
        fields='__all__'