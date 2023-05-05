# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters
# and setters instead!

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise ValueError("Worker must be an instance of the Worker class")
        self._workers.append(worker)

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, value):
        raise AttributeError("Cannot set workers directly")

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if not isinstance(value, Boss):
            raise ValueError("Boss must be an instance of the Boss class")
        self._boss = value
        self._boss.add_worker(self)


boss1 = Boss(1, "John", "ABC Company")
boss2 = Boss(2, "Mike", "XYZ Company")

worker1 = Worker(1, "Bob", "ABC Company", boss1)
print(f"{worker1.name}'s boss is {worker1.boss.name}")

worker1.boss = boss2
print(f"{worker1.name}'s new boss is {worker1.boss.name}")

worker2 = Worker(2, "Alice", "XYZ Company", boss2)

for worker in boss1.workers:
    print(f"{worker.name} works for {boss1.name}")

for worker in boss2.workers:
    print(f"{worker.name} works for {boss2.name}")

