from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# Create urls here
urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name="accounts"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEdit.as_view(), name='profile_edit'),
    path('profile/password/', views.PasswordChange.as_view(), name='password_change'),
]
