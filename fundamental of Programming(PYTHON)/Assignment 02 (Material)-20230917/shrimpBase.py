import random
import matplotlib.pyplot as plt
from shrimp import Shrimp

XMAX = 1000
YMAX = 500
    
def main():
    shrimpList = []
    
    for i in range(20):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        shrimpList.append(Shrimp([randX, randY], [XMAX, YMAX]))
        #print(shrimpList[i])
     
    for i in range(20):
        print("\n ### TIMESTEP ",i, "###")
        xvalues = []
        yvalues = []
        sizes = []
        for shrimp in shrimpList:
            shrimp.stepChange()
            #print(shrimp)
            xvalues.append(shrimp.pos[0])
            yvalues.append(shrimp.pos[1])
            sizes.append(shrimp.getSize())
        
        plt.scatter(xvalues, yvalues, s=sizes)   # Note plt origin is bottom left 
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.pause(1)
        plt.clf()
    
if __name__ == "__main__":
    main()