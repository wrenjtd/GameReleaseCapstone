from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Game, GamePlatform, Member
from django.urls import reverse

def index(request):
    current_games_list = Game.objects.order_by('title')
    context = {
        'current_games_list': current_games_list
    }
    return render(request, 'moviesapp/index.html', context)

def login(request):
    return HttpResponse('Login:ok')

def logout(request):
    return HttpResponse('Logout:ok')

def members(request):
    return HttpResponse('WishList Page: ok')

def create_user(request):
    m_username = request.POST['username']
    m_email = request.POST['member_email']
    m_birthday = request.POST['birthday']
    m_password = request.POST['password']
    a_member = Member(username=m_username, email=m_email, birthday=m_birthday, password=m_password)
    a_member.save()
    
    return HttpResponseRedirect(reverse('MoviesApp:members'))


# def submit(request):

# Create your views here.
