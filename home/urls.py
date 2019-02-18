from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create urls here
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('details/', login_required(views.DetailView.as_view()), name='details'),
    path('checking/', views.Checking.as_view(), name='checking'),
    path('map/', views.MapView.as_view(), name='map'),
    path('json/<int:id>', views.json_response.as_view(), name='json')
]
