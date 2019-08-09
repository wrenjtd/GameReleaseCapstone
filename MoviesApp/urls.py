from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'MoviesApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('members/', views.members, name='members'),
    path('create_user/', views.create_user, name='create_user')
]