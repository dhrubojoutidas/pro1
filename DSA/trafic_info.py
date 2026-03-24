#
#traffic.py ----- implementation for traffic management system
#
#Auther : Dhrubo Jouti das Troyee
# Date:22/01/2024
#
#

#from DSAStack import DSAStack
#from DSAQueue import DSAQueue

from collections import deque
import timeit
import heapq
from DSAHeapM import *

 # class for graph representation of road network
class Graph:
    def __init__(self):
        self.adj_list = {} # for storing graph nodes and neighnours
        self.traffic_data = {} # for storign traffic data for ech edge

    # adding edge in graph
    def add_edge(self, start, end, distance, traffic_vol, road_capacity, congestion_level):
         # add the edge to the adjacent list
        if start not in self.adj_list:
            self.adj_list[start] = []
        self.adj_list[start].append((end, distance))

        if end not in self.adj_list:
            self.adj_list[end] = []
        self.adj_list[end].append((start, distance))  # Assuming the graph is undirected

        # Add traffic data for the edge
        edge_key = (start, end)

        self.traffic_data[edge_key] = {
            'traffic_vol': traffic_vol,
            'road_capacity': road_capacity,
            'congestion_level': congestion_level
        }
 # update traffic data for exiting edge
    def update_edge(self, start, end, traffic_vol, road_capacity, congestion_level):
        edge_key = (start, end)
        if edge_key in self.traffic_data:
            self.traffic_data[edge_key]['traffic_vol'] = traffic_vol
            self.traffic_data[edge_key]['road_capacity'] = road_capacity
            self.traffic_data[edge_key]['congestion_level'] = congestion_level
            return True
        return False


    def road_remove(self):
        print("Remove Road:")
        start = input("Enter the start location: ")
        end = input("Enter the end location: ")

        edge_key = (start, end)
        if edge_key in self.traffic_data:
            del self.traffic_data[edge_key]
            self.adj_list[start] = [(neighbor, distance) for neighbor, distance in self.adj_list[start] if neighbor != end]
            self.adj_list[end] = [(neighbor, distance) for neighbor, distance in self.adj_list[end] if neighbor != start]
            print(f"Road removed: {start} - {end}")
        else:
            print(f"No road found between {start} and {end}")

    def remove_intersection(self):
        intersection = input("Enter the name of the intersection to remove: ")

        if intersection in self.traffic_data:
        # Remove the intersection from the adjacency list
           del self.adj_list[intersection]

        # Remove all edges connected to the intersection
           for node, neighbors in self.adj_list.items():
                self.adj_list[node] = [(neighbor, distance) for neighbor, distance in neighbors if neighbor != intersection]

        # Remove the intersection from the traffic data
           del self.traffic_data[intersection]
           print(f"Intersection '{intersection}' removed successfully.")
        else:
             print(f"Intersection '{intersection}' not found.")


   # mehods to pritn a route with  trafffic info
    def print_route(self,algorithm, path):
           print(f"\n{algorithm} Path:")
           if path:
                for i in range(len(path) - 1):
                    start_node, end_node, traffic_info = path[i]
                    print(f"Edge: {start_node} - {end_node} | Traffic Volume: {traffic_info.get('traffic_vol', 'N/A')} | Road Capacity: {traffic_info.get('road_capacity', 'N/A')} | Congestion Level: {traffic_info.get('congestion_level', 'N/A')}")
           else:
                 print("No path found.")

    # methods to print  route found using breath  1st Search
    def print_bfs_route(self, start, end):
        bfs_path = self.bfs(start, end)
        self.print_route("BFS", bfs_path)
   
   # methods to print  route found using  depth  first Search
    def print_dfs_route(self, start, end):
        dfs_path = self.dfs(start, end)
        self.print_route("DFS", dfs_path)

    # this methods for finding the shortest parth
    def dijkstra(self, start, end):
          # Initialize distances to all nodes as infinity, except the start node
          distances = {node: float('infinity') for node in self.adj_list}
          distances[start] = 0

          # Priority queue to store nodes and their distances
          priority_queue = [(0, start)]
          # Dijkstra's algorithm
          while priority_queue:
               current_distance, current_node = heapq.heappop(priority_queue)
               # Skip nodes with outdated distances
               if current_distance > distances[current_node]:
                  continue
            
          # Update distances to neighbors and enqueue them
          for neighbor, edge_distance in self.adj_list[current_node]:
               total_distance = current_distance + edge_distance

               if total_distance < distances[neighbor]:
                   distances[neighbor] = total_distance
                   heapq.heappush(priority_queue, (total_distance, neighbor))

         # Reconstruct the shortest path
          path = self._Reconstruct_path(start, end, distances)
          return path
  #  helper methods to reconstaruct the shortest path
    def _Reconstruct_path(self, start, end, distances):

        # Reconstruct the shortest path from end to start
         path = []
         current_node = end
         while current_node != start:
              path.append(current_node)
              neighbors = self.adj_list[current_node]
              min_neighbor = self._distance_min_neighbor(neighbors, distances)
              current_node = min_neighbor[0]

         path.append(start)
         return path[::-1]
  
    def _distance_min_neighbor(self, neighbors, distances):
        # Find the neighbor with the minimum distance
        min_distance = float('infinity')
        min_neighbor = None

        for neighbor, edge_distance in neighbors:
            total_distance = distances[neighbor] + edge_distance
            if total_distance < min_distance:
                min_distance = total_distance
                min_neighbor = (neighbor, edge_distance)

        return min_neighbor

    



   # addd  new location  tot he graph
    def location_add(self, location):
        if location not in self.adj_list:
            self.adj_list[location] = []

  # adding nrew ontersaction to the graph
    def new_intersection_add(self):
        print("Add New Intersection:")
        new_intersection = input("Enter the name of the new intersection: ")
        self.location_add(new_intersection)
        print(f"New intersection added: {new_intersection}")
   # add path in the graph
    def add_path(self, start, end, distance):
        if start in self.adj_list and end in self.adj_list:
            self.adj_list[start].append((end, distance))
            self.adj_list[end].append((start, distance))

    # methods to dispaly adjacany list
    def display_adj_list(self):
        # Display the adjacency list of the graph
        for node, neighbors in self.adj_list.items():
            print(f"{node} -> {', '.join([f'{neighbor[0]} ({neighbor[1]} miles)' for neighbor in neighbors])}")

 # methods to display traffic data for a path
    def display_traffic_data(self, path):
        for i in range(len(path) - 1):
            edge_key = (path[i], path[i + 1])
            traffic_info = self.traffic_data.get(edge_key, {})
            print(f"Edge: {path[i]} - {path[i + 1]} | Traffic Volume: {traffic_info.get('traffic_vol', 'N/A')} | Road Capacity: {traffic_info.get('road_capacity', 'N/A')} | Congestion Level: {traffic_info.get('congestion_level', 'N/A')}")
    



    # BFS implementation
            
    def dfs(self, start, end):
        visited = set()
        stack = [(start, [])]

        while stack:
            current_node, path = stack.pop()

            if current_node not in visited:
                visited.add(current_node)

                if current_node == end:
                    return path + [current_node]

                for neighbor, distance in self.adj_list[current_node]:
                    if neighbor not in visited:
                        edge_key = (current_node, neighbor)
                        traffic_info = self.traffic_data.get(edge_key, {})
                        stack.append((neighbor, path + [(current_node, neighbor, traffic_info)]))

        return None



    def bfs(self, start, end):
       visited = set()
       queue = deque([(start, [])])

       while queue:
            current_node, path = queue.popleft()

            if current_node not in visited:
                visited.add(current_node)

                if current_node == end:
                    return path + [current_node]

                for neighbor, distance in self.adj_list[current_node]:
                   if neighbor not in visited:
                        edge_key = (current_node, neighbor)
                        traffic_info = self.traffic_data.get(edge_key, {})
                        queue.append((neighbor, path + [(current_node, neighbor, traffic_info)]))   #[current_node]))


       return None
   # methods for mdify traffic flow restriction
    def traffic_flow_modify(self):
        print("Modify Traffic Flow Restrictions:")
        start= input("Enter the start location: ")
        end= input("Enter the end location: ")

        if start in self.adj_list and end in self.adj_list:
            traffic_vol = int(input("Enter the new traffic volume: "))
            road_capacity = int(input("Enter the new road capacity: "))
            congestion_level = input("Enter the new congestion level: ")

            if self.update_edge(start, end, traffic_vol, road_capacity, congestion_level):
                print(f"Traffic data updated for {start} - {end}")
            else:
                print(f"No existing road found between {start} and {end}")
        else:
            print(f"At least one of the locations does not exist in the traffic network.")
   # methods for  searching a specific route   using a  chosen algorithms
    def specific_route_search(self):
        print("Search Specific Route:")
        start = input("Enter the start location: ")
        end= input("Enter the end location: ")

        algorithm = input("Choose algorithm (BFS/DFS): ").upper()
        if algorithm == "BFS":
            path = self.bfs(start, end)
        elif algorithm == "DFS":
            path = self.dfs(start, end)
        else:
            print("Invalid algorithm choice.")
            return

        if path:
            self.print_route(algorithm, path)
        else:
            print("No path found.")

 # class for a hashtable for storeing traffic  data
