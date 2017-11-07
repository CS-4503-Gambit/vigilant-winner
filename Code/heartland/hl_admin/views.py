from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import *
from django.db.models import Avg
from .forms import *
from django.contrib.auth.models import User

# The home screen. Provides links to the other major Admin functionality.
def home(request):
    context = {'no_home': True}
    return render(request, 'hl_admin/home.html', context)

# List the categories available for scoring.
def categories(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'hl_admin/categories.html', context)

# List the criteria on which the category can be evaluated.
def criteria(request, category):
    c = Category.objects.get(name=category)
    context = {'category': c, 'teams': c.team_set.all()}
    return render(request, 'hl_admin/criteria.html', context)

# Finally, list the sorted scores based on their average judge evaluation in
# the specified category and criterion.
def scores(request, category, criteria):
    cat = Category.objects.get(name=category)
    crit = Score_Criterion.objects.get(name=criteria)
    scores = Score.objects.filter(criterion=crit, judge_team__team__category=cat).values('judge_team__team', 'judge_team__team__entry_name').annotate(avg=Avg('value')).order_by('-avg')
    context = {'category': cat, 'criterion': crit, 'scores': scores}
    return render(request, 'hl_admin/scores.html', context)

# Lists all the judges whose scores can be reviewed.
def judges(request):
    context = {'judges': Judge.objects.all()}
    return render(request, 'hl_admin/judges.html', context)

# Display the judge's average scoring per criterion.
def judge_stats(request, judge_name):
    judge = Judge.objects.get(user__username=judge_name)
    scores = Score.objects.filter(judge_team__judge=judge).values('criterion').annotate(avg=Avg('value'))
    context = {'judge': judge, 'scores': scores}
    return render(request, 'hl_admin/judge_stats.html', context)

# Create a new user with the posted form, or else provide a form to fill.
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
                r.password = form.data['password'] # Storing the password as a charfield so we can use it in the qr code...
                r.save()
            elif form.data['type'] == 'Judge':
                j = Judge()
                j.user = u
                j.password = form.data['password']
                j.save()
        encoded = form.data['username'] + '%' + form.data['password'] # Separate username and password by %
        userurl = "https://api.qrserver.com/v1/create-qr-code/?data=" + encoded + "&amp;size=400x400"
        context = {'header': u.username, 'qrurl': userurl, 'redirect': '/admin/home'}
        return render(request, 'core/showqr.html', context)
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'hl_admin/createuser.html', context)

# List every entity who can have a QR Code generated.
def viewqr(request):
    registrars = Registrar.objects.all()
    judges = Judge.objects.all()
    teams = Team.objects.all()
    context = {'registrars': registrars, 'judges': judges, 'teams': teams}
    return render(request, 'hl_admin/listqr.html', context)

# Display the QR code for the selected registrar
def qr_registrar(request, registrar_name):
    try:
        registrar = Registrar.objects.get(user__username=registrar_name)
        encoded = registrar.user.username + '%' + registrar.password
        regurl = "https://api.qrserver.com/v1/create-qr-code/?data=" + encoded + "&amp;size=400x400"
        context = {'header': 'Registrar ' + registrar.user.username, 'qrurl': regurl, 'redirect': '/admin/home'}
        return render(request, 'core/showqr.html', context)
    except:
        return redirect('viewqr')
    
# Display the QR code for the selected judge
def qr_judge(request, judge_name):
    try:
        judge = Judge.objects.get(user__username=judge_name)
        encoded = judge.user.username + '%' + judge.password
        judgeurl = "https://api.qrserver.com/v1/create-qr-code/?data=" + encoded + "&amp;size=400x400"
        context = {'header': 'Judge ' + judge.user.username, 'qrurl': judgeurl, 'redirect': '/admin/home'}
        return render(request, 'core/showqr.html', context)
    except:
        return redirect('viewqr')

# Display the QR code for the selected team.
def qr_team(request, team_name):
    try:
        team = Team.objects.get(team_name=team_name)
        team_url = "https://api.qrserver.com/v1/create-qr-code/?data=" + team.team_name + "&amp;size=400x400"
        context = {'header': 'Team ' + team.team_name, 'qrurl': team_url, 'redirect': '/admin/home'}
        return render(request, 'core/showqr.html', context)
    except:
        return redirect('viewqr')

