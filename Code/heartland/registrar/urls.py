from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home$', view.home, name='home'),
]
