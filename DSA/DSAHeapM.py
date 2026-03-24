#DSAHeap.py ---  done
import numpy as np


class DSAHeap : 
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, start, end, distance):
        self.adjacency_list[start].append((end, distance))
        self.adjacency_list[end].append((start, distance))

    def __init__ (self) :
        self.heapArr = np.empty(0, dtype = int)
        self.count = 0

    def isEmpty (self):
        return self.count == 0

    def getCount(self):
        return self.count
    
    

    #if u  are doing hydreting fcuntion, it do not take any thigs.. if u are doing recurvive fucntion it takes many things klike whwre u want to call the recurvice funtion)index)
    def tickleUp(self, heapArr, index): # when u made the newnode from top,restore heap property,by sesrching or ulterring top to bottm
        parent_idx = (index -1) //  2   # add  somthign at the top so u need toc heck the patresnts 
        
        if index >0 :#if  index is > 0 menas elemnts is not at the top of the heap
           if  self.heapArr[index] > self.heapArr[parent_idx] : #keep compareing the value of the eleement witht he parents' indx
                  temp = self.heapArr[index]
                  self.heapArr[index] = self.heapArr[parent_idx]
                  self.heapArr[parent_idx] = temp
                  self.tickleUp(self.heapArr, parent_idx) # keep  continuw untill it reach the bottm
 # cz the node we are adding is learfer than parents, so it swap with parents, our heap is amx heapso maximum value will be on the top



    def tickleDown(self, heapArr, index, count): # tickel down operation  compare lC, Rc.. ficnout theindx of the largest value and then swap
        left_idx =(index * 2) +1
        right_idx = left_idx +1

        if left_idx <self.count :
            larger_idx = left_idx
            if right_idx < self.count :
                 if self.heapArr[left_idx] < self.heapArr[right_idx]:
                     larger_idx   = right_idx 
            if self.heapArr[larger_idx] > self.heapArr[index]: #check if the largerr value  is gtretter then the value itse;f
                   temp = self.heapArr[larger_idx]
                   self.heapArr[larger_idx] = self.heapArr[index]
                   self.heapArr[index] = temp
                   self.tickleDown(self.heapArr,larger_idx, self.count)

    def remove(self):
        if  self.isEmpty():
             print("Ur heap is empty!!!")
        else:  # if not empty
            delNode =self.heapArr[0] #very 1st value go the ndoe
            self.heapArr[0] = self.heapArr[self.count - 1] # copy the  valye of the last node here of the last root node
            *self.heapArr, = self.heapArr #del self.heapArr[-1] #we del the last ele of the heap
            self.count -= 1 # update
            self.tickleDown (self.heapArr, 0 , self.count)
            return delNode

    def add(self, value):
        # our heapo now is a array, righty,  and arrayb has fixed size, u can not add according to ur wish,, u ahve to do it by index to index
        newheap = np.empty(self.count +1 , dtype = int)
        for i in range (self.count) : #(len(self.heapArr)):
             newheap[i] = self.heapArr[i]
        newheap[self.count] = value
        self.heapArr = newheap
        self.count += 1
        self.tickleUp(self.heapArr, self.count - 1)
        # Print all elements
        #print("Elements after adding " + str(value) + ": " + str(self.heapArr))
        print(str(value) )

        
    def  heapify (self, heapArr,count) : # before impilemt the heapsortt we need to immplement thsi
        # cz heaify will makwe sure theat the root node has the maximum vaalue in the array
        for i in range((self.count //2) -1, 0,1): # cz i start from the npone leaft node. go bzackwards
              self.trickleDown(self, heapArr, i, self.count)
        return self.heapArr      
        
    def heapSort(self,heapArr, count):
       
        self.heapArr =  self.heapify(self.heapArr, self.count)# inialize a heap array by caling heapify as heapyfy insure that the node contains in maximum value of the array    
        for i in range(self.count -1, 0, -1) :
             temp = self.heapArr[0]
             self.heapArr[0] = self.heapArr[i]
             self.heapArr[i] =  temp # swaping
             self.tickleDown(self.heapArr[0:i], 0,i)
        return self.heapArr
             
    def getmaxValue(self):
         return self.heapArr[0] # max value is very 1st value of ur hep array
  

    def getMaxChild(self, index):
         if (index*2) + 1 < self.count :
            left_child = index * 2 + 1
            right_child = (index * 2) + 2

            if right_child < self.count and self.heapArr[left_child] < self.heapArr[right_child]:
                 return right_child
            else:
                 return left_child
         else:
            return index * 2
         #     return index* 2 + 1
         #else:
          #     if self.heapArr[i*2] > self.heapArr[(i*2) + 1]:
           #           return i*2
            #   else:
             #        return(i*2) +1
                
               
    def getMinValue(self):
         pass

    def display (self):
         for i in  self.heapArr:
             print(i)
            