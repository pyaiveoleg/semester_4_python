import unittest
from threading import Thread

from homeworks.homework_6.task_1.semaphore import Semaphore


class TestSemaphore(unittest.TestCase):
    def setUp(self):
        self.counter = 0
        self.semaphore = Semaphore()

    def inc(self):
        with self.semaphore:
            self.counter += 1

    def test_one_thread(self):
        thread = Thread(target=self.inc)
        thread.start()
        thread.join()

        self.assertEqual(self.counter, 1)

    def test_several_threads(self):
        self.semaphore.set_size(1)
        threads_quantity = 10

        threads = [Thread(target=self.inc) for i in range(threads_quantity)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        self.assertEqual(self.counter, threads_quantity)
