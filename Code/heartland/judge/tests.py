from django.test import TestCase, Client
from core.models import *
#import unittest

# Create your tests here.
class judge_tests(TestCase):
    #Sets up database and checks to see if an empty judge home page will load
    def test_judge_home_empty(self):
        u = User()
        u.username='judge'
        u.set_password('judge')
        u.save()
        j = Judge()
        j.user = u
        j.save()
        cr = Score_Criterion()
        cr.name = 'Overall'
        cr.save() 
        cr = Score_Criterion()
        cr.name = 'Graphics'
        cr.save()
        cr = Score_Criterion()
        cr.name = 'Music'
        cr.save()
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
        self.client = Client()
        self.client.login(username="judge", password="judge")
        response = self.client.get('/judge/home')
        #Check that response is 200
        self.assertEqual(response.status_code, 200)
       
    #Sets up database and checks to see if a judge home page will load with only unjudged teams
    def test_judge_home_unjudged(self):
        u = User()
        u.username='judge'
        u.set_password('judge')
        u.save()
        j = Judge()
        j.user = u
        j.save()
        cr = Score_Criterion()
        cr.name = 'Overall'
        cr.save() 
        cr = Score_Criterion()
        cr.name = 'Graphics'
        cr.save()
        cr = Score_Criterion()
        cr.name = 'Music'
        cr.save()
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
        u = User()
        u.username='registrar'
        u.set_password('registrar')
        u.save()
        r = Registrar()
        r.user = u
        r.save()
        t = Team()
        t.team_name = 'Team'
        t.entry_name = 'Entry'
        t.registrar = r
        t.category = Category.objects.get(name="FPS")
        t.save()
        self.client = Client()
        self.client.login(username="judge", password="judge")
        response = self.client.get('/judge/home')
        #Check that response is 200
        self.assertEqual(response.status_code, 200)
        #checks if headings are correctly hidden/shown
        self.assertNotContains(response, "Already Judged Teams")
        self.assertContains(response, "Teams Left to Judge")
        #checks if correct number of entries are displayed
        self.assertEqual(len(response.context['unjudged']), 1)
        self.assertEqual(len(response.context['judged']), 0)

    #Sets up database and checks to see if a judge home page will load with unjudged and judged teams
    def test_judge_home_unjudged_and_judged(self):
        u = User()
        u.username='judge'
        u.set_password('judge')
        u.save()
        j = Judge()
        j.user = u
        j.save()
        cr = Score_Criterion()
        cr.name = 'Overall'
        cr.save() 
        cr = Score_Criterion()
        cr.name = 'Graphics'
        cr.save()
        cr = Score_Criterion()
        cr.name = 'Music'
        cr.save()
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
        u = User()
        u.username='registrar'
        u.set_password('registrar')
        u.save()
        r = Registrar()
        r.user = u
        r.save()
        t = Team()
        t.team_name = 'Team'
        t.entry_name = 'Entry'
        t.registrar = r
        t.category = Category.objects.get(name="FPS")
        t.save()
        t = Team()
        t.team_name = 'Team Two'
        t.entry_name = 'Entry Two'
        t.registrar = r
        t.category = Category.objects.get(name="FPS")
        t.save()
        jt = Judge_Team()
        jt.team = t
        jt.judge = j
        jt.save()
        s = Score()
        s.judge_team = jt
        s.criterion = cr
        s.value = 8
        s.save()
        self.client = Client()
        self.client.login(username="judge", password="judge")
        response = self.client.get('/judge/home')
        #Check that response is 200
        self.assertEqual(response.status_code, 200)
        #checks if headings are correctly hidden/shown
        self.assertContains(response, "Already Judged Teams")
        self.assertContains(response, "Teams Left to Judge")
        #checks if correct number of entries are displayed
        self.assertEqual(len(response.context['unjudged']), 1)
        self.assertEqual(len(response.context['judged']), 1)
        
    #Sets up database and checks to see if a judge home page will load with only judged teams
    def test_judge_home_judged(self):
        u = User()
        u.username='judge'
        u.set_password('judge')
        u.save()
        j = Judge()
        j.user = u
        j.save()
        cr = Score_Criterion()
        cr.name = 'Overall'
        cr.save() 
        cr = Score_Criterion()
        cr.name = 'Graphics'
        cr.save()
        cr = Score_Criterion()
        cr.name = 'Music'
        cr.save()
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
        u = User()
        u.username='registrar'
        u.set_password('registrar')
        u.save()
        r = Registrar()
        r.user = u
        r.save()
        t = Team()
        t.team_name = 'Team'
        t.entry_name = 'Entry'
        t.registrar = r
        t.category = Category.objects.get(name="FPS")
        t.save()
        jt = Judge_Team()
        jt.team = t
        jt.judge = j
        jt.save()
        s = Score()
        s.judge_team = jt
        s.criterion = cr
        s.value = 8
        s.save()
        self.client = Client()
        self.client.login(username="judge", password="judge")
        response = self.client.get('/judge/home')
        #Check that response is 200
        self.assertEqual(response.status_code, 200)
        #checks if headings are correctly hidden/shown
        self.assertContains(response, "Already Judged Teams")
        self.assertNotContains(response, "Teams Left to Judge")
        #checks if correct number of entries are displayed
        self.assertEqual(len(response.context['unjudged']), 0)
        self.assertEqual(len(response.context['judged']), 1)
        
    #Sets up database and checks to see if a judge scoring page will load        
    def test_judge_Score(self):
        u = User()
        u.username='judge'
        u.set_password('judge')
        u.save()
        j = Judge()
        j.user = u
        j.save()
        cr = Score_Criterion()
        cr.name = 'Overall'
        cr.save() 
        cr = Score_Criterion()
        cr.name = 'Graphics'
        cr.save()
        cr = Score_Criterion()
        cr.name = 'Music'
        cr.save()
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
        u = User()
        u.username='registrar'
        u.set_password('registrar')
        u.save()
        r = Registrar()
        r.user = u
        r.save()
        t = Team()
        t.team_name = 'Team'
        t.entry_name = 'Entry'
        t.registrar = r
        t.category = Category.objects.get(name="FPS")
        t.save()
        self.client = Client()
        self.client.login(username="judge", password="judge")
        response = self.client.get('/judge/teams/Team/')
        #Check that response is 200
        self.assertEqual(response.status_code, 200)

        