from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from django.db.models import Avg

# Create your views here.
def home(request):
    return render(request, 'admin/home.html')

def categories(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'admin/categories.html', context)

def criteria(request, category):
    c = Category.objects.get(name=category)
    context = {'category': c, 'teams': c.team_set.all()}
    return render(request, 'admin/criteria.html', context)

def scores(request, category, criteria):
    cat = Category.objects.get(name=category)
    crit = Score_Criterion.objects.get(name=criteria)
    scores = Score.objects.filter(criterion=crit).values('judge_team__team').annotate(avg=Avg('value')).order_by('-avg')
    context = {'category': cat, 'criterion': crit, 'scores': scores}
    return render(request, 'admin/scores.html', context)

def judges(request):
    context = {'judges': Judge.objects.all()}
    return render(request, 'admin/judges.html', context)

def judge_stats(request, judge_name):
    judge = Judge.objects.get(user__username=judge_name)
    scores = Score.objects.filter(judge_team__judge=judge).values('criterion').annotate(avg=Avg('value'))
    context = {'judge': judge, 'scores': scores}
    return render(request, 'admin/judge_stats.html', context)
