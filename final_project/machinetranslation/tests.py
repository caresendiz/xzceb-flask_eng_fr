from translator import english_to_french, french_to_english
import unittest

class test_french_translator(unittest.TestCase):
    def test_french(self):
        #self.assertNotEqual(french_to_english(''), None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        

class test_english_translator(unittest.TestCase):
    def test_english(self):
        #self.assertNotEqual(english_to_french(''), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        


if __name__ == '__main__':
    unittest.main()