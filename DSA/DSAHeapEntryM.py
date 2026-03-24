#DSAHeapEntry.py --  done 
class DSAHeapEntry:
    def __init__(self, priority = None, val = object) :
        self.priority =priority
        self.val = val


    def __getter__ (self,val): #getvalue
        return self.val 
    
    def __setter__(self, x): #setvalue
        self.val =  x

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority

 

  
      

