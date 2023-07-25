from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('taskupdate/<str:pk>',views.Taskupdate,name="taskupdate"),
    path('taskdelete/<str:pk>',views.deletetask,name="deletetask"),
]
