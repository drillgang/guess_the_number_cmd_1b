import unittest,sys,os
import main

class Test_GTN(unittest.TestCase):
    
    def setUp(self):
        
        """
        init object
        """
        
        self.gtn=main.GTN()
        
    def test_ans_more(self):
        
        """
        test for func ans answer more
        """
        val=self.gtn.number+10
        self.gtn.ans(val)
        ans=sys.stdin.read()
    
    def test_ans_less(self):
        
        """
        test for func ans answer more
        """
        
    def test_ans_equally(self):
        
        """
        test for func ans answer equally
        """
    
    def test_guessnumber(self):
        
        """
        test for func guessnumber
        """
        
        pass
    
if __name__ == "__main__":
    unittest.main()
