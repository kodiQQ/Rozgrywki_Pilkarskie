from django.forms import ModelForm
from .models import Team, Player, Match, League,Match_Goal,Match_Penalty,Squad

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields= '__all__'

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields= '__all__'

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields= '__all__'

'''
class FinishedMatchForm(ModelForm):
    class Meta:
        model = Finished_Match
        fields= '__all__'
        '''

class LeagueForm(ModelForm):
    class Meta:
        model = League
        fields= '__all__'


class MatchGoalForm(ModelForm):
    class Meta:
        model = Match_Goal
        fields= '__all__'
        exclude=['match','team']

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)
        super(MatchGoalForm, self).__init__(*args, **kwargs)
        if team:
            self.fields['player'].queryset = Player.objects.filter(team=team)
        else:
            self.fields['player'].queryset = Player.objects.none()


class MatchPenaltyForm(ModelForm):
    class Meta:
        model = Match_Penalty
        fields= ['player','card']


    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)
        super(MatchPenaltyForm, self).__init__(*args, **kwargs)
        if team:
            self.fields['player'].queryset = Player.objects.filter(team=team)
        else:
            self.fields['player'].queryset = Player.objects.none()


'''
class SquadForm(ModelForm):
    class Meta:
        model = Squad
        fields= ['player']

    #funkcja ogranicza wybór piłkarzy do piłkarzy tylko z danej frużyny
    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)
        super(SquadForm, self).__init__(*args, **kwargs)
        if team:
            self.fields['player'].queryset = Player.objects.filter(team=team)
        else:
            self.fields['player'].queryset = Player.objects.none()
            '''


class SquadForm(ModelForm):
    class Meta:
        model = Squad
        fields = ['player']

    #funkcja ograniczająca wybór piłkarzy do piłkarzy tylko z danego zespołu ( nie do wszystkich z bazy danych)
    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)
        super(SquadForm, self).__init__(*args, **kwargs)
        if team:
            self.fields['player'].queryset = Player.objects.filter(team=team)
        else:
            self.fields['player'].queryset = Player.objects.none()

