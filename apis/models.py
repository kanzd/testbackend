from django.db import models

# Create your models here.
class Project(models.Model):
    id=models.AutoField
    project_name=models.TextField(max_length=3000)
    project_deadline=models.TextField(max_length=3000)
    project_image=models.ImageField(upload_to="image/")
    def __str__(self):
        return str(self.id)


class Task(models.Model):
    id=models.AutoField
    project=models.IntegerField()
    Task_name=models.TextField(max_length=3000)
    Task_details=models.TextField(max_length=3000)
    def __str__(self):
        return str(self.id)