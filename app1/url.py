from django.urls import path
from .views import hellow_world
urlpatterns = [

    path("", hellow_world) ,
] 