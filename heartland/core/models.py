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

# Admin Relation: No realtions, stores admin credentials
class Admin(Judge):
    pass

# Team Relation: Stores team and entry information. Ternary relation with Judge and Score
class Team(models.Model):
    team_name = models.CharField(max_length=128, primary_key=True)
    entry_name = models.CharField(max_length=128)
    registrar = models.ForeignKey(Registrar)

# part of the ternary relation
class Judge_Team(models.Model):
    judge = models.OneToOneField(Judge, primary_key=True)
    team = models.OneToOneField(Team)

    class Meta:
        unique_together = ('judge', 'team')

# Score_Criterion Relation: Stores a specific scoring criterion, such as visuals or audio.
# Can be applied to multiple categories.
class Score_Criterion(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    scores = models.ManyToManyField(Judge_Team)

# Category Relation: 
class Category(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    criteria = models.ManyToManyField(Score_Criterion)

Team.category = models.ForeignKey(Category, on_delete=models.CASCADE)
