from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from .models import Registrar, Judge

# Create your views here.
def login(request):
    template = loader.get_template('core/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login_success(request):
    if request.user.is_superuser:
        return redirect("/admin/home")
    try:
        if request.user.registrar is not None:
            return redirect("/registrar/home")
    except Registrar.DoesNotExist:
        try:
            if request.user.judge is not None:
                return redirect("/judge/home")
        except Judge.DoesNotExist:
            return login(request)
