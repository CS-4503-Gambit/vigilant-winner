from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import *
from .forms import JudgeForm

# Create your views here.
def home(request):
    return render(request, 'judge/home.html')

def teams(request):
    context = {'teams': Team.objects.all()}
    return render(request, 'judge/teams.html', context)

def judge_team(request, team_name):
    judge = request.user.judge
    team = Team.objects.get(team_name=team_name)
    category = team.category
    criteria = []
    for crit in category.criteria.all():
        criteria.append(crit.name)
    try:
        jt = Judge_Team.objects.get(judge=judge, team=team)
        initial = {}
        for crit in category.criteria.all():
            initial[crit.name] = 0
            try:
                initial[crit.name] = jt.score_set.get(criterion=crit).value
            except:
                pass
        form = JudgeForm(initial=initial, criteria=criteria)
    except:
        form = JudgeForm(criteria=criteria)
    context = {'team': team, 'form': form}
    return render(request, 'judge/score.html', context)

def submit_score(request, team_name):
    judge = request.user.judge
    team = Team.objects.get(team_name=team_name)
    category = team.category
    try:
        jt = Judge_Team.objects.get(judge=judge, team=team)
    except:
        jt = Judge_Team()
        jt.judge = judge
        jt.team = team
        jt.save()
    form = JudgeForm(request.POST, criteria=None)
    data = form.data
    for crit in category.criteria.all():
        try:
            s = jt.score_set.get(criterion=crit)
        except:
            s = Score()
            s.judge_team = jt
            s.criterion = crit
        s.value = data[crit.name]
        s.save()
    return redirect('teams')
