import unittest

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

class TestFCFS(unittest.TestCase):
    def test_fcfs_average_waiting_time(self):
        processes = get_fcfs_manual_data()
        average_waiting_time, _ = fcfs_scheduler(processes)
        self.assertAlmostEqual(average_waiting_time, 17)

    def test_fcfs_execution_order(self):
        processes = get_fcfs_manual_data()
        _, execution_order = fcfs_scheduler(processes)
        expected_order = [
            (0, 24, 24, 1),
            (24, 27, 3, 2),
            (27, 30, 3, 3)
        ]
        self.assertEqual(execution_order, expected_order)


class TestSJFNonPreemptive(unittest.TestCase):
    def test_sjf_average_waiting_time(self):
        processes = get_sjf_non_preemptive_manual_data()
        average_waiting_time, _ = sjf_non_preemptive_scheduler(processes)
        self.assertAlmostEqual(average_waiting_time, 7)

    def test_sjf_execution_order(self):
        processes = get_sjf_non_preemptive_manual_data()
        _, execution_order = sjf_non_preemptive_scheduler(processes)
        expected_order = [
            (0, 3, 3, 4),
            (3, 9, 6, 1),
            (9, 16, 7, 3),
            (16, 24, 8, 2)
        ]
        self.assertEqual(execution_order, expected_order)


class TestSJFPreemptive(unittest.TestCase):
    def test_sjf_average_waiting_time(self):
        processes = get_sjf_preemptive_manual_data()
        average_waiting_time, _ = sjf_preemptive_scheduler(processes)
        self.assertAlmostEqual(average_waiting_time, 6.5)

    def test_sjf_execution_order(self):
        processes = get_sjf_preemptive_manual_data()
        _, execution_order = sjf_preemptive_scheduler(processes)
        expected_order = [
            (0, 1, 1, 1),
            (1, 5, 4, 2),
            (5, 10, 5, 4),
            (10, 17, 7, 1),
            (17, 26, 9, 3)
        ]
        self.assertEqual(execution_order, expected_order)


class TestRoundRobin(unittest.TestCase):
    def test_round_robin_average_waiting_time(self):
        processes, quantum = get_round_robin_manual_data()
        average_waiting_time, _ = round_robin_scheduler(processes, quantum)
        self.assertAlmostEqual(average_waiting_time, 5.67, places=2)

    def test_round_robin_execution_order(self):
        processes, quantum = get_round_robin_manual_data()
        _, execution_order = round_robin_scheduler(processes, quantum)
        expected_order = [
            (0, 4, 4, 1),
            (4, 7, 3, 2),
            (7, 10, 3, 3),
            (10, 14, 4, 1),
            (14, 18, 4, 1),
            (18, 22, 4, 1),
            (22, 26, 4, 1),
            (26, 30, 4, 1)
        ]
        self.assertEqual(execution_order, expected_order)


class TestPrioritySchedulingNonPreemptive(unittest.TestCase):
    def test_priority_scheduling_average_waiting_time(self):
        processes = get_priority_scheduling_non_preemptive_manual_data()
        average_waiting_time, _ = priority_scheduling_non_preemptive(processes)
        self.assertAlmostEqual(average_waiting_time, 8.2)

    def test_priority_scheduling_execution_order(self):
        processes = get_priority_scheduling_non_preemptive_manual_data()
        _, execution_order = priority_scheduling_non_preemptive(processes)
        expected_order = [
            (0, 1, 1, 2),
            (1, 6, 5, 5),
            (6, 16, 10, 1),
            (16, 18, 2, 3),
            (18, 19, 1, 4)
        ]
        self.assertEqual(execution_order, expected_order)


class TestPrioritySchedulingPreemptive(unittest.TestCase):
    def test_priority_scheduling_average_waiting_time(self):
        processes = get_priority_scheduling_preemptive_manual_data()
        average_waiting_time, _ = priority_scheduling_preemptive(processes)
        self.assertAlmostEqual(average_waiting_time, 2.75)

    def test_priority_scheduling_execution_order(self):
        processes = get_priority_scheduling_preemptive_manual_data()
        _, execution_order = priority_scheduling_preemptive(processes)
        expected_order = [
            (0, 2, 2, 1),
            (2, 3, 1, 2),
            (3, 4, 1, 1),
            (4, 5, 1, 4),
            (5, 12, 7, 1),
            (12, 14, 2, 3)
        ]
        self.assertEqual(execution_order, expected_order)


class TestRRPriorityScheduling(unittest.TestCase):
    def test_rr_priority_scheduling_average_waiting_time(self):
        processes, quantum = get_rr_priority_manual_data()
        average_waiting_time, _ = round_robin_priority_scheduling(processes, quantum)
        self.assertAlmostEqual(average_waiting_time, 13.8)

    def test_rr_priority_scheduling_execution_order(self):
        processes, quantum = get_rr_priority_manual_data()
        _, execution_order = round_robin_priority_scheduling(processes, quantum)
        expected_order = [
            (0, 2, 2, 4),
            (2, 4, 2, 4),
            (4, 6, 2, 4),
            (6, 7, 1, 4),
            (7, 9, 2, 2),
            (9, 11, 2, 3),
            (11, 13, 2, 2),
            (13, 15, 2, 3),
            (15, 16, 1, 2),
            (16, 18, 2, 3),
            (18, 20, 2, 3),
            (20, 22, 2, 1),
            (22, 24, 2, 5),
            (24, 26, 2, 1),
            (26, 27, 1, 5)
        ]
        self.assertEqual(execution_order, expected_order)


class TestMultilevelQueueScheduling(unittest.TestCase):
    def test_multilevel_queue_scheduling_average_waiting_time(self):
        processes = get_multilevel_manual_data()
        average_waiting_time, _ = multilevel_queue_scheduling(processes)
        self.assertAlmostEqual(average_waiting_time, 13.86, places=2)

    def test_multilevel_queue_scheduling_execution_order(self):
        processes = get_multilevel_manual_data()
        _, execution_order = multilevel_queue_scheduling(processes)
        expected_order = [
            (0, 2, 2, 1),
            (2, 4, 2, 1),
            (4, 6, 2, 5),
            (6, 7, 1, 1),
            (7, 8, 1, 5),
            (8, 12, 4, 2),
            (12, 16, 4, 6),
            (16, 20, 4, 2),
            (20, 23, 3, 6),
            (23, 29, 6, 3),
            (29, 31, 2, 7),
            (31, 35, 4, 4)
        ]
        self.assertEqual(execution_order, expected_order)


class TestMultilevelFeedbackQueueScheduling(unittest.TestCase):
    def test_multilevel_feedback_queue_scheduling_average_waiting_time(self):
        processes = get_multilevel_feedback_manual_data()
        average_waiting_time, _ = multilevel_feedback_queue_scheduling(processes)
        self.assertAlmostEqual(average_waiting_time, 23)

    def test_multilevel_feedback_queue_scheduling_execution_order(self):
        processes = get_multilevel_feedback_manual_data()
        _, execution_order = multilevel_feedback_queue_scheduling(processes)
        expected_order = [
            (0, 8, 8, 1),
            (8, 13, 5, 2),
            (13, 21, 8, 3),
            (21, 29, 8, 4),
            (29, 32, 3, 5),
            (32, 44, 12, 1),
            (44, 46, 2, 3),
            (46, 62, 16, 4),
            (62, 68, 6, 4)
        ]
        self.assertEqual(execution_order, expected_order)
