from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Team
# Create your views here.
def admin_panel(request):
    return render(request,'base/admin_panel.html')

def team_management(request):
    return render(request,'base/admin_panel_context/team_management.html')

def player_management(request):
    return render(request,'base/admin_panel_context/player_management.html')

def match_management(request):
    return render(request,'base/admin_panel_context/match_management.html')