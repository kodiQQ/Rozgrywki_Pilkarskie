from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Team, Player, Statistics, Match, League, Match_Penalty, Match_Goal, Squad, Queue
from .forms import TeamForm, PlayerForm, MatchForm, LeagueForm, MatchPenaltyForm,MatchGoalForm,SquadForm,StatisticsForm
from django.db.models import IntegerField, ExpressionWrapper, F
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
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
    matches = Match.objects.filter(
        (Q(league__name__icontains=q) |
        Q(team1__name__icontains=q) |
        Q(team2__name__icontains=q))&Q(finished=False)
    )
    leagues = League.objects.all()
    match_count = matches.count()
    context = {'matches': matches, 'leagues': leagues, 'match_count': match_count}
    return render(request,'base/home.html',context)

def statistics(request,pk):
    league_obj = League.objects.get(pk=pk)
    league_id1 = league_obj.id
    teams=Team.objects.filter(league_id=league_id1)
    statistics0 = Statistics.objects.filter(team__in=teams)

    #sortuje względem punktów
    statistics = statistics0.annotate(
        total_points=ExpressionWrapper(F('wins') * 3 + F('draws'), output_field=IntegerField())
    ).order_by('-total_points')

    '''
    league_obj = League.objects.get(pk=pk)
    league_id = league_obj.id
    teams_all=Season_table
    print(league_obj)
    teams = Season_table.objects.filter(league=league_obj).values_list('team', flat=True)
    for t in teams:
        print("druzyna: "+str(t))


    statistics_all=Statistics.objects.all()
    for s in statistics_all:
        print("statistics_all:")
        print(s)
        print(s.team.id)
    statistics0 = Statistics.objects.filter(team__in=teams)

    print("statistics0")
    print(statistics0)
    statistics = statistics0.annotate(
        total_points=ExpressionWrapper(F('wins') * 3 + F('draws'), output_field=IntegerField())
    ).order_by('-total_points')
    '''
    '''
    statistics = Statistics.objects.annotate(
        total_points=ExpressionWrapper(F('wins') * 3 + F('draws'), output_field=IntegerField())
    ).order_by('-total_points')
    '''

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

    form = PlayerForm()

    #for field in form:
        #field.label_tag = field.label_tag(attrs={'class': 'form-label'})

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
    matches = Match.objects.filter(finished=False)
    context = {'matches': matches}
    return render(request,'base/admin_panel_context/Match/match_management.html',context)

def finished_match_management(request):
    matches = Match.objects.filter(finished=True)
    context = {'matches': matches}
    return render(request,'base/admin_panel_context/Finished_Match/finished_match_management.html',context)
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
    obj=Match.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('match_management')
    context={'obj':obj}
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
    form = LeagueForm(instance=league)
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
    return render(request, 'base/admin_panel_context/League/league_delete.html',context)





