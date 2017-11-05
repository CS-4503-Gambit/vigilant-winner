from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/(?P<team_name>[\w\s]+)/$', views.judge_team, name='judge_team'),
]
