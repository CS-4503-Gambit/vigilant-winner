from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import *
from .forms import JudgeForm
import json

# Create your views here.
#Home page for the judge page
def home(request):
    judge = request.user.judge 
	#Database searches to seperate judged and unjuded teams
    unjudged = Team.objects.exclude(team_name__in=Judge_Team.objects.filter(judge=judge).values('team'))
    judged = Team.objects.filter(team_name__in=Judge_Team.objects.filter(judge=judge).values('team'))
	#map to html page
    context = {'unjudged': unjudged, 'judged': judged}
    return render(request, 'judge/home.html', context)

#Judgeing page where scoring criteria are desplayed for a particular team
def judge_team(request, team_name):
    judge = request.user.judge
	#try if the team name is in the database, mostly used when scanning QR code
    try:
        team = Team.objects.get(team_name=team_name)
    except:
        return redirect('/judge/home')
	#get criteria for specific team that is being loaded
    category = team.category
    criteria = []
    for crit in category.criteria.all():
        criteria.append(crit.name)
    try:
		#Checks to see if score values exist for the selected team
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

#Functionality of sending scores to database after score is submitted, returns to home page
def submit_score(request, team_name):
    judge = request.user.judge
    team = Team.objects.get(team_name=team_name)
    category = team.category
	#checks if Judge_Team object exists, if not create database object
    try:
        jt = Judge_Team.objects.get(judge=judge, team=team)
    except:
        jt = Judge_Team()
        jt.judge = judge
        jt.team = team
        jt.save()
    form = JudgeForm(request.POST, criteria=None)
    data = form.data
	#iterates through criteria to updates or add scores 
    for crit in category.criteria.all():
        try:
            s = jt.score_set.get(criterion=crit)
        except:
            s = Score()
            s.judge_team = jt
            s.criterion = crit
        s.value = data[crit.name]
        s.save()
    return redirect('/judge/home')

@csrf_exempt
def sync(request):
    judge = request.user.judge
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        for team_name, values in data.items():
            team = Team.objects.get(team_name=team_name)
            try:
                jt = Judge_Team.objects.get(judge=judge, team=team)
            except:
                jt = Judge_Team()
                jt.judge = judge
                jt.team = team
                jt.save()
            for value in values:
                for sc_name, score in value.items():
                    sc = Score_Criterion.objects.get(name=sc_name)
                    try:
                        s = Score.objects.get(criterion=sc, judge_team=jt)
                    except:
                        s = Score()
                        s.criterion = sc
                        s.judge_team = jt
                        s.save()
                    s.value = score
                    s.save()
        return HttpResponse("Success")
    return HttpResponse("Error")
