#Unittesting.py

import unittest
from unittest.mock import patch
from io import StringIO

from Q3PartA import funmean
from Q3PartB import El_COVID
from Q3PartC import  median

class AllTest(unittest.TestCase):

 #testcase 1 to testcase 6 is the testcode for median of 3 numbers  Q3.PartC.py
     
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



     # testfucntions for testing Covid doage  accordign to age Q3PartB.py
    def test_El_COVID(self):
        self.assertEqual(El_COVID(-1), "Invalid age")
        self.assertEqual(El_COVID(3), "Not eligible")
        self.assertEqual(El_COVID(10), "Eligible for 1 dose")
        self.assertEqual(El_COVID(15), "Eligible for 2 doses")
        self.assertEqual(El_COVID(20), "Eligible for 3 doses")
        self.assertEqual(El_COVID(46), "Eligible for optional dose")
        self.assertEqual(El_COVID(60), "Must take optional dose")
        self.assertEqual(El_COVID(85), "See your GP for eligibility")
        self.assertEqual(El_COVID(100), "Invalid age") 

    def test_funmean(self):  #  test code for  mean of 4 numbers Q3.PartA.py
        self.assertEqual(funmean(3,5,7,2),-1 )
        self.assertEqual(funmean (5,4,7,2 ), 4.5) 
        self.assertEqual(funmean (2,6,7,3) , -1)       
        self.assertEqual(funmean (5,3,1,6) , -1  )
        self.assertEqual(funmean(6,6,9,2), -1 )
        self.assertEqual(funmean (2,4,1,3) , -1)
        self.assertEqual(funmean(9,5,3,3), 5  ) 
        self.assertEqual(funmean(6,6,8,8) , -1 )               

if  __name__ == "__main__":
    unittest.main()



       