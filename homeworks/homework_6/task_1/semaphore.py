from threading import Condition
import contracts


class Semaphore:
    """
    Class used to control access to a common resource by multiple processes and avoid critical section problems
    in a concurrent system
    """

    def __init__(self):
        self.size = 1
        self.condition = Condition()

    # to use semaphore with a context manager
    def __enter__(self):
        with self.condition:
            while self.size == 0:
                self.condition.wait()
            self.size -= 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self.condition:
            self.size += 1
            self.condition.notify()

    @contracts.pre(lambda cls, x: x >= 0, message="Negative initial size is illegal.")
    def set_size(self, initial_size: int = 1) -> None:
        """
        Sets max quantity of threads that can use common resource
        """
        self.size = initial_size
