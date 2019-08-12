from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Game, GamePlatform, Member
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

def index(request):
    current_games_list = Game.objects.order_by('title')
    context = {
        'current_games_list': current_games_list
    }
    return render(request, 'moviesapp/index.html', context)

def verify_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('MoviesApp:index'))
    else:
        # raise Http404("Invalid user credentials!")
        return HttpResponseRedirect(reverse('MoviesApp:login'))

def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('MoviesApp:index'))

@login_required
def members(request):
    # the_user = User.objects.
    return render(request, 'moviesapp/members.html')
    

def login_page(request):
      return render(request, 'moviesapp/login.html')    

def create_user(request):
    return render(request, 'moviesapp/create_user.html')


def create_user_submission(request):
    m_username = request.POST['username']
    m_email = request.POST['member_email']
    m_birthday = request.POST['birthday']
    m_password = request.POST['password']
    
    a_member = User.objects.create_user(m_username,m_email,m_password)
    group = Group.objects.get(name='Normal')
    a_member.groups.add(group)
    a_member.save()
    return HttpResponseRedirect(reverse('MoviesApp:members'))
# Create your views here.
