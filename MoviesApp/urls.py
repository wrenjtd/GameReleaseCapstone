from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'MoviesApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('members/', views.members, name='members'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_user/create_user_submission/', views.create_user_submission, name='create_user_submission'),
    path('verify_user/', views.verify_user, name='verify_user'),
    path('accounts/', include('django.contrib.auth.urls')),
]