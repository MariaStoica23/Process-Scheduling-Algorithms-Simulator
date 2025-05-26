from implementations.process import Process

def get_fcfs_manual_data():
    return [
        Process(pid=1, burst_time=24),
        Process(pid=2, burst_time=3),
        Process(pid=3, burst_time=3)
    ]

def get_sjf_non_preemptive_manual_data():
    return [
        Process(pid=1, burst_time=6),
        Process(pid=2, burst_time=8),
        Process(pid=3, burst_time=7),
        Process(pid=4, burst_time=3)
    ]

def get_sjf_preemptive_manual_data():
    return [
        Process(pid=1, burst_time=8, arrival_time=0),
        Process(pid=2, burst_time=4, arrival_time=1),
        Process(pid=3, burst_time=9, arrival_time=2),
        Process(pid=4, burst_time=5, arrival_time=3)
    ]

def get_round_robin_manual_data():
    processes = [
        Process(pid=1, burst_time=24),
        Process(pid=2, burst_time=3),
        Process(pid=3, burst_time=3)
    ]
    quantum = 4
    return processes, quantum

def get_priority_scheduling_non_preemptive_manual_data():
    return [
        Process(pid=1, burst_time=10, priority=3),
        Process(pid=2, burst_time=1, priority=1),
        Process(pid=3, burst_time=2, priority=4),
        Process(pid=4, burst_time=1, priority=5),
        Process(pid=5, burst_time=5, priority=2)
    ]

def get_priority_scheduling_preemptive_manual_data():
    return [
        Process(pid=1, burst_time=10, priority=3, arrival_time=0),
        Process(pid=2, burst_time=1, priority=1, arrival_time=2),
        Process(pid=3, burst_time=2, priority=4, arrival_time=3),
        Process(pid=4, burst_time=1, priority=1, arrival_time=4)
    ]

def get_rr_priority_manual_data():
    processes = [
        Process(pid=1, burst_time=4, priority=3),
        Process(pid=2, burst_time=5, priority=2),
        Process(pid=3, burst_time=8, priority=2),
        Process(pid=4, burst_time=7, priority=1),
        Process(pid=5, burst_time=3, priority=3)
    ]
    quantum = 2
    return processes, quantum

def get_multilevel_manual_data():
    return [
        Process(pid=1, burst_time=5, priority=1, arrival_time=0),
        Process(pid=2, burst_time=8, priority=2, arrival_time=1),
        Process(pid=3, burst_time=6, priority=3, arrival_time=2),
        Process(pid=4, burst_time=4, priority=4, arrival_time=3),
        Process(pid=5, burst_time=3, priority=1, arrival_time=4),
        Process(pid=6, burst_time=7, priority=2, arrival_time=5),
        Process(pid=7, burst_time=2, priority=3, arrival_time=6)
    ]

def get_multilevel_feedback_manual_data():
    return [
        Process(pid=1, burst_time=20, arrival_time=0),
        Process(pid=2, burst_time=5, arrival_time=2),
        Process(pid=3, burst_time=10, arrival_time=4),
        Process(pid=4, burst_time=30, arrival_time=6),
        Process(pid=5, burst_time=3, arrival_time=8)
    ]