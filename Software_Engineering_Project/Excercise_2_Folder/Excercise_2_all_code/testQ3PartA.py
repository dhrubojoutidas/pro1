#testQ3PartA.py ----- testing the Q3PartA.py 
import unittest
from Q3PartA import funmean

class testfunMean (unittest.TestCase) :
    def testcase1(self):
        self.assertEqual(funmean(3,5,7,2),-1 )

    def testcase2(self):
        self.assertEqual(funmean (5,4,7,2 ), 4.5   ) 

    def testcase3(self):
        self.assertEqual(funmean (2,6,7,3) , -1)       
    
    def testcase4(self):
        self.assertEqual(funmean (5,3,1,6) , -1  )

    def testcase5(self):
        self.assertEqual(funmean(6,6,9,2), -1 )

    def testcase6(self):
        self.assertEqual(funmean (2,4,1,3) , -1)

    def testcase7(self):
        self.assertEqual(funmean(9,5,3,3), 5  ) 


    def testcase8(self):
        self.assertEqual(funmean(6,6,8,8) , -1 )               


if  __name__ == "__main__":
    unittest.main()
