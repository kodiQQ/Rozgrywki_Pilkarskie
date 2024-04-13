from django.contrib import admin

# Register your models here.
from .models import Match, Team, Statistics, Season_Table, Participation, Player, Contract, Squad, Scorer_Table

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Statistics)
admin.site.register(Season_Table)
admin.site.register(Participation)
admin.site.register(Player)
admin.site.register(Contract)
admin.site.register(Squad)
admin.site.register(Scorer_Table)