from django.contrib.auth.models import User
from django.db import models

# Registrar Relation: Relation with Team, many-to-one
class Registrar(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    password = models.CharField(max_length=128, null=False)

# Judge Relation: Ternary relation with Team and Score, many to many to many
class Judge(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    password = models.CharField(max_length=128, null=False)

# Team Relation: Stores team and entry information. Ternary relation with Judge and Score
class Team(models.Model):
    team_name = models.CharField(max_length=128, primary_key=True)
    entry_name = models.CharField(max_length=128, null=False)
    registrar = models.ForeignKey(Registrar, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)

# part of the ternary relation
class Judge_Team(models.Model):
    judge = models.ForeignKey(Judge, null=False)
    team = models.ForeignKey(Team, null=False)

    class Meta:
        unique_together = (('judge', 'team'),)

# Score_Criterion Relation: Stores a specific scoring criterion, such as visuals or audio.
# Can be applied to multiple categories.
class Score_Criterion(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

# Score Relation: Actual judging score, part of ternary relation
class Score(models.Model):
    criterion = models.ForeignKey(Score_Criterion, on_delete=models.CASCADE, null=False)
    judge_team = models.ForeignKey(Judge_Team, null=False)
    value = models.IntegerField(null=False)

    class Meta:
        unique_together = (('judge_team', 'criterion'))

# Category Relation: 
class Category(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    criteria = models.ManyToManyField(Score_Criterion)
    
    def __str__(self):
        return self.name
