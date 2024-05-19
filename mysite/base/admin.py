from django.contrib import admin

# Register your models here.
from .models import Match,Queue, Team, Statistics, Participation, Player, Squad, Scorer_Table,League,Season_table,Position,Type_of_Card,Match_Penalty
from .models import Match_Goal
admin.site.register(Match)
admin.site.register(Queue)
admin.site.register(Team)
admin.site.register(Statistics)
admin.site.register(Participation)
admin.site.register(Player)
admin.site.register(Squad)
admin.site.register(Scorer_Table)
admin.site.register(League)
admin.site.register(Season_table)
admin.site.register(Position)
admin.site.register(Type_of_Card)
admin.site.register(Match_Penalty)
admin.site.register(Match_Goal)