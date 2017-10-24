from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Registrar)
admin.site.register(Judge)
admin.site.register(Admin)
admin.site.register(Team)
admin.site.register(Judge_Team)
admin.site.register(Score_Criterion)
admin.site.register(Score)
admin.site.register(Category)
