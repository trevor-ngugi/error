import unittest
from app.models import Pitch

class PostModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """
    
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.pitch= Pitch(title = 'This heading', content = 'This body')


    def tearDown(self):
        Pitch.query.delete()



    def test_instance(self):
        self.assertTrue(isinstance(self.pitch, Pitch))



    def test_check_instance_variables(self):
        self.assertEquals(self.pitch.title,'This heading')
        self.assertEquals(self.pitch.content,'This body')