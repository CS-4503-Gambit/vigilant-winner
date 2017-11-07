from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from core.models import *

# The Registrar's Home Screen: Add a team or edit a team.
def home(request):
    context = {'no_home': True}
    return render(request, 'registrar/home.html', context)

# Add a team to the database using a form.
def addteam(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            team = Team()
            team.team_name = form.data['team_name']
            team.entry_name = form.data['entry_name']
            team.category = Category.objects.get(name=form.data['category'])
            team.registrar = request.user.registrar
            team.save()
            return redirect('/registrar/showqr/' + team.team_name)
    else:
        form = RegistrationForm()
        context = { 'form': form}
        return render(request, 'registrar/addteam.html', context)

# Display the teams separated by whether or not this registrar was the last to update them.
def teams(request):
    myteams = Team.objects.filter(registrar=request.user.registrar)
    otherteams = Team.objects.exclude(registrar=request.user.registrar)
    context = {'myteams': myteams, 'otherteams': otherteams}
    return render(request, 'registrar/teams.html', context)

# Edit the team using a form. If the team name changes, create a new entity in the database and delete the old.
def editteam(request, team_name):
    try:
        team = Team.objects.get(team_name=team_name)
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                if form.data['team_name'] != team_name:
                    team.delete()
                    team = Team()
                    team.team_name = form.data['team_name']
                team.entry_name = form.data['entry_name']
                team.category = Category.objects.get(name=form.data['category'])
                team.registrar = request.user.registrar
                team.save()
                return redirect('/registrar/showqr/' + team.team_name)
        initial = {'team_name': team.team_name, 'category': team.category.name, 'entry_name': team.entry_name}
        form = RegistrationForm(initial=initial)
        context = {'form': form}
        return render(request, 'registrar/addteam.html', context)
    except:
        return redirect('addteam')

# Display the QR code for hte specified team.
def showqr(request, team):
    teamurl = "https://api.qrserver.com/v1/create-qr-code/?data=" + team + "&amp;size=400x400"
    context = {'header': 'Team ' + team,'qrurl': teamurl, 'redirect': '/registrar/home'}
    return render(request, 'core/showqr.html', context)
