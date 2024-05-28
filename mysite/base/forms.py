from django.forms import ModelForm
from .models import Team, Player, Match, League,Match_Goal,Match_Penalty,Squad,Statistics,Queue
from django import forms
from .models import Player
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields= '__all__'
        widgets = {
            'league': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }
'''
class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields= '__all__'
        exclude = ['goals']
        '''



class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ['goals']

        widgets = {
            'team': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields= '__all__'
        exclude = ['finished']
        widgets = {
            'team1': forms.Select(attrs={'class': 'form-control'}),
            'team2': forms.Select(attrs={'class': 'form-control'}),
            'referee': forms.TextInput(attrs={'class': 'form-control'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'}),
            'league': forms.Select(attrs={'class': 'form-control'}),
            'queue_number': forms.NumberInput(attrs={'class': 'form-control'}),

        }


        def __init__(self, *args, **kwargs):
            super(MatchForm, self).__init__(*args, **kwargs)
            if 'league' in self.data:
                try:
                    league_id = int(self.data.get('league'))
                    self.fields['queue_number'].queryset = Queue.objects.filter(league_id=league_id).order_by('number')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty Queue queryset
            elif self.instance.pk and self.instance.league:
                self.fields['queue_number'].queryset = self.instance.league.queue_set.order_by('number')
            else:
                self.fields['queue_number'].queryset = Queue.objects.none()

class StatisticsForm(ModelForm):
    class Meta:
        model = Statistics
        fields= '__all__'

'''
class FinishedMatchForm(ModelForm):
    class Meta:
        model = Finished_Match
        fields= '__all__'
        '''

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }


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

