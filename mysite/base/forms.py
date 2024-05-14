from django.forms import ModelForm
from .models import Team, Player, Match, League,Match_Goal,Match_Penalty

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
        exclude = ['match']

class MatchPenaltyForm(ModelForm):
    class Meta:
        model = Match_Penalty
        fields= '__all__'
        exclude=['match']