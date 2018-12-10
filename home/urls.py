from django.urls import path
from . import views

# Create urls here
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('details/', views.DetailView.as_view(), name='details'),
]
