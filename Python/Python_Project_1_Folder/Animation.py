import random
import matplotlib.pyplot as plt
import csv
import sys


# Define constants for map size
map_width= 100
map_height  = 100


# class of  for Humans, Vampires, and Items


class Vampire:
    def __init__(self, human_health):
        self.health = human_health
        self.x = random.randint(0, map_width - 1)
        self.y = random.randint(0, map_height  - 1)

    def movement(self):
        self.x += random.randint(-8, 8)
        self.y += random.randint(-8, 8) #  vimpare can move up to 8 step direction 
        self.x = max(0, min(map_width - 1, self.x))
        self.y = max(0, min(map_height   - 1, self.y))

    def interaction(self, other):
        if isinstance(other, Human) and random.random() < 0.7:
            other.health = 0
            print(" Human has killed vampire")
            return True
        return False

class Human:
    def __init__(self):
        self.health = 100
        self.age = random.randint(10, 50)
        self.x = random.randint(0,map_width- 1)
        self.y = random.randint(0, map_height   - 1)

    def movement(self):
        self.x += random.randint(-4, 4)  #  human can move up to 4 space direction 
        self.y += random.randint(-4, 4)
        self.x = max(0, min(map_width - 1, self.x))
        self.y = max(0, min(map_height  - 1, self.y))

    def interaction(self, other):
        if isinstance(other, Human):
            if random.random() < 0.4:  #Human and human interaction:  40%chance
                self.health += 20       # 20% gain 
                other.health -= 20       # 20% loss
                print("Human and human interaction 40% chances : ")
            else:
                self.health += 10
                other.health += 10
                print("humans help and both gain 10 health, as 60% human helps each other")




class Water:
    def __init__(self):
        self.health = 50
        self.x = random.randint(0,map_width - 1)
        self.y = random.randint(0, map_height   - 1)
        print("Human  just drank water:")



class Food:
    def __init__(self):
        self.health = 30
        self.x = random.randint(0, map_width - 1)
        self.y = random.randint(0, map_height   - 1)
        print(" human has eaten the food  and gain 50 health")


class Garlic:
    def __init__(self):
        self.health = 100
        self.x = random.randint(0, map_width - 1)
        self.y = random.randint(0, map_height   - 1)
        print("human has eaten the  garlic")





 # initializtion  interactions_of_performance fuction
def interactions_of_performance(humans, vampires, items):
    for human in humans:
        for vampire in vampires:
            if do_v(human, vampire):
                human.interaction(vampire)
                if vampire.interaction(human):
                    vampires.remove(vampire)
                    break

 # Implecation of  interactions between humans and items
    for human in humans:
        for item in items:
            if do_v(human, item):
                human.interaction(item)
                if human.interaction(item):
                    humans.remove(human)
                    break

   
 #  implication of interaction between vampires & iteams
    for vampire in vampires:
        for item in items:
            if do_v(vampire, item):
                vampire.interaction(item)
                if vampire.interaction(item):
                    vampires.remove(vampire)
                    break



# fuction to initialization of humans, vampirres, iteams for simualtion

def initialize_simulation(initial_human_count, initial_vampire_count):
    humans = [Human() for _ in range(initial_human_count)]
    vampires = [Vampire(human.health) for human in random.sample(humans, initial_vampire_count)]
    items = [random.choice([Food(), Water(), Garlic()]) for _ in range(initial_human_count + initial_vampire_count)]
    
    return humans, vampires, items





 #calculate the difference between x and y coordinator between  axis_1 , axis_2
def do_v( axis_1 , axis_2):
    return abs( axis_1.x - axis_2.x) <= 1 and abs( axis_1.y - axis_2.y) <= 1

     
 
                
           
def update_positions(Human):
    for human in Human:
        human.movement()
    

def update_positions(Vampire):
    for vampire in Vampire:
        vampire.movement()

# Function to visualize the simulation of the fact 

def visualize_simulation(humans, vampires, items, timestep):
   
    # plotting for the interaction between human, vampire, food, water, garlic 

    
    garlic_x = [item.x for item in items if isinstance(item, Garlic)]
    garlic_y = [item.y for item in items if isinstance(item, Garlic)]
    plt.scatter(garlic_x, garlic_y, color='gray', marker='^',  s= 75,label='Garlic')  

    human_scatter = plt.scatter([human.x for human in humans], [human.y for human in humans], color='green', s= 60, label='Humans', marker = "o")
    vampire_scatter = plt.scatter([vampire.x for vampire in vampires], [vampire.y for vampire in vampires],  s= 65, marker = "o",color='red', label='Vampires')

    water_x = [item.x for item in items if isinstance(item, Water)]
    water_y = [item.y for item in items if isinstance(item, Water)]
    plt.scatter(water_x, water_y, color='blue', marker='s',s= 100, label='Water')

    food_x = [item.x for item in items if isinstance(item, Food)]
    food_y = [item.y for item in items if isinstance(item, Food)]
    plt.scatter(food_x, food_y, color='brown', marker='s',  s= 70, label='Food')

 

    plt.title( "simulation between human, vampire, food, water, garlic iteams")
    plt.xlabel("x_values")
    plt.ylabel("Y_alues")
    plt.legend()

    plt.xlim(0, map_width - 1)
    plt.ylim(0, map_height   - 1)

    plt.pause(1)  # Pause for a short while to see the animation
    plt.clf()
    
    for i in range(21):
        print("\n ### TIMESTEP ",i, "###")
    

# Function to save simulation data to a CSV file
def simulation_data_save(filename, initial_human_count, initial_vampire_count, final_human_count, final_vampire_count):
    with open(filename, 'a') as file:
        file.write(f"{initial_human_count},{initial_vampire_count},{final_human_count},{final_vampire_count}\n")







# Main simulation loop
def main(initial_human_count, initial_vampire_count, num_timesteps):
    humans, vampires, items = initialize_simulation(initial_human_count, initial_vampire_count)
    initial_human_count = len(humans)
    initial_vampire_count = len(vampires)
 



   
    # Inside the main simulation loop
    for timestep in range(num_timesteps):
        update_positions(humans)
        update_positions(vampires)
        interactions_of_performance(humans, vampires, items)
        visualize_simulation(humans, vampires, items, timestep)
    
    final_human_count = len(humans)
    final_vampire_count = len(vampires)
  
 
    # Save the final state and simulation data to CSV
    simulation_data_save("simulation_output.csv", initial_human_count, initial_vampire_count, final_human_count, final_vampire_count)


 
# Command-line parameters
initial_human_count = 20
initial_vampire_count = 20
num_timesteps = 21



if __name__ == '__main__':
     main(initial_human_count, initial_vampire_count, num_timesteps)

#if __name__ == '__main__':
     #main()








