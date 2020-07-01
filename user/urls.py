from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#  path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

app_name = 'user'

#path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
 
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('<username>/profile/', views.profile, name='profile'),
]