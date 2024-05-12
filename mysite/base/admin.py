from django.contrib import admin

# Register your models here.
from .models import Match, Team, Statistics, Participation, Player, Squad, Scorer_Table,League,Season_table

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Statistics)
admin.site.register(Participation)
admin.site.register(Player)
admin.site.register(Squad)
admin.site.register(Scorer_Table)
admin.site.register(League)
admin.site.register(Season_table)