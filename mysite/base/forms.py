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

class LeagueForm(ModelForm):
    class Meta:
        model = League
        fields= '__all__'


class MatchGoalForm(ModelForm):
    class Meta:
        model = Match_Goal
        fields= '__all__'
        exclude=['match','team']

class MatchPenaltyForm(ModelForm):
    class Meta:
        model = Match_Penalty
        fields= '__all__'
        exclude=['match','team']


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

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)
        super(SquadForm, self).__init__(*args, **kwargs)
        if team:
            self.fields['player'].queryset = Player.objects.filter(team=team)
        else:
            self.fields['player'].queryset = Player.objects.none()

