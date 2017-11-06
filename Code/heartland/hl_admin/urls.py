from django.conf.urls import url
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
]
