from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path("getprojects/",views.ProjectFetch.as_view()),
  path("addproject/",views.ProjectAdd.as_view()),
  path("deleteproject/<int:id>/",views.ProjectDelete.as_view()),
  path("updateproject/",views.ProjectUpdate.as_view()),
  path("gettasks/<int:projectid>",views.TaskFetch.as_view()),
  path("addtask/",views.TaskAdd.as_view()),
  path("deletetask/<int:id>/",views.TaskDelete.as_view()),
  path("updatetask/",views.TaskUpdate.as_view())
 
]