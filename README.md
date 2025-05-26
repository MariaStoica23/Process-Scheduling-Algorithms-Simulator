# ⚙️ Process Scheduling Algorithms Simulator

A clear and interactive simulator for **CPU scheduling algorithms**, designed to help understand core **Operating Systems** concepts through visualization and testing.


## 📌 About the Project

This project implements multiple **process scheduling algorithms** in **Python**, including **FCFS**, **SJF**, **Round Robin**, **Priority Scheduling**, **Round-Robin Priority Scheduling**, and **Multi-level Queue Scheduling** with multiple priority levels.

**Highlights:**
- Manual and random process generation with configurable burst times and priorities
- Detailed calculation of average waiting times and execution profiles
- Interactive graphical interface using **Tkinter**
- Visual scheduling timelines rendered with **Matplotlib**
- Unit testing with Python’s built-in **unittest** framework for correctness verification
- Focus on key **Operating Systems** principles related to CPU scheduling
- Comprehensive code documentation has also been created using **Doxygen** to facilitate understanding and maintenance of the implementation.



## 📎 How It Works

1. Input a set of processes either manually or generate them randomly.
2. Choose the scheduling algorithm to simulate.
3. The simulator calculates:
   - Average waiting time for the selected algorithm.
   - Execution timeline showing process intervals with start/end/duration.
4. Results are displayed graphically with clear timelines and statistics.
5. Users can experiment interactively to better understand scheduling behaviors.


## 🔧 Tech Stack

- **Language:** Python 3
- **GUI:** Tkinter (built-in Python GUI framework)
- **Visualization:** Matplotlib (plots and timelines)
- **Testing:** unittest (Python standard testing library)
- **Random Data Generation:** Python's `random` and `numpy` libraries


## ✅ Features

- Implements 6 different scheduling algorithms with correct logic
- Supports multi-level queues with customizable priorities and scheduling policies
- Manual and automated process creation with realistic burst time and priority distributions
- Calculates average waiting times and generates detailed execution profiles
- Interactive GUI allows hands-on experimentation with scheduling algorithms
- Visual output helps users intuitively grasp scheduling dynamics
- Comprehensive unit tests ensure reliable algorithm implementation


## 💡 Future Improvements

- Support for dynamic priority adjustment and multi-level feedback queues
- Addition of I/O-bound process simulation
- Export scheduling results to CSV or JSON formats
- Enhanced GUI with drag-and-drop process management
- Web-based front-end for easier access and sharing


## 👤 Author

> Project developed by Stoica Anna Maria.
> Created as part of an Operating Systems course project to explore and visualize process scheduling algorithms.


Enjoy exploring process scheduling! 🚦
