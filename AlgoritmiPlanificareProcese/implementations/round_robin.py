from implementations.process import Process
from collections import deque

def round_robin_scheduler(processes, quantum):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0
    execution_order = []
    waiting_time = 0

    queue = deque()
    completed = 0
    in_queue = [False] * len(processes)

    index = 0
    while completed < len(processes) or queue:
        while index < len(processes) and processes[index].arrival_time <= current_time:
            if not in_queue[index]:
                queue.append(processes[index])
                in_queue[index] = True
            index += 1

        if not queue:
            if index < len(processes):
                current_time = processes[index].arrival_time
                continue
            else:
                break

        current_process = queue.popleft()

        if current_process.start_time is None:
            current_process.start_time = current_time

        execution_time = min(current_process.remaining_time, quantum)
        execution_order.append((current_time, current_time + execution_time, execution_time, current_process.pid))
        current_process.remaining_time -= execution_time
        current_time += execution_time

        while index < len(processes) and processes[index].arrival_time <= current_time:
            if not in_queue[index]:
                queue.append(processes[index])
                in_queue[index] = True
            index += 1

        if current_process.remaining_time > 0:
            queue.append(current_process)
        else:
            current_process.end_time = current_time
            waiting_time += current_process.end_time - current_process.arrival_time - current_process.burst_time
            completed += 1

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time, execution_order