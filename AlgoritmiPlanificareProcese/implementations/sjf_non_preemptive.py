from implementations.process import Process

def sjf_non_preemptive_scheduler(processes):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0
    execution_order = []
    waiting_time = 0

    completed = 0

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

        current_process = min(available, key=lambda p: p.burst_time)

        current_process.start_time = max(current_time, current_process.arrival_time)
        current_process.end_time = current_process.start_time + current_process.burst_time

        execution_order.append((current_process.start_time, current_process.end_time, current_process.burst_time, current_process.pid))

        waiting_time += current_process.start_time - current_process.arrival_time
        current_time = current_process.end_time

        current_process.remaining_time = 0
        completed += 1

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time, execution_order