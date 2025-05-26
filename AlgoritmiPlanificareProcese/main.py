import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import  matplotlib.pyplot as plt

from implementations.fcfs import fcfs_scheduler
from implementations.sjf_non_preemptive import sjf_non_preemptive_scheduler
from implementations.sjf_preemptive import sjf_preemptive_scheduler
from implementations.round_robin import round_robin_scheduler
from implementations.priority_scheduling_non_preemptive import priority_scheduling_non_preemptive
from implementations.priority_scheduling_preemptive import priority_scheduling_preemptive
from implementations.rr_priority_scheduling import round_robin_priority_scheduling
from implementations.multilevel_queue_scheduling import multilevel_queue_scheduling
from implementations.multilevel_feedback_queue_scheduling import multilevel_feedback_queue_scheduling

from data.manual_data import (
    get_fcfs_manual_data,
    get_sjf_non_preemptive_manual_data,
    get_sjf_preemptive_manual_data,
    get_round_robin_manual_data,
    get_priority_scheduling_non_preemptive_manual_data,
    get_priority_scheduling_preemptive_manual_data,
    get_rr_priority_manual_data,
    get_multilevel_manual_data,
    get_multilevel_feedback_manual_data
)

from data.generated_data import generate_processes


algorithm = {
    "FCFS": (fcfs_scheduler, get_fcfs_manual_data),
    "SJF (Non-Preemptive)": (sjf_non_preemptive_scheduler, get_sjf_non_preemptive_manual_data),
    "SJF (Preemptive)": (sjf_preemptive_scheduler, get_sjf_preemptive_manual_data),
    "Round Robin": (lambda p: round_robin_scheduler(p,4), get_round_robin_manual_data),
    "Priority Scheduling (Non-Preemptive)": (priority_scheduling_non_preemptive, get_priority_scheduling_non_preemptive_manual_data),
    "Priority Scheduling (Preemptive)": (priority_scheduling_preemptive, get_priority_scheduling_preemptive_manual_data),
    "RR + Priority Scheduling": (lambda p: round_robin_priority_scheduling(p,2), get_rr_priority_manual_data),
    "Multilevel Queue Scheduling": (multilevel_queue_scheduling, get_multilevel_manual_data),
    "Multilevel Feedback Queue Scheduling": (multilevel_feedback_queue_scheduling, get_multilevel_feedback_manual_data)
}


def get_processes(current_algorithm, data_source):
    scheduler_function, manual_data_function = algorithm[current_algorithm]

    if data_source == "Manual data":
        data = manual_data_function()
        processes = data[0] if isinstance(data, tuple) else data   #aaaaaaaaaaaaaaaaaaaaa
    else:
        if current_algorithm == "Multilevel Queue Scheduling":
            processes = generate_processes(count=5, max_priority=4)
        elif current_algorithm == "Multilevel Feedback Queue Scheduling":
            processes = generate_processes(count=5, max_priority=3)
        else:
            processes = generate_processes(count=5)
    return processes, scheduler_function


def display_processes_table(processes, parent_frame):
    text_widget = tk.Text(parent_frame, height=8, width=32, font=("Courier New", 10))
    text_widget.insert(tk.END, f"{'PID':<6}{'Burst':<8}{'Priority':<10}{'Arrival':<8}\n")
    text_widget.insert(tk.END, "-" * 32 + "\n")
    for p in processes:
        text_widget.insert(tk.END, f"{'P' + str(p.pid):<6}{p.burst_time:<8}{p.priority:<10}{p.arrival_time:<8}\n")
    text_widget.config(state=tk.DISABLED)
    text_widget.pack()


def draw_chart(execution_order, parent_frame):
    fig, ax = plt.subplots(figsize=(8, 2.5))

    for start, end, duration, pid in execution_order:
        ax.barh(0, duration, left=start, height=0.5, align="center", color="skyblue")
        ax.text(start + duration / 2, 0, f"P{pid}", ha="center", va="center", color="black", fontsize=9)

    ax.set_xlim(0, execution_order[-1][1])
    ax.set_ylim(-0.5, 0.5)
    rect = plt.Rectangle((0, -0.25), execution_order[-1][1], 0.5, linewidth=1, edgecolor="black", facecolor="none")
    ax.add_patch(rect)

    transition_points = sorted({pt for s, e, *_ in execution_order for pt in {s, e}})
    for point in transition_points:
        ax.vlines(point, -0.25, 0.25, color="black", linewidth=0.5)
        ax.text(point, -0.35, f"{point}", ha="center", va="center", fontsize=8)

    ax.set_yticks([])
    ax.set_xticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    plt.close(fig)


def run_simulation():
    for widget in results_frame.winfo_children():
        widget.destroy()
    for widget in chart_frame.winfo_children():
        widget.destroy()

    current_algorithm = algorithm_var.get()
    data_source = data_var.get()

    processes, scheduler_function = get_processes(current_algorithm, data_source)
    average_waiting_time, execution_order = scheduler_function(processes)

    display_processes_table(processes, results_frame)

    tk.Label(results_frame, text=f"Average waiting time: {average_waiting_time:.2f} ms", font=("Courier New", 10)).pack(pady=(15, 0))

    draw_chart(execution_order, chart_frame)


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


root = tk.Tk()
root.title("Planning Algorithm Simulator")
root.minsize(800, 556)

algorithm_var = tk.StringVar(value="FCFS")
data_var = tk.StringVar(value="Manual data")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

ttk.Label(frame_top, text="Choose algorithm: ").grid(row=0, column=0)
algorithm_menu = ttk.Combobox(frame_top, textvariable=algorithm_var, values=list(algorithm.keys()), width=40, state="readonly")
algorithm_menu.grid(row=0, column=1)

ttk.Label(frame_top, text="Choose data type: ").grid(row=1, column=0)
data_menu = ttk.Combobox(frame_top, textvariable=data_var, values=["Manual data", "Generated data"], width=40, state="readonly")
data_menu.grid(row=1, column=1)

run_button = ttk.Button(frame_top, text="Run Simulation", command=run_simulation)
run_button.grid(row=2, columnspan=2, pady=10)

results_frame = tk.Frame(root)
results_frame.pack(pady=5)

chart_frame = tk.Frame(root)
chart_frame.pack(pady=10)

center_window(root)

root.mainloop()