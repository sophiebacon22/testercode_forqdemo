import threading
from queue import Queue

class Transaction:

    def __init__(self):
        self.queue = Queue()
        self.workers = []
        self.num_workers = 10

    def add_transaction(self, transaction):
        self.queue.put(transaction)

    def start_workers(self):
        for i in range(self.num_workers):
            worker = threading.Thread(target=self.process_transaction)
            worker.start()
            self.workers.append(worker)

    def process_transaction(self):
        while True:
            transaction = self.queue.get()
            # process transaction
            self.queue.task_done()

    def join_workers(self):
        self.queue.join()
        for worker in self.workers:
            worker.join()