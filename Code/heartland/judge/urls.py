from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^(?P<team_name>[\w\s]+)/$', views.judge_team, name='judge_team'),
    url(r'^(?P<team_name>[\w\s]+)/submit_score', views.submit_score, name='submit_score'),
]
