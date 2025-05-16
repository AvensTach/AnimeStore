from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('users/<str:username>/', views.user_profile, name='user-page'),
    path('registration/', views.registraion, name='registraion'),
]
