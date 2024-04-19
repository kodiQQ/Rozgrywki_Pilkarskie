from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('teams/', views.teams, name="teams"),
    path('admin_panel/',views.admin_panel,name="admin_panel"),
    path('admin_panel/team_management/',views.team_management,name="team_management"),
    path('admin_panel/team_management/team_create/',views.team_create,name="team_create"),
    path('admin_panel/team_management/team_delete/<int:pk>',views.team_delete,name="team_delete"),
    path('admin_panel/team_management/team_edit/<int:pk>', views.team_edit, name="team_edit"),
    path('admin_panel/player_management/',views.player_management,name="player_management"),
    path('admin_panel/match_management/',views.match_management,name="match_management"),
    #path('admin_panel/team_management/add_team',views.team_management,name="team_add"),




]