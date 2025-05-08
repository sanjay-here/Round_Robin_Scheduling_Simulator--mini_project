import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = -1

def round_robin_scheduling(processes, quantum):
    time = 0
    queue = sorted(processes, key=lambda p: p.arrival_time)
    gantt_chart = []
    process_queue = queue[:]
    
    while process_queue:
        process = process_queue.pop(0)
        if process.response_time == -1:
            process.response_time = time - process.arrival_time
        
        if process.remaining_time > quantum:
            gantt_chart.append((process.pid, time, time + quantum))
            time += quantum
            process.remaining_time -= quantum
        else:
            gantt_chart.append((process.pid, time, time + process.remaining_time))
            time += process.remaining_time
            process.completion_time = time
            process.turnaround_time = time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            process.remaining_time = 0

        if process.remaining_time > 0:
            process_queue.append(process)
    
    return gantt_chart

def calculate():
    try:
        quantum = int(entry_quantum.get())
        processes = []
        
        for i in range(len(entries_burst_time)):
            pid = f"P{i+1}"
            arrival_time = int(entries_arrival_time[i].get())
            burst_time = int(entries_burst_time[i].get())
            processes.append(Process(pid, arrival_time, burst_time))
        
        gantt_chart = round_robin_scheduling(processes, quantum)
        
        for widget in result_canvas_frame.winfo_children():
            widget.destroy()
        
        headers = ["Process ID", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time", "Response Time"]
        for j, header in enumerate(headers):
            tk.Label(result_canvas_frame, text=header, font=("Arial", 10, "bold")).grid(row=0, column=j)
        
        for i, process in enumerate(processes, start=1):
            tk.Label(result_canvas_frame, text=process.pid).grid(row=i, column=0)
            tk.Label(result_canvas_frame, text=process.arrival_time).grid(row=i, column=1)
            tk.Label(result_canvas_frame, text=process.burst_time).grid(row=i, column=2)
            tk.Label(result_canvas_frame, text=process.completion_time).grid(row=i, column=3)
            tk.Label(result_canvas_frame, text=process.turnaround_time).grid(row=i, column=4)
            tk.Label(result_canvas_frame, text=process.waiting_time).grid(row=i, column=5)
            tk.Label(result_canvas_frame, text=process.response_time).grid(row=i, column=6)
        
        avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
        avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
        avg_response_time = sum(p.response_time for p in processes) / len(processes)
        
        tk.Label(result_canvas_frame, text=f"Average Waiting Time: {avg_waiting_time:.2f}", font=("Arial", 10, "bold")).grid(row=len(processes) + 1, column=1, columnspan=3)
        tk.Label(result_canvas_frame, text=f"Average Turnaround Time: {avg_turnaround_time:.2f}", font=("Arial", 10, "bold")).grid(row=len(processes) + 2, column=1, columnspan=3)
        tk.Label(result_canvas_frame, text=f"Average Response Time: {avg_response_time:.2f}", font=("Arial", 10, "bold")).grid(row=len(processes) + 3, column=1, columnspan=3)
        
        plot_gantt_chart(gantt_chart)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer values.")

def plot_gantt_chart(gantt_chart):
    fig, ax = plt.subplots()
    for pid, start, end in gantt_chart:
        ax.broken_barh([(start, end - start)], (10, 9), facecolors=('tab:blue'))
        ax.text(start + (end - start) / 2, 15, pid, ha='center', va='center', color='white')
    
    ax.set_ylim(5, 35)
    ax.set_xlim(0, max(end for _, _, end in gantt_chart))
    ax.set_xlabel('Time')
    ax.set_yticks([])
    ax.set_title("Gantt Chart for Round Robin Scheduling")
    
    canvas = FigureCanvasTkAgg(fig, master=gantt_canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def create_burst_time_entries():
    for widget in burst_frame.winfo_children():
        widget.destroy()

    try:
        num_processes = int(entry_num_processes.get())
        global entries_burst_time, entries_arrival_time
        entries_burst_time, entries_arrival_time = [], []

        for i in range(num_processes):
            tk.Label(burst_frame, text=f"Arrival Time for P{i+1}:").grid(row=i, column=0)
            arrival_entry = tk.Entry(burst_frame)
            arrival_entry.grid(row=i, column=1)
            entries_arrival_time.append(arrival_entry)

            tk.Label(burst_frame, text=f"Burst Time for P{i+1}:").grid(row=i, column=2)
            burst_entry = tk.Entry(burst_frame)
            burst_entry.grid(row=i, column=3)
            entries_burst_time.append(burst_entry)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for number of processes.")

# Setup Tkinter GUI
root = tk.Tk()
root.title("Round Robin Scheduling")
root.geometry("675x500")

# Main Scrollable Frame
main_canvas = tk.Canvas(root)
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=main_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

main_canvas.configure(yscrollcommand=scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

main_frame = tk.Frame(main_canvas)
main_canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Quantum input
tk.Label(main_frame, text="Quantum Time:").grid(row=0, column=0, pady=5)
entry_quantum = tk.Entry(main_frame)
entry_quantum.grid(row=0, column=1, pady=5)

# Input for number of processes
tk.Label(main_frame, text="Number of Processes:").grid(row=1, column=0, pady=5)
entry_num_processes = tk.Entry(main_frame)
entry_num_processes.grid(row=1, column=1, pady=5)
tk.Button(main_frame, text="Set Processes", command=create_burst_time_entries).grid(row=1, column=2, pady=5)

# Burst and Arrival time entries container
burst_frame = tk.Frame(main_frame)
burst_frame.grid(row=2, column=0, columnspan=3, pady=5)

# Scrollable result frame for Process Table
result_canvas_frame = tk.Frame(main_frame)
result_canvas_frame.grid(row=4, column=0, columnspan=3, pady=10)

# Gantt chart frame
gantt_canvas_frame = tk.Frame(main_frame)
gantt_canvas_frame.grid(row=5, column=0, columnspan=3, pady=10)

# Calculate button
tk.Button(main_frame, text="Calculate", command=calculate).grid(row=3, column=1, pady=10)

root.mainloop()
