import unittest 
import q2code 

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(q2code.fizzBuzz(), 'heloo')

if __name__ == '__main__':
    unittest.main()