class TrafficHashTable():  #add_edge   update_edge(    display_traffic_data
    def __init__(self):
        self.traffic_data = {}

    def add_edge(self, start, end, traffic_vol, road_capacity, congestion_level):
        edge_key = (start, end)
        self.traffic_data[edge_key] = {
            'traffic_vol': traffic_vol,
            'road_capacity': road_capacity,
            'congestion_level': congestion_level
        }

    def update_edge(self, start, end, traffic_vol, road_capacity, congestion_level):
        edge_key = (start, end)
        if edge_key in self.traffic_data:
            self.traffic_data[edge_key]['traffic_vol'] = traffic_vol
            self.traffic_data[edge_key]['road_capacity'] = road_capacity
            self.traffic_data[edge_key]['congestion_level'] = congestion_level
            return True
        return False

    def display_traffic_data(self, path):
        for i in range(len(path) - 1):
            edge_key = (path[i], path[i + 1])
            traffic_info = self.traffic_data.get(edge_key, {})
            print(f"Edge: {path[i]} - {path[i + 1]} | Traffic Volume: {traffic_info.get('traffic_vol', 'N/A')} | Road Capacity: {traffic_info.get('road_capacity', 'N/A')} | Congestion Level: {traffic_info.get('congestion_level', 'N/A')}")


 #  methods for reading   "traffic_data.txt "" file

