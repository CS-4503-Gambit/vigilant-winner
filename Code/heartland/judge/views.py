from django.shortcuts import render
from django.http import HttpResponse
from core.models import *

# Create your views here.
def home(request):
    return render(request, 'judge/home.html')

def teams(request):
    context = {'teams': Team.objects.all()}
    return render(request, 'judge/teams.html', context)

def judge_team(request, team_name):
    pass
