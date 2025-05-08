# 🎯 Round Robin Scheduling Simulator (Desktop App)

A Python-based GUI application to simulate the **Round Robin CPU Scheduling Algorithm**. This educational tool allows users to input multiple processes along with their arrival and burst times, choose a quantum time, and visualize the process execution timeline via a Gantt chart.

---

## 🛠️ Features

- Input custom number of processes
- Enter arrival and burst times
- Specify quantum (time slice)
- Displays:
  - Completion Time
  - Turnaround Time
  - Waiting Time
  - Response Time
  - Average statistics
- Generates Gantt chart for process execution timeline
- Built-in error handling for invalid inputs
- Scrollable interface for better UX

---

## 📸 Screenshots

*You can insert screenshots here using:*

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone or Download the Repository

git clone https://github.com/sanjay-here/Round_Robin_Scheduling_Simulator--mini_project.git

### 2. Install Dependencies
Ensure you have Python 3 installed. Then install the required modules:

>pip install matplotlib

### 3. Run the Application

>python roundrobin.py


## 🧠 Algorithm Used: Round Robin
Round Robin is a pre-emptive scheduling algorithm where each process is assigned a fixed time slot (quantum). It works on the principle of First Come First Serve, but with time slicing to ensure fair CPU sharing.


## 📈 Gantt Chart
The Gantt chart is dynamically generated using Matplotlib, showing the start and end times for each process slice.


## 📂 File Structure

roundrobin.py          # Main Python script
README.md              # Project documentation
🧑‍💻 Tech Stack

Python 3

Tkinter – for GUI

Matplotlib – for Gantt chart visualization

## 🙌 Acknowledgements
This project is designed as a part of the Operating Systems course to help students visualize CPU scheduling algorithms.
