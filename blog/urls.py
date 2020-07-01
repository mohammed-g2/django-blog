from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/post/', views.post, name='post'),
    path('create/post/', views.create_post, name='create_post'),
    path('<int:id>/edit/post/', views.edit_post, name='edit_post'),
    path('delete/post/', views.delete_post, name='delete_post'),
    path('user/<username>/posts/', views.user_posts, name='user_posts'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
]