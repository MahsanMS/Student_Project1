# Student_Project1
A Python project simulating the pathfinding component of a warehouse robot (practice project, middle school).

# Warehouse Robot Pathfinding Simulator

This project was originally developed during my early high school years as a practice project.  
It is written in Python and simulates the pathfinding system of a warehouse robot. The idea was to design a software that serves as the "eyes" of the robot, helping it navigate efficiently inside a warehouse or between stores.

---

## 🎯 Project Goals
- Find the shortest path from the robot’s current location to the destination (e.g., the position of a new item or the correct shelf inside the warehouse).
- Find the shortest path between stores (or other locations) in order to deliver goods as quickly as possible.

---

## ⚙️ Features
- **2D Warehouse Navigation**: The warehouse is modeled as a grid where obstacles, start, and destination coordinates are provided by the user.
- **Graph-Based Navigation**: Streets between stores are represented as a weighted graph, where edge weights depend on distance and traffic.
- **Algorithms Used**:  
  - A* for shortest pathfinding inside the warehouse  
  - DFS for pathfinding in the street/graph environment  
- **Simulation**: Built using Python with `turtle` for visualization.  

---

## 🚀 How to Run
You can either:
1. Run the compiled executable file (`.exe`).  
2. Run the source code with Python (make sure the required libraries are installed).

### Required Libraries
- `numpy`  
- `PIL`  
- `tkinter`  
- `shutil`  
- `pandas`

Install them via pip if necessary:  
```bash
pip install numpy pillow pandas
```

## 🖥️ Usage Guide
- Warehouse Navigation:
  - Define the warehouse as an n × m grid.
  - Provide the coordinates of obstacles, starting point, and destination.
- Street Navigation:
  - Model the map as a weighted graph.
  - Provide the number of vertices, edges, and weights (weights = time needed to traverse a street considering distance and traffic).
  - Currently weights must be entered manually, but in a real product they would be set automatically.

 ## 📌 Notes
 - This project was created purely for educational purposes and is not intended for further development.
 - Future versions may integrate real-time data (e.g., traffic conditions) for more realistic simulations.

## 👥 Contributors
- Mahsan Mohammadzadeh Soltanmoradi
- Fateme Mostafavi
