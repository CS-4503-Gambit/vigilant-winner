from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^addteam/', views.addteam, name='addteam'),
    url(r'^showqr/(?P<team>[\s\w]+)', views.showqr, name='showqr'),
    url(r'^teams$', views.teams, name='teams'),
    url(r'^editteam/(?P<team_name>.+)', views.editteam, name='editteam'),
]
