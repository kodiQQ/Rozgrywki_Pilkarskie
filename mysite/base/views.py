from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Team, Player, Statistics, Match, League
from .forms import TeamForm, PlayerForm, MatchForm, LeagueForm
from django.db.models import IntegerField, ExpressionWrapper, F
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    matches = Match.objects.filter(league__name__icontains  =q)
    leagues = League.objects.all()
    context = {'matches': matches, 'leagues': leagues}
    return render(request,'base/home.html',context)

def statistics(request):
    statistics = Statistics.objects.annotate(
        total_points=ExpressionWrapper(F('wins') * 3 + F('draws'), output_field=IntegerField())
    ).order_by('-total_points')
    #context={'team':statistics.team, 'wins':statistics.team, 'draws':statistics.draws,'loses':statistics.loses, 'goals':statistics.goals,'goals_lost':statistics.goals_lost, 'points':statistics.points}
    context={'statistics':statistics}
    return render(request, 'base/statistics.html',context)

def teams(request):
    teams=Team.objects.all()
    context={'teams':teams}
    return render(request,'base/teams.html',context)

@login_required(login_url='/login')
def admin_panel(request):
    return render(request,'base/admin_panel.html')


#TEAM
@login_required(login_url='/login')
def team_management(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request,'base/admin_panel_context/Team/team_management.html',context)

@login_required(login_url='/login')
def team_create(request):
    form=TeamForm()
    context={'form': form}
    #bez tego ifa to co wpiszemy i zatwierdzimy na stronie nie będzie zapisane w bazie danych!
    if request.method =='POST':
        form=TeamForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/admin_panel_context/Team/team_form.html',context)

@login_required(login_url='/login')
def team_edit(request,pk):
    team = Team.objects.get(id=pk)
    form = TeamForm(instance=team)
    context = {'form': form}
    if request.method == 'POST':
        form= TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_management')
    return render(request, 'base/admin_panel_context/Team/team_form.html', context)

@login_required(login_url='/login')
def team_delete(request,pk):
    team=Team.objects.get(id=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_management')
    context={'obj':team}
    return render(request, 'base/admin_panel_context/Team/team_delete.html',context)

#PLAYER
@login_required(login_url='/login')
def player_create(request):
    form=PlayerForm()
    context={'form': form}
    #bez tego ifa to co wpiszemy i zatwierdzimy na stronie nie będzie zapisane w bazie danych!
    if request.method =='POST':
        form=PlayerForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/admin_panel_context/Player/player_form.html',context)

@login_required(login_url='/login')
def player_edit(request,pk):
    player = Player.objects.get(id=pk)
    form = PlayerForm(instance=player)
    context = {'form': form}
    if request.method == 'POST':
        form= PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_management')
    return render(request, 'base/admin_panel_context/Player/player_form.html', context)

@login_required(login_url='/login')
def player_delete(request,pk):
    player=Player.objects.get(id=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player_management')
    context={'obj':player}
    return render(request, 'base/admin_panel_context/Player/player_delete.html',context)

@login_required(login_url='/login')
def team_delete(request,pk):
    team=Team.objects.get(id=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_management')
    context={'obj':team}
    return render(request, 'base/admin_panel_context/Team/team_delete.html',context)

@login_required(login_url='/login')
def player_management(request):
    players = Player.objects.all()
    context = {'players': players}
    return render(request,'base/admin_panel_context/Player/player_management.html',context)

@login_required(login_url='/login')
def match_management(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    return render(request,'base/admin_panel_context/Match/match_management.html',context)

#MATCH

@login_required(login_url='/login')
def match_create(request):
    form=MatchForm()
    context={'form': form}
    #bez tego ifa to co wpiszemy i zatwierdzimy na stronie nie będzie zapisane w bazie danych!
    if request.method =='POST':
        form=MatchForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/admin_panel_context/Match/match_form.html',context)

@login_required(login_url='/login')
def match_edit(request,pk):
    match = Match.objects.get(id=pk)
    form = MatchForm(instance=match)
    context = {'form': form}
    if request.method == 'POST':
        form= MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_management')
    return render(request, 'base/admin_panel_context/Match/match_form.html',context)

@login_required(login_url='/login')
def match_delete(request,pk):
    match=Match.objects.get(id=pk)
    if request.method == 'POST':
        match.delete()
        return redirect('match_management')
    context={'obj':match}
    return render(request, 'base/admin_panel_context/Match/match_delete.html',context)

#LEAGUE

@login_required(login_url='/login')
def league_management(request):
    leagues = League.objects.all()
    context = {'leagues': leagues}
    return render(request,'base/admin_panel_context/League/league_management.html',context)

@login_required(login_url='/login')
def league_create(request):
    form=LeagueForm()
    context={'form': form}
    #bez tego ifa to co wpiszemy i zatwierdzimy na stronie nie będzie zapisane w bazie danych!
    if request.method =='POST':
        form=LeagueForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/admin_panel_context/League/league_form.html',context)

@login_required(login_url='/login')
def league_edit(request,pk):
    league = League.objects.get(id=pk)
    form = LeagueForm(instance=match)
    context = {'form': form}
    if request.method == 'POST':
        form= LeagueForm(request.POST, instance=league)
        if form.is_valid():
            form.save()
            return redirect('league_management')
    return render(request, 'base/admin_panel_context/League/league_form.html',context)

@login_required(login_url='/login')
def league_delete(request,pk):
    league = League.objects.get(id=pk)
    if request.method == 'POST':
        league.delete()
        return redirect('league_management')
    context={'obj':league}
    return render(request, 'base/admin_panel_context/Match/league_delete.html',context)