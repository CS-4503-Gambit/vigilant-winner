from django.test import TestCase

# Create your tests here.
class AdminTestCase(TestCase):
    def setup(self):
        exec(open('populate.py').read())

    def testScores():

