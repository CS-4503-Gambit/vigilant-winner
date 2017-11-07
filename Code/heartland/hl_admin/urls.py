from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^db/', admin.site.urls),
    url(r'^scores/$', views.categories, name='categories'),
    url(r'^scores/(?P<category>[\w\s]+)/$', views.criteria, name='criteria'),
    url(r'^scores/(?P<category>[\w\s]+)/(?P<criteria>[\w\s]+)$', views.scores, name='scores'),
    url(r'^judges/$', views.judges, name='judges'),
    url(r'^judges/(?P<judge_name>[\w\s]+)/$', views.judge_stats, name='judge_stats'),
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^viewqr/$', views.viewqr, name='viewqr'),
    url(r'^viewqr/reg/(?P<registrar_name>[\w\s]+)', views.qr_registrar, name='qr_registrar'),
    url(r'^viewqr/judge/(?P<judge_name>[\w\s]+)', views.qr_judge, name='qr_judge'),
    url(r'^viewqr/team/(?P<team_name>.+)', views.qr_team, name='qr_team'),
]
