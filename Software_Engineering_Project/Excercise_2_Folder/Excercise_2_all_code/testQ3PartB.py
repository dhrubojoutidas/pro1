#testQ3PartB.py -----
from  Q3PartB import El_COVID

import unittest
class TestE1COVID (unittest.TestCase) :
    
    def testcase1(self):
        self.assertEqual(El_COVID(-1), "Invalid age")
    def testcase2(self):
        self.assertEqual(El_COVID(3),"Not eligible")

    def testcase3(self):
        self.assertEqual(El_COVID(10),"Eligible for 1 dose") 

    def testcase4(self):
        self.assertEqual(El_COVID(15),"Eligible for 2 dose")       
    
    def testcase5(self):
        self.assertEqual(El_COVID(20),"Eligible for 3 dose")

    def testcase6(self):
        self.assertEqual(El_COVID(46), "Eligible for optional dose""Must take optional dose")

    def testcase7(self):
        self.assertEqual(El_COVID (60),"Must take optional dose")

    def testcase8(self):
        self.assertEqual(El_COVID(85),"See your GP for eligibility") 


    def testcase9(self):
        self.assertEqual(El_COVID(100) ,"Invalid age" ) 
    def testcase10(self):
        self.assertEqual(El_COVID(-1) ,"Invalid age"  )                    


if  __name__ == "__main__":
    unittest.main()

