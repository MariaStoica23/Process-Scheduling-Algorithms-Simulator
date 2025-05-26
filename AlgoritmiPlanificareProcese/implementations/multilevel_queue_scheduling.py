from implementations.process import Process
from collections import deque

def multilevel_queue_scheduling(processes):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0
    execution_order = []
    waiting_time = 0

    queues = [deque() for _ in range(4)]
    quantums = {0: 2, 1: 4}
    completed = 0

    index = 0
    while completed < len(processes):
        while index < len(processes) and processes[index].arrival_time <= current_time:
            level = processes[index].priority - 1
            queues[level].append(processes[index])
            index += 1

        level_to_run = None
        for i, q in enumerate(queues):
            if q:
                level_to_run = i
                break

        if level_to_run is None:
            if index < len(processes):
                current_time = processes[index].arrival_time
                continue
            else:
                break

        queue = queues[level_to_run]
        current_process = queue.popleft()

        if current_process.start_time is None:
            current_process.start_time = current_time

        if level_to_run in quantums:
            quantum = quantums[level_to_run]
            execution_time = min(current_process.remaining_time, quantum)
        else:
            execution_time = current_process.remaining_time

        execution_order.append((current_time, current_time + execution_time, execution_time, current_process.pid))
        current_process.remaining_time -= execution_time
        current_time += execution_time

        while index < len(processes) and processes[index].arrival_time <= current_time:
            level = processes[index].priority - 1
            queues[level].append(processes[index])
            index += 1

        if current_process.remaining_time > 0:
            if level_to_run in quantums:
                queues[level_to_run].append(current_process)
        else:
            current_process.end_time = current_time
            waiting_time += current_process.end_time - current_process.arrival_time - current_process.burst_time
            completed += 1

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time, execution_order
