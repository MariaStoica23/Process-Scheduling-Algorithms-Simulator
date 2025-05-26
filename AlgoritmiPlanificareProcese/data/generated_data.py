import random
from implementations.process import Process

def generate_processes(count=5, max_priority=5, max_arrival=20, seed=None):
    if seed is not None:
        random.seed(seed)

    processes = []
    for pid in range(1, count + 1):
        burst_time = int(random.gauss(5, 5))
        burst_time = min(burst_time, 15)
        burst_time = max(1, burst_time)

        priority = random.randint(1, max_priority)
        arrival_time = random.randint(0, max_arrival)

        processes.append(Process(pid=pid, burst_time=burst_time, priority=priority, arrival_time=arrival_time))

    return processes