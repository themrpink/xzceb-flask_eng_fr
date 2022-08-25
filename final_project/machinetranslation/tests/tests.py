import unittest
from . import english_to_french
from . import french_to_english  
    

class TestTranslator(unittest.TestCase):
    def test_english_to_french_null(self):
        self.assertRaises(ValueError,english_to_french, None)
    def test_french_to_english_null(self):
        self.assertRaises(ValueError, french_to_english, None)
    def test_english_to_french(self):
        self.assertEqual("Bonjour", english_to_french("Hello"))
        self.assertIsNotNone
    def test_french_to_english(self):
        self.assertEqual("Hello", french_to_english("Bonjour"))
        
        
if __name__=='__main__':
    unittest.main()