def queues(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    #queues = Queue.objects.filter(league=league)
    match=Match.objects.filter(league=league)
    max_queue_number=0
    for m in match:
        if max_queue_number < m.queue_number:
            max_queue_number=m.queue_number
            
    matches_list=[]
    for i in range(max_queue_number):
        try:
            matches_queue=Match.objects.filter(league=league,queue_number=(i+1))
            matches_list.append(matches_queue)
        except:
            matches_list.append("Brak Meczy")
        


    context = {'league': league, 'matches_list': matches_list}
    return render(request, 'base/queues.html', context)


# def queue_matches(request, league_id, queue_number):
#     league = League.objects.get(pk=league_id)
#     queue = Queue.objects.get(league=league, number=queue_number)
#     matches = Match.objects.filter(queue_number=queue)  # Filtrowanie meczów dla konkretnej kolejki
#
#     print("Liczba meczów:", matches.count())
#
#     context = {'league': league, 'queue': queue, 'matches': matches}
#     return render(request, 'base/queue_matches.html', context)


def match_event_management(request,pk):

    match=Match.objects.get(id=pk)


    team1=match.team1
    team2 = match.team2
    match_goals_team1=Match_Goal.objects.filter(match_id=pk,team=team1)
    match_goals_team2 = Match_Goal.objects.filter(match_id=pk, team=team2)
    match_penalties_team1=Match_Penalty.objects.filter(match_id=pk,team=team1)
    match_penalties_team2 = Match_Penalty.objects.filter(match_id=pk,team=team2)

    check = request.GET.get('q') if request.GET.get('q') != None else ''
    check2 = request.GET.get('r') if request.GET.get('r') != None else ''

    form = None
    print(check)
    print(check2)
    if(check=="add_goal"):

        #form = MatchGoalForm()
        #context = {'form': form}
        # bez tego ifa to co wpiszemy i zatwierdzimy na stronie nie będzie zapisane w bazie danych!

        if request.method == 'POST':
            team = team1 if check2 == "team1" else team2
            form = MatchGoalForm(request.POST, team=team)
            if form.is_valid():
                new_goal = form.save(commit=False)
                new_goal.match = match
                new_goal.team = team
                new_goal.save()
                return redirect('match_event_management', pk=pk)
        else:
            team = team1 if check2 == "team1" else team2
            form = MatchGoalForm(team=team)


    if(check=="add_penalty"):

        if request.method == 'POST':
            team = team1 if check2 == "team1" else team2
            form = MatchPenaltyForm(request.POST, team=team)
            if form.is_valid():
                new_penalty = form.save(commit=False)
                new_penalty.match = match
                new_penalty.team = team
                new_penalty.save()
                return redirect('match_event_management', pk=pk)
        else:
            team = team1 if check2 == "team1" else team2
            form = MatchPenaltyForm(team=team)

    context={'check':check,'match':match,'form':form,'match_goals_team1':match_goals_team1,'match_goals_team2':match_goals_team2,'match_penalties_team1':match_penalties_team1,'match_penalties_team2':match_penalties_team2,'check2':check2}

    return render(request,'base/admin_panel_context/Match_Event/match_event_management.html',context)

def match_event_penalty_delete(request,player_id,match_id):
    match_penalty = Match_Penalty.objects.filter(player_id=player_id,match_id=match_id)
    if request.method == 'POST':
        match_penalty.delete()
        return redirect('match_event_management',match_id)
    context = {'obj': match_penalty[0]}
    return render(request,'base/admin_panel_context/Match_Event/match_event_penalty_delete.html',context)

def match_event_goal_delete(request,player_id,match_id,time):
    match_goal = Match_Goal.objects.filter(player_id=player_id,match_id=match_id,time=time)
    if request.method == 'POST':
        match_goal.delete()
        return redirect('match_event_management', match_id)
    context = {'obj': match_goal}
    return render(request,'base/admin_panel_context/Match_Event/match_event_goal_delete.html',context)

def squad_management(request, pk):
    match = get_object_or_404(Match, id=pk)
    team1 = match.team1
    team2 = match.team2

    squad_team1 = Squad.objects.filter(match_id=pk, team=team1)
    squad_team2 = Squad.objects.filter(match_id=pk, team=team2)

    check = request.GET.get('q', '')
    check2 = request.GET.get('r', '')
    print(check2)
    form = None

    if check == "add_player":
        if request.method == 'POST':
            team = team1 if check2 == "team1" else team2
            form = SquadForm(request.POST, team=team)
            if form.is_valid():
                new_squad = form.save(commit=False)
                new_squad.match = match
                new_squad.team = team
                new_squad.save()
                return redirect('squad_management', pk=pk)
        else:
            team = team1 if check2 == "team1" else team2
            form = SquadForm(team=team)

    elif check == "delete_player":
        if request.method == 'POST':
            team = team1 if check2 == "team1" else team2
            form = SquadForm(request.POST, team=team)
            if form.is_valid():
                player=request.POST.get('player')
                squad = get_object_or_404(Squad, player=player, team=team, match=match)
                squad.delete()

                return redirect('squad_management', pk=pk)
        else:
            team = team1 if check2 == "team1" else team2
            form = SquadForm(team=team)

    context = {
        'check': check,
        'check2': check2,
        'match': match,
        'form': form,
        'squad_team1': squad_team1,
        'squad_team2': squad_team2,
    }

    return render(request, 'base/admin_panel_context/Squad/squad_management.html', context)

def finish_match(request,pk):
    match=Match.objects.get(id=pk)

    #sprawdzenie czy pole statystyki istnieje:
    try:
        Statistics.objects.get(team=match.team1)
    except:
        form=StatisticsForm()
        new_statistics = form.save(commit=False)
        new_statistics.team = match.team1
        new_statistics.save()

    try:
        Statistics.objects.get(team=match.team2)
    except:
        form=StatisticsForm()
        new_statistics = form.save(commit=False)
        new_statistics.team = match.team2
        new_statistics.save()


    if match.finished==False:
        match.finished=True
        match.save()
        try:
            team1_goals=Match_Goal.objects.filter(match=match,team=match.team1)
            team1_goals_count=len(team1_goals)
            team2_goals = Match_Goal.objects.filter(match=match, team=match.team2)
            team2_goals_count = len(team2_goals)
            team1_statistics=Statistics.objects.get(team=match.team1)
            team2_statistics = Statistics.objects.get(team=match.team2)

            for g in team1_goals:
                p = Player.objects.get(id=g.player.id)
                p.goals = p.goals + 1
                p.save()

            for g in team2_goals:
                p = Player.objects.get(id=g.player.id)
                p.goals = p.goals + 1
                p.save()


            if team1_goals_count == team2_goals_count:
                team1_statistics.draws=team1_statistics.draws+1
                team2_statistics.draws = team2_statistics.draws + 1

            elif  team1_goals_count > team2_goals_count:
                team1_statistics.wins= team1_statistics.wins+1
                team2_statistics.loses=team2_statistics.loses+1
            else:
                team1_statistics.loses = team1_statistics.loses + 1
                team2_statistics.wins = team2_statistics.wins + 1

            team1_statistics.goals=team1_statistics.goals+team1_goals_count
            team1_statistics.goals_lost=team1_statistics.goals_lost+team2_goals_count
            team2_statistics.goals = team2_statistics.goals + team2_goals_count
            team2_statistics.goals_lost = team2_statistics.goals_lost + team1_goals_count

            team1_statistics.save()
            team2_statistics.save()
        except:
            1




    return redirect('match_management')

def cancel_finish_match(request,pk):
    match=Match.objects.get(id=pk)

    if match.finished==True:
        match.finished=False
        match.save()
        try:
            team1_goals=Match_Goal.objects.filter(match=match,team=match.team1)
            team1_goals_count=len(team1_goals)
            team2_goals = Match_Goal.objects.filter(match=match, team=match.team2)
            team2_goals_count = len(team2_goals)
            team1_statistics=Statistics.objects.get(team=match.team1)
            team2_statistics = Statistics.objects.get(team=match.team2)

            for g in team1_goals:
                p = Player.objects.get(id=g.player.id)
                p.goals = p.goals - 1
                p.save()

            for g in team2_goals:
                p = Player.objects.get(id=g.player.id)
                p.goals = p.goals - 1
                p.save()

            if team1_goals_count == team2_goals_count:
                team1_statistics.draws=team1_statistics.draws-1
                team2_statistics.draws = team2_statistics.draws-1

            elif  team1_goals_count > team2_goals_count:
                team1_statistics.wins= team1_statistics.wins-1
                team2_statistics.loses=team2_statistics.loses-1
            else:
                team1_statistics.loses = team1_statistics.loses-1
                team2_statistics.wins = team2_statistics.wins-1

            team1_statistics.goals=team1_statistics.goals-team1_goals_count
            team1_statistics.goals_lost=team1_statistics.goals_lost-team2_goals_count
            team2_statistics.goals = team2_statistics.goals - team2_goals_count
            team2_statistics.goals_lost = team2_statistics.goals_lost - team1_goals_count

            team1_statistics.save()
            team2_statistics.save()
        except:
            1


    return redirect('finished_match_management')



def team(request,pk):
    team=Team.objects.filter(id=pk)
    statistics=Statistics.objects.get(team_id=pk)
    players=Player.objects.filter(team_id=pk)
    context={'team':team,'statistics':statistics,'players':players}

    return render(request,'base/team.html',context)

def player(request,pk):
    player=Player.objects.get(id=pk)
    context = {'player': player}
    return render(request, 'base/player.html', context)

def player_statistics(request,pk):
    league_obj = League.objects.get(pk=pk)
    league_id1 = league_obj.id
    teams=Team.objects.filter(league_id=league_id1)
    player_statistics0 = Player.objects.filter(team__in=teams)

    #sortuje względem punktów
    players = player_statistics0.annotate(
        total_goals=ExpressionWrapper(F('goals'), output_field=IntegerField())
    ).order_by('-total_goals')

    context={'players':players}
    return render(request, 'base/player_statistics.html',context)