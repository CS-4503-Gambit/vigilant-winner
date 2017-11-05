from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^db/', admin.site.urls),
    url(r'^scores/$', views.scores, name='scores'),
    url(r'^scores/(?P<category>[\w\s]+)/$', views.category_score, name='category_score')
]
