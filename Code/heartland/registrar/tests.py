from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

from core.models import *



class RegistrarTestCase(TestCase):



    #Test by Rongyao

    def setup(self):

        exec(open('populate.py').read())

        self.client = Client()

        self.client.login(username='registrar', password='registrar')



    # Test the home screen for registar

    # Test by Rongyao

    def test_registrar_home(self):

        self.setup()

        response = self.client.get('/registrar/home/')

        # Check that the response was successful

        self.assertEqual(response.status_code, 200)

        # Check all the buttons are present

        self.assertContains(response, "Add a Team")

        self.assertContains(response, "Registered Teams")



    # Test add a team to the database using a form

    # Test by Rongyao

    def test_addteam(request):

        self.setup()

        response = self.client.get('/registrar/addteam/')

        # Check that the response was successful

        self.assertEqual(response.status_code, 200)

        # Check that the fields are present

        self.assertContains(response, 'Category')

        self.assertContains(response, 'Team_name')

        self.assertContains(response, 'Entry_name')



    # Test display the teams

    # Test by Rongyao

    def test_display_teams(request):

        self.setup()

        response = self.client.get('/registrar/teams/')

        self.assertEqual(response.status_code, 200)

        # Check that the list header is present

        self.assertContains(response, 'My Teams')

        self.assertContains(response, 'Other Teams')
