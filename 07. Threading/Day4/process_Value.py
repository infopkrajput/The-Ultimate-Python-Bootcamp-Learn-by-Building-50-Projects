from multiprocessing import Process, Value

def increment(shared_value):
    for _ in range(100000):
        with shared_value.get_lock():
            shared_value.value += 1
        
    
if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value:", counter.value)

