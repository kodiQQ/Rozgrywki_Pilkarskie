from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Team
from .forms import TeamForm
# Create your views here.

def loginPage(request):

    if request.user.is_authenticated:
       return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
             user = User.objects.get(username=username)
        except:
             messages.error(request, 'Podany użytkownik nie istnieje')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Błędna nazwa użytkownika lub hasło')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request,'base/home.html')

def teams(request):
    teams=Team.objects.all()
    context={'teams':teams}
    return render(request,'base/teams.html',context)

def admin_panel(request):
    return render(request,'base/admin_panel.html')

def team_management(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request,'base/admin_panel_context/team_management.html',context)

def team_create(request):
    form=TeamForm()
    context={'form': form}
    #bez tego ifa to co wpiszemy i zatwierdzimy na stronie nie będzie zapisane w bazie danych!
    if request.method =='POST':
        form=TeamForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/admin_panel_context/team_form.html',context)

def team_edit(request,pk):
    team = Team.objects.get(id=pk)
    form = TeamForm(instance=team)
    context = {'form': form}
    if request.method == 'POST':
        form= TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_management')
    return render(request, 'base/admin_panel_context/team_form.html', context)

def team_delete(request,pk):
    team=Team.objects.get(id=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_management')
    context={'obj':team}
    return render(request, 'base/admin_panel_context/team_delete.html',context)



def player_management(request):
    return render(request,'base/admin_panel_context/player_management.html')

def match_management(request):
    return render(request,'base/admin_panel_context/match_management.html')
