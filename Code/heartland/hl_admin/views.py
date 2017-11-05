from django.shortcuts import render
from django.http import HttpResponse
from core.models import *

# Create your views here.
def home(request):
    return render(request, 'admin/home.html')

def scores(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'admin/scores.html', context)

def category_score(request, category):
    c = Category.objects.get(name=category)
    context = {'category': c, 'teams': c.team_set.order_by()}
    return render(request, 'admin/score_category.html', context)
