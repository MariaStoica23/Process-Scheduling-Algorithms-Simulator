from implementations.process import Process

def fcfs_scheduler(processes):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0
    execution_order = []
    waiting_time = 0

    for p in processes:
        p.start_time = max(current_time, p.arrival_time)
        p.end_time = p.start_time + p.burst_time
        execution_order.append((p.start_time, p.end_time, p.burst_time, p.pid))
        waiting_time += p.start_time - p.arrival_time
        current_time = p.end_time

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time, execution_order
