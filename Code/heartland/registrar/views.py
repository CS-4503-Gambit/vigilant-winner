from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from core.models import *

# Create your views here.
def home(request):
    return render(request, 'registrar/home.html')

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
        context = { 'form': form }
        return render(request, 'registrar/addteam.html', context)

def showqr(request, team):
    teamurl = "https://api.qrserver.com/v1/create-qr-code/?data=" + team + "&amp;size=400x400"
    context = {'team': team, 'teamurl': teamurl}
    return render(request, 'registrar/showqr.html', context)
