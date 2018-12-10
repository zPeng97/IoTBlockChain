from django.urls import path
from . import views


urlpatterns = [
    # /world/
    path('', views.index, name= "worldmap")
]

