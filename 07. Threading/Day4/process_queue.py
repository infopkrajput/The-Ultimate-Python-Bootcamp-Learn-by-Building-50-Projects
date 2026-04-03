from multiprocessing import Process, Queue
import time

def prepare_chai(q):
    q.put("Boil water")

if __name__ == "__main__":
    queue = Queue()

    process = Process(target=prepare_chai, args=(queue,))
    process.start()
    process.join()

    print("Chai preparation step:", queue.get())
