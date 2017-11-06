from django.test import TestCase, Client
from core.models import *
import unittest

# Create your tests here.
class judge_tests(unittest.TestCase):
    def test_Setup(self):
        u = User()
        u.username='judge'
        u.set_password('judge')
        u.save()
        j = Judge()
        j.user = u
        j.save()
        
    def test_judge_home_empty(self):
        self.client = Client()
        self.client.login(username="judge", password="judge")
        response = self.client.get('/judge/home')
        #Check that response is 200
        self.assertEqual(response.status_code, 200)