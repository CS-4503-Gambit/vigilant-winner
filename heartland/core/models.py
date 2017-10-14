from django.db import models

# User Relation: superclass to Registrar, Judge, Admin
class User(models.Model):
    username = models.CharField(max_length=128, primary_key=True)
    password = models.CharField(max_length=128)

    class Meta:
        abstract = True

# Registrar Relation: Relation with Team, many-to-one
class Registrar(User):
    pass

# Judge Relation: Ternary relation with Team and Score, many to many to many
class Judge(User):
    pass

# Admin Relation: No relations, stores admin credentials
class Admin(Judge):
    pass

# Team Relation: Stores team and entry information. Ternary relation with Judge and Score
class Team(models.Model):
    team_name = models.CharField(max_length=128, primary_key=True)
    entry_name = models.CharField(max_length=128)
    registrar = models.ForeignKey(Registrar)

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
    category = models.ForeignKey(Score_Criterion, on_delete=models.CASCADE)
    scores = models.ManyToManyField(Judge_Team)
    value = models.IntegerField(null=False)

# Category Relation: 
class Category(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    criteria = models.ManyToManyField(Score_Criterion)

Team.category = models.ForeignKey(Category, on_delete=models.CASCADE)
