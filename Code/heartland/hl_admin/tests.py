from django.test import TestCase

# Create your tests here.
class AdminTestCase(TestCase):
    def setup(self):
        pass

    def testScores():
        exec(open('populate.py').read())
