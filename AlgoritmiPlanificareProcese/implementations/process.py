class Process:
    def __init__(self, pid, burst_time, priority=0, arrival_time=0):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.arrival_time = arrival_time
        self.last_executed_time = arrival_time
        self.start_time = None
        self.end_time = None