def read_traffic_data(file_path, traffic_data_structure):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue

            split_line = [comp.strip() for comp in line.split(',')]

            if len(split_line) == 4:
                road_segment, traffic_vol, road_capacity, congestion_level = split_line
                traffic_data_structure.add_edge( *road_segment.split('-'), int(traffic_vol), int(road_capacity), congestion_level)
            else:
                print(f"Invalid traffic data line: {line}")

 # methods for  reading traffic_netwrk.txt" file
def network_graph_file(file_path, graph, traffic_data_structure): 
        with open(file_path, 'r') as file:
           for line in file:
               if line.startswith('#') or not line.strip():
                  continue

               split_line = [comp.strip() for comp in line.split(',')]

               if len(split_line) == 3:
                  start, end, distance = split_line
                  graph.add_edge(start, end, int(distance), 0, 0, 'N/A')  # Add default traffic data
                  traffic_data_structure.add_edge(start, end, 0, 0, 'N/A')

               else:
                  print(f"invalid line: {line}")







 #  methods for comapring the efficiency   between hashtable, array, linked list


def efficiency_comparison(graph, traffic_data_structure):
    # Measure time to access traffic data using hash table
    hashtable_S = timeit.default_timer()
    data_hashtable(graph)
    hashtable_E = timeit.default_timer()
    hashtable_time= hashtable_E - hashtable_S

    # Measure time to access traffic data using array
    array_S = timeit.default_timer()
    data_array(graph)
    array_E = timeit.default_timer()
    array_time = array_E - array_S

    # Measure time to access traffic data using linked list
    linked_list_S = timeit.default_timer()
    data_linked_list(graph)
    linked_list_E = timeit.default_timer() 
    linked_list_time = linked_list_E -linked_list_S

    print("-----Efficiency Comparison----:")
    print(f"Hash Table Time: {hashtable_time:.10f} seconds")
    print(f"Array Time: {array_time:.10f} seconds")
    print(f"Linked List Time: {linked_list_time:.10f} seconds")



