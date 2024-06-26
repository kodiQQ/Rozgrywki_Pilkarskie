from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('teams/', views.teams, name="teams"),
    path('match/', views.match_list, name='match-list'),
    path('match/<int:match_id>/', views.match_detail, name='match-detail'),    path('queues/', views.queues, name="queues"),
    path('queues/<int:league_id>/', views.queues, name='queues'),
    path('matches_played/', views.matches_played, name='matches_played'),
    #path('matchdays<int:league_id>/', views.matchdays, name='matchdays'),
    #path('queues/<int:league_id>/', views.queues, name='queues'),
    #path('queues/<int:league_id>/', views.queues, name='queues'),
    #path('queues/<int:league_id>/<int:queue_number>/', views.queue_matches, name='queue_matches'),
    path('team/<int:pk>',views.team, name='team'),
    path('player/<int:pk>',views.player, name='player'),
    path('admin_panel/',views.admin_panel,name="admin_panel"),
    path('admin_panel/team_management/',views.team_management,name="team_management"),
    path('admin_panel/team_management/team_create/',views.team_create,name="team_create"),
    path('admin_panel/team_management/team_delete/<int:pk>',views.team_delete,name="team_delete"),
    path('admin_panel/team_management/team_edit/<int:pk>', views.team_edit, name="team_edit"),
    path('admin_panel/player_management/',views.player_management,name="player_management"),
    path('admin_panel/player_management/player_create',views.player_create,name="player_create"),
    path('admin_panel/player_management/player_delete/<int:pk>',views.player_delete,name="player_delete"),
    path('admin_panel/player_management/player_edit/<int:pk>',views.player_edit,name="player_edit"),
    path('admin_panel/match_management/', views.match_management, name="match_management"),
    path('admin_panel/match_management/match_create/', views.match_create, name="match_create"),
    path('admin_panel/match_management/match_delete/<int:pk>', views.match_delete, name="match_delete"),
    path('admin_panel/match_management/match_edit/<int:pk>', views.match_edit, name="match_edit"),

    path('admin_panel/match_management/match_event_management/<int:pk>', views.match_event_management, name="match_event_management"),

    path('admin_panel/match_management/match_event_management/delete_penalty/<int:player_id>/<int:match_id>', views.match_event_penalty_delete, name="match_event_penalty_delete"),
    path('admin_panel/match_management/match_event_management/delete_goal/<int:player_id>/<int:match_id>/<int:time>', views.match_event_goal_delete, name="match_event_goal_delete"),
    path('admin_panel/match_management/finish_match/<int:pk>',views.finish_match, name="finish_match"),
    path('admin_panel/match_management/cancel_finish_match/<int:pk>',views.cancel_finish_match, name="cancel_finish_match"),

    path('admin_panel/match_management/squad/<int:pk>',views.squad_management ,name="squad_management"),
    path('admin_panel/league_management/', views.league_management, name="league_management"),
    path('admin_panel/league_management/league_create/', views.league_create, name="league_create"),
    path('admin_panel/league_management/league_delete/<int:pk>', views.league_delete, name="league_delete"),
    path('admin_panel/league_management/league_edit/<int:pk>', views.league_edit, name="league_edit"),

    path('statistics/<int:pk>', views.statistics,name='statistics'),
    path('playerstatistics/<int:pk>', views.player_statistics,name='player_statistics'),

    path('admin_panel/match_management/',views.match_management,name="match_management"),
    path('admin_panel/finished_match_management/',views.finished_match_management,name="finished_match_management"),
    #path('admin_panel/team_management/add_team',views.team_management,name="team_add"),




]