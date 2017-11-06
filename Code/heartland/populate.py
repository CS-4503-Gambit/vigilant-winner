# Populates the databse with some users.
# Execute within the django shell

from core.models import *

# Admin
print('admin')
u = User()
u.username='admin'
u.set_password('heartland')
u.is_superuser=True
u.is_staff=True
u.save()

# Registrar
print('registrar')
u = User()
u.username='registrar'
u.set_password('registrar')
u.save()
r = Registrar()
r.user = u
r.save()

# Judge
print('judge')
u = User()
u.username = 'judge'
u.set_password('judge')
u.save()
j = Judge()
j.user = u
j.save()

# Criteria
print('criteria')
cr = Score_Criterion()
cr.name = 'Overall'
cr.save()
print('saved one')
cr = Score_Criterion()
cr.name = 'Graphics'
cr.save()
cr = Score_Criterion()
cr.name = 'Music'
cr.save()

# Category
print('category')
c = Category()
c.name = 'Video Games'
c.save()
print('adding crit')
c.criteria.add(Score_Criterion.objects.get(name='Overall'))
print('added crit')
c.criteria.add(Score_Criterion.objects.get(name='Graphics'))
c.criteria.add(Score_Criterion.objects.get(name='Music'))
c = Category()
c.name = 'FPS'
c.save()
c.criteria.add(Score_Criterion.objects.get(name='Overall'))
c.criteria.add(Score_Criterion.objects.get(name='Graphics'))

# Teams
t = Team()
t.team_name = 'Team'
t.entry_name = 'Entry'
t.registrar = r
t.category = c
t.save()
t = Team()
t.team_name = 'Team Two'
t.entry_name = 'Entry Two'
t.registrar = r
t.category = c
t.save()
