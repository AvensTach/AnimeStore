from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('users/<str:username>/', views.user_profile, name='profile'),
    path('registration/', views.registrationPage, name='registration'),
]
