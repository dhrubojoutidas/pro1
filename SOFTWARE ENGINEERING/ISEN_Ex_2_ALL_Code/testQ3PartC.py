##testQ3PartC.py

from Q3PartC import median 
import unittest
from unittest.mock import patch
from io import StringIO


class TestMedianFunction(unittest.TestCase):

    def testcase1(self): #v1 =M
        with patch('builtins.input', side_effect=['5', '3', '7']), \
             patch('sys.stdout',  new_callable=StringIO) as mock_stdout:
            result = median()
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, '5')
            self.assertEqual(result, 5)

    def testcase2(self): #  npn - interger input
        with patch('builtins.input', side_effect=['abc', '5', '8']), \
             patch('sys.stdout',  new_callable=StringIO) as mock_stdout:
            result = median()
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, 'Invalid input')
            self.assertIsNone(result)

    def testcase3(self): #all 0
        with patch('builtins.input', side_effect=['0', '0', '0']), \
             patch('sys.stdout',  new_callable=StringIO) as mock_stdout:
            result = median()
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, '0')
            self.assertEqual(result, 0)

    def testcase4(self): #v1 = M
        with patch('builtins.input', side_effect=['10', '15', '6']), \
             patch('sys.stdout',  new_callable=StringIO) as mock_stdout:
            result = median()
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, '10')
            self.assertEqual(result, 10) 


    def testcase5(self): #all value same
        with patch('builtins.input', side_effect=['6', '6', '6']), \
             patch('sys.stdout',  new_callable=StringIO) as mock_stdout:
            result = median()
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, '6')
            self.assertEqual(result, 6)

    def testcase6(self):
        with patch('builtins.input', side_effect=['0', '0', '0']), \
             patch('sys.stdout',  new_callable=StringIO) as mock_stdout:
            result = median()
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, '0')
            self.assertEqual(result, 0)                      

if __name__ == '__main__':
    unittest.main()
