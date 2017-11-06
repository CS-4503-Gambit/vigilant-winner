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
r.password = 'registrar'
r.save()

# Judge
print('judge')
u = User()
u.username = 'judge'
u.set_password('judge')
u.save()
j = Judge()
j.user = u
j.password = 'judge'
j.save()

# Criteria
print('criteria')
cr = Score_Criterion()
cr.name = 'Overall'
cr.save()
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
c.criteria.add(Score_Criterion.objects.get(name='Overall'))
c.criteria.add(Score_Criterion.objects.get(name='Graphics'))
c.criteria.add(Score_Criterion.objects.get(name='Music'))
c = Category()
c.name = 'FPS'
c.save()
c.criteria.add(Score_Criterion.objects.get(name='Overall'))
c.criteria.add(Score_Criterion.objects.get(name='Graphics'))

# Teams
print('teams')
t = Team()
t.team_name = 'Team'
t.entry_name = 'Entry'
t.registrar = r
t.category = Category.objects.get(name='FPS')
t.save()
t = Team()
t.team_name = 'Team Two'
t.entry_name = 'Entry Two'
t.registrar = r
t.category = Category.objects.get(name='Video Games')
t.save()

# Judge_Team
print('judge_team')
jt = Judge_Team()
jt.team = t
jt.judge = j
jt.save()

# Score
print('score')
s = Score()
s.judge_team = jt
s.criterion = cr
s.value = 8
s.save()
