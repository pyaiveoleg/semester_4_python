import unittest
from typing import Callable
from threading import Thread

from homeworks.homework_6.task_1.semaphore import Semaphore


def run_threads(target: Callable, threads_quantity: int):
    """
    Runs given number of threads perfoming giving function.
    """
    threads = [Thread(target=target) for i in range(threads_quantity)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


class TestSemaphore(unittest.TestCase):
    def setUp(self):
        self.counter = 0
        self.semaphore = Semaphore()

    def inc(self):
        with self.semaphore:
            self.counter += 1

    def dec(self):
        with self.semaphore:
            self.counter -= 1

    def test_one_thread(self):
        thread = Thread(target=self.inc)
        thread.start()
        thread.join()

        self.assertEqual(self.counter, 1)

    def test_several_threads(self):
        self.semaphore.set_size(1)
        threads_quantity = 10
        run_threads(target=self.inc, threads_quantity=threads_quantity)
        self.assertEqual(self.counter, threads_quantity)

    def test_size_less_zero(self):
        with self.assertRaises(AssertionError):
            self.semaphore.set_size(-1)

    def test_long_critical_section(self):
        number_of_increments = 100000
        with self.semaphore:
            for i in range(number_of_increments):
                self.counter += 1

        self.assertEqual(self.counter, number_of_increments)

    def test_size_less_than_threads(self):
        number_of_threads = 5
        self.semaphore.set_size(3)
        run_threads(target=self.inc, threads_quantity=number_of_threads)
        self.assertEqual(self.counter, number_of_threads)

    def test_size_more_than_threads(self):
        number_of_threads = 5
        self.semaphore.set_size(7)
        run_threads(target=self.inc, threads_quantity=number_of_threads)
        self.assertEqual(self.counter, number_of_threads)

    def test_opposite_operations(self):
        number_of_threads = 5
        for i in range(number_of_threads):
            # to shuffle incrementing and decrementing functions
            run_threads(target=self.inc, threads_quantity=1)
            run_threads(target=self.dec, threads_quantity=1)
        self.assertEqual(self.counter, 0)