def data_hashtable(graph):
    for edge_key in graph.traffic_data:
        traffic_info = graph.traffic_data[edge_key]

def data_array(graph):
    for edge_key in graph.traffic_data:
        traffic_info = graph.traffic_data[edge_key]

def data_linked_list(graph):
    for edge_key in graph.traffic_data:
        traffic_info = graph.traffic_data[edge_key]



# methods for handinling traffic data priority queue
class Traffic_Priority_Queue () :
    # contsactor : Inilializing an empty heap for the p quue
    def __init__(self): 
        self.heap = []
    ## methods for add item (edgee tarffic data) to the p.queue
    def push(self, item):
        self.heap.append(item)
        self._heapify_up()
    # methods for  remove and return item  with highjest priority(max traffic volumn)
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        return root
   # methods to insert an edge with traffic volumn  into p queue
    def insert_edge(self, edge, traffic_vol):
    
         new_element = (traffic_vol, edge)
         self.heap.append(new_element)
         self._heapify_up(len(self.heap) - 1)
 # methods for find and return edge with highest congestion level
    def find_highest_congestion_edge(self):
        if self.heap:
            return self.heap[0][1]
        return None
# Hepler methods for maintain max heap property
    def _heapify_up(self, index):
        while index > 0:
            parent_idx = (index - 1) // 2
            if self.heap[parent_idx] < self.heap[index]:
                # Swap elements if parent's priority is smaller
                self.heap[parent_idx], self.heap[index] = self.heap[index], self.heap[parent_idx]
                index = parent_idx
            else:
                break

# hepler methids for maintaining
    def _heapify_down(self):
        index = 0
        while True:
            LC_idx = 2 * index + 1
            RC_idx = 2 * index + 2
            largest = index

            if LC_idx < len(self.heap) and self.heap[LC_idx] > self.heap[largest]:
                largest = LC_idx

            if RC_idx < len(self.heap) and self.heap[RC_idx] > self.heap[largest]:
                largest = RC_idx

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

 # methods for opeoning file traffic_dataa.txt
with open( "traffic_data.txt" , 'r') as file:
        traffic_priority_queue =Traffic_Priority_Queue()
        for line in file: # iter ech line in the  file
            if line.startswith('#') or not line.strip():
                continue

            split_line = [comp.strip() for comp in line.split(',')]

            if len(split_line) == 4:
                road_segment, traffic_vol, road_capacity, congestion_level = split_line
                 # inserteddge (rod-seg) into  p.queue with traffic vol
                traffic_priority_queue.insert_edge(road_segment.split('-'), int(traffic_vol))  #, int(road_capacity), congestion_level)
 
 # Find the edge with the highest congestion level
congestion_edge_highest = traffic_priority_queue.find_highest_congestion_edge()
print(f"Highest Congestion Edge: {congestion_edge_highest}")



if __name__ == "__main__":
    file_path = "traffic_network.txt"
    #traffic_file_path = "traffic_data.txt"
    traffic_data_structure = TrafficHashTable()
    graph = Graph()


    # Construct graph from road network file
    network_graph_file(file_path, graph, traffic_data_structure)

    # Add traffic data to the graph
    traffic_data_file_path = "traffic_data.txt"
    read_traffic_data(traffic_data_file_path, traffic_data_structure)





