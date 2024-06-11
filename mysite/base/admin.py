from django.contrib import admin

# Register your models here.
from .models import Match,Queue, Team, Statistics, Participation, Player, Squad, Scorer_Table,League,Season_table,Position,Type_of_Card,Match_Penalty
from .models import Match_Goal, Match_and_Score
from .forms import MatchForm

#admin.site.register(Match)
#admin.site.register(Queue)
admin.site.register(Team)
admin.site.register(Statistics)
admin.site.register(Participation)
admin.site.register(Player)
admin.site.register(Squad)
admin.site.register(Scorer_Table)
#admin.site.register(League)
admin.site.register(Season_table)
admin.site.register(Position)
admin.site.register(Type_of_Card)
admin.site.register(Match_Penalty)
admin.site.register(Match_Goal)
admin.site.register(Match_and_Score)
@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = ('number', 'league')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    form = MatchForm
    list_display = ('team1', 'team2', 'queue_number', 'league', 'finished')