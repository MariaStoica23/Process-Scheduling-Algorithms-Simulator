from implementations.process import Process

def sjf_preemptive_scheduler(processes):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0
    execution_order = []
    waiting_time = 0

    completed = 0
    last_pid = None
    start_time = None

    while completed < len(processes):
        available = []
        for p in processes:
            if p.arrival_time <= current_time and p.remaining_time > 0:
                available.append(p)

        if len(available) == 0:
            earliest_arrival = None
            for p in processes:
                if p.remaining_time > 0:
                    if earliest_arrival is None or p.arrival_time < earliest_arrival:
                        earliest_arrival = p.arrival_time
            current_time = earliest_arrival
            continue

        current_process = min(available, key=lambda p: p.remaining_time)

        if last_pid != current_process.pid:
            if start_time is not None and last_pid is not None:
                execution_order.append((start_time, current_time, current_time - start_time, last_pid))
            start_time = current_time
            last_pid = current_process.pid

        if current_process.start_time is None:
            current_process.start_time = current_time

        current_process.remaining_time -= 1
        current_time += 1

        if current_process.remaining_time == 0:
            completed += 1
            current_process.end_time = current_time
            waiting_time += current_process.end_time - current_process.arrival_time - current_process.burst_time

    if start_time is not None and last_pid is not None:
        execution_order.append((start_time, current_time, current_time - start_time, last_pid))

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time, execution_order