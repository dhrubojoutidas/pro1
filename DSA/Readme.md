# 🚦 Traffic Optimization System (DSA Project)

## 📌 Overview

This project is a **Traffic Management and Optimization System** developed using **Python**.
It applies core **Data Structures and Algorithms (DSA)** concepts such as Graphs, BFS, DFS, Hash Tables, Heaps, and Dijkstra’s Algorithm to improve urban traffic flow.

---

## 🖼️ Project Preview

<img width="800" alt="Traffic System" src="https://via.placeholder.com/800x400.png?text=Traffic+Optimization+System" />

---

## 📝 Deliverables

### 📄 1. Project Report

* [DSA Assignment Report](DSA_assinm,et_report_90028995.pdf)

---

### 💻 2. Source Code Files

* [traffic_info.py](trafic_info.py)
* [DSAHeapM.py](DSAHeapM.py)
* [DSAHeapEntryM.py](DSAHeapEntryM.py)
* [testharness.py](testharness)

---

### 📂 3. Input Data Files

* [traffic_network.txt](traffic_network.txt)
* [traffic_data.txt](traffic_data.txt)

---

## ⚙️ Features

### 🔹 Graph Construction

* Builds traffic network using adjacency list
* Input from `traffic_network.txt` 

### 🔹 Route Optimization

* BFS (shortest path)
* DFS (exploration)
* Dijkstra’s Algorithm (advanced shortest path)

### 🔹 Dynamic Traffic Management

* Add/remove roads
* Modify traffic data
* Search routes dynamically

### 🔹 Data Handling

* Hash Tables for fast lookup
* Efficiency comparison (Hash vs Array vs Linked List)

### 🔹 Priority Queue System

* Heap-based priority queue
* Finds highest congestion routes

---

## ▶️ How to Run

```bash
python testharness.py
```

---

## 🎮 Menu Options

From your program:

```
1. Display Adjacency List  
2. Find Route using BFS  
3. Find Route using DFS  
4. Add New Location  
5. Add New Path  
6. Update Traffic Data  
7. Compare Data Structures  
...
15. Dijkstra’s Algorithm  
16. Exit  
```



---

## 📦 Dependencies

* Python 3.10+
* NumPy
* Standard libraries (`collections`, `heapq`, `timeit`)

---

## 🧠 Algorithms Used

* BFS → O(V + E)
* DFS → O(V + E)
* Dijkstra → O((V + E) log V)
* Heap operations → O(log N)



---

## 📊 System Design

* Graph-based traffic model
* Heap for congestion prioritization
* Hash table for traffic data



---

## 🔮 Future Improvements

* Machine Learning traffic prediction
* Real-time data integration (GPS, sensors)
* GUI-based interface
* Scalable city-level deployment



---

## 👨‍💻 Author

* Dhrubo Jouti Das Troyee
* Student ID: 90028995

---


### 🧠 Core Logic
- [traffic_info.py](trafic_info.py)

### 📊 Data Files
- [traffic_network.txt](traffic_network.txt)
- [traffic_data.txt](traffic_data.txt)

### ⚙️ Data Structures
- [DSAHeapM.py](DSAHeapM.py)
- [DSAHeapEntryM.py](DSAHeapEntryM.py)

### ▶️ Runner
- [testharness.py](testharness)


## 📂 Files Overview

* 📄 [testharness.py](testharness)
  → Interactive test harness for running the traffic system

* 📄 [traffic_info.py](trafic_info.py)
  → Core implementation of Graph, BFS, DFS, Dijkstra, and traffic logic

* 📄 [traffic_network.txt](traffic_network.txt)
  → Input file containing road network structure (nodes & edges)

* 📄 [traffic_data.txt](traffic_data.txt)
  → Contains traffic volume, capacity, and congestion levels

* 📄 [DSAHeapM.py](DSAHeapM.py)
  → Custom heap (priority queue) implementation

* 📄 [DSAHeapEntryM.py](DSAHeapEntryM.py)
  → Heap entry structure (priority + value)



## 📂 Files

* 🔧 [testharness.py](testharness)
  → Interactive test harness for the traffic network

* 📄 [traffic_info.py](trafic_info.py)
  → Core implementation of the Graph class and algorithms (BFS, DFS, Dijkstra)

* 🗺️ [traffic_network.txt](traffic_network.txt)
  → Contains road network data (nodes and distances)

* 🚗 [traffic_data.txt](traffic_data.txt)
  → Stores traffic volume, capacity, and congestion levels

* 🧠 [DSAHeapM.py](DSAHeapM.py)
  → Custom heap (priority queue) implementation

* ⚙️ [DSAHeapEntryM.py](DSAHeapEntryM.py)
  → Heap entry structure for priority queue
