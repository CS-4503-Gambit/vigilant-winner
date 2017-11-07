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
u = User()
u.username='reg'
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
u = User()
u.username = 'judy'
u.set_password('judge')
u.save()
j = Judge()
j.user = u
j.password = 'judge'
j.save()

# Criteria
print('criteria')
# Goes in all categories
cr = Score_Criterion()
cr.name = 'Overall'
cr.save()
# Goes in Video Game and Art
cr = Score_Criterion()
cr.name = 'Graphics'
cr.save()
# Goes in Video Game
cr = Score_Criterion()
cr.name = 'Music'
cr.save()
# Goes in Video Game
cr = Score_Criterion()
cr.name = 'Atmosphere'
cr.save()
# Goes in Art
cr = Score_Criterion()
cr.name = 'Style'
cr.save()

# Category
print('category')
c = Category()
c.name = 'Video Games'
c.save()
c.criteria.add(Score_Criterion.objects.get(name='Overall'))
c.criteria.add(Score_Criterion.objects.get(name='Graphics'))
c.criteria.add(Score_Criterion.objects.get(name='Music'))
c.criteria.add(Score_Criterion.objects.get(name='Atmosphere'))
c = Category()
c.name = 'Art'
c.save()
c.criteria.add(Score_Criterion.objects.get(name='Overall'))
c.criteria.add(Score_Criterion.objects.get(name='Graphics'))
c.criteria.add(Score_Criterion.objects.get(name='Style'))

# Teams
print('teams')
t = Team()
t.team_name = 'Bethesda Softworks'
t.entry_name = 'The Elder Scrolls V: Skyrim'
t.registrar = Registrar.objects.get(user__username='reg')
t.category = Category.objects.get(name='Video Games')
t.save()
t = Team()
t.team_name = 'Irrational Studios'
t.entry_name = 'BioShock Infinite'
t.registrar = Registrar.objects.get(user__username='registrar')
t.category = Category.objects.get(name='Video Games')
t.save()
t = Team()
t.team_name = 'Leonardo Da Vinci'
t.entry_name = 'Mona Lisa'
t.registrar = Registrar.objects.get(user__username='reg')
t.category = Category.objects.get(name='Art')
t.save()

# Judge_Team
print('judge_team')
def createJudgeTeam(team, judge):
    jt = Judge_Team()
    jt.team = team
    jt.judge = judge
    jt.save()

createJudgeTeam(Team.objects.get(team_name='Bethesda Softworks'), Judge.objects.get(user__username='judge'))
createJudgeTeam(Team.objects.get(team_name='Irrational Studios'), Judge.objects.get(user__username='judge'))
createJudgeTeam(Team.objects.get(team_name='Leonardo Da Vinci'), Judge.objects.get(user__username='judge'))
createJudgeTeam(Team.objects.get(team_name='Leonardo Da Vinci'), Judge.objects.get(user__username='judy'))
createJudgeTeam(Team.objects.get(team_name='Bethesda Softworks'), Judge.objects.get(user__username='judy'))

# Score
print('score')
def score(team_name, judge_name, scores):
    jt = Judge_Team.objects.get(team__team_name=team_name, judge__user__username=judge_name)
    team = Team.objects.get(team_name=team_name)
    for crit in team.category.criteria.all():
        print(judge_name, team_name, crit.name)
        s = Score()
        s.judge_team = jt
        s.criterion = crit
        s.value = scores.pop()
        s.save()

score('Bethesda Softworks', 'judge', [10, 10, 10, 10])
score('Irrational Studios', 'judge', [9, 7, 8, 8])
score('Leonardo Da Vinci', 'judge', [9, 8, 10])
score('Leonardo Da Vinci', 'judy', [7, 6, 5])
score('Bethesda Softworks', 'judy', [9, 10, 8, 10])
