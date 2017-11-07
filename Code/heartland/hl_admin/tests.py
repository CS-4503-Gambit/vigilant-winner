from django.test import TestCase, Client
from core.models import *

# Create your tests here.
class AdminTestCase(TestCase):

    def setup(self):
        exec(open('populate.py').read())
        self.client = Client()
        self.client.login(username='admin', password='heartland')

    # Test the home screen for admin login
    def test_admin_home(self):
        self.setup()
        response = self.client.get('/admin/home/')
        # Check that the response was successful
        self.assertEqual(response.status_code, 200)
        # Check all the links are present
        self.assertContains(response, "Manage Database")
        self.assertContains(response, "View Results")
        self.assertContains(response, "View Judging Statistics")
        self.assertContains(response, "Create Judge or Registrar")
        self.assertContains(response, "View QR Codes")

    # Test the category display
    def test_category_display(self):
        self.setup()
        response = self.client.get('/admin/scores/')
        # Check that the response was successful
        self.assertEqual(response.status_code, 200)
        # Check that both categories are present
        self.assertContains(response, "Video Games")
        self.assertContains(response, "FPS")

    # Test the create user screen
    def test_create_user(self):
        self.setup()
        response = self.client.get('/admin/create_user/')
        # Check that the response was successful
        self.assertEqual(response.status_code, 200)
        # Check that the fields are present
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Type')
    
    # Test the View QR Code screen
    def test_view_qr(self):
        self.setup()
        response = self.client.get('/admin/viewqr/')
        # Check that the response was successful
        self.assertEqual(response.status_code, 200)
        # Check that each category is present
        self.assertContains(response, 'Registrars')
        self.assertContains(response, 'Judges')
        self.assertContains(response, 'Teams')
        # check that the specific entries are present
        self.assertContains(response, 'registrar')
        self.assertContains(response, 'judge')
        self.assertContains(response, 'Team')
        self.assertContains(response, 'Team Two')

    def test_judge_list(self):
        self.setup()
        response = self.client.get('/admin/judges/')
        # Check that the response was successful
        self.assertEqual(response.status_code, 200)
        # Check that the list header is present
        self.assertContains(response, 'List of Judges')
        # Check that the judge is present
        self.assertContains(response, 'judge')
