from django.forms import ModelForm
from .models import Team, Player, Match, League

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