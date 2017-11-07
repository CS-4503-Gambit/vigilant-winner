from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import *
from django.db.models import Avg
from .forms import *
from django.contrib.auth.models import User

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
    scores = Score.objects.filter(criterion=crit, judge_team__team__category=cat).values('judge_team__team').annotate(avg=Avg('value')).order_by('-avg')
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

def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        try:
            u = User.objects.get(username=form.data['username'])
        except:
            u = User()
            u.username = form.data['username']
            u.set_password(form.data['password'])
            u.save()
            if form.data['type'] == 'Registrar':
                r = Registrar()
                r.user = u
                r.password = form.data['password']
                r.save()
            elif form.data['type'] == 'Judge':
                j = Judge()
                j.user = u
                j.password = form.data['password']
                j.save()
        encoded = form.data['username'] + '%' + form.data['password']
        userurl = "https://api.qrserver.com/v1/create-qr-code/?data=" + encoded + "&amp;size=400x400"
        context = {'header': u.username, 'qrurl': userurl, 'redirect': '/admin/home'}
        return render(request, 'core/showqr.html', context)
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'admin/createuser.html', context)

def viewqr(request):
    registrars = Registrar.objects.all()
    judges = Judge.objects.all()
    teams = Team.objects.all()
    context = {'registrars': registrars, 'judges': judges, 'teams': teams}
    return render(request, 'admin/listqr.html', context)

def qr_registrar(request, registrar_name):
    try:
        registrar = Registrar.objects.get(user__username=registrar_name)
        encoded = registrar.user.username + '%' + registrar.password
        regurl = "https://api.qrserver.com/v1/create-qr-code/?data=" + encoded + "&amp;size=400x400"
        context = {'header': 'Registrar ' + registrar.user.username, 'qrurl': regurl, 'redirect': '/admin/home'}
        return render(request, 'core/showqr.html', context)
    except:
        return redirect('viewqr')
    
def qr_judge(request, judge_name):
    try:
        judge = Judge.objects.get(user__username=judge_name)
        encoded = judge.user.username + '%' + judge.password
        judgeurl = "https://api.qrserver.com/v1/create-qr-code/?data=" + encoded + "&amp;size=400x400"
        context = {'header': 'Judge ' + judge.user.username, 'qrurl': judgeurl, 'redirect': '/admin/home'}
        return render(request, 'core/showqr.html', context)
    except:
        return redirect('viewqr')

def qr_team(request, team_name):
    try:
        team = Team.objects.get(team_name=team_name)
        team_url = "https://api.qrserver.com/v1/create-qr-code/?data=" + team.team_name + "&amp;size=400x400"
        context = {'header': 'Team ' + team.team_name, 'qrurl': team_url, 'redirect': '/admin/home'}
        return render(request, 'core/showqr.html', context)
    except:
        return redirect('viewqr')

