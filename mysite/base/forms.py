from django.forms import ModelForm
from .models import Team, Player, Match

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