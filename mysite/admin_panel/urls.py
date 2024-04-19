from django.urls import path
from . import views


urlpatterns = [

    path('admin_panel/',views.admin_panel,name="admin_panel"),
    path('admin_panel/team_management/',views.team_management,name="team_management"),
    path('admin_panel/player_management/',views.player_management,name="player_management"),
    path('admin_panel/match_management/',views.match_management,name="match_management"),
    path('admin_panel/team_management/add_team',views.team_management,name="team_management"),
    path('admin_panel/team_management/delete_team',views.team_management,name="team_management"),



]