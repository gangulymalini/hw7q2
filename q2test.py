import unittest 
import q2code 

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(q2code.leapyear(300), "is not a leap year")
    def test2(self):
        self.assertEqual(q2code.leapyear(400), "is a leap year")

if __name__ == '__main__':
    unittest.main()