import threading
import time

def cpu_heavy_task():
    print("Starting CPU heavy task...")
    count = 0
    for i in range(10**8):
        count += i
    print("CPU heavy task completed. Count:", count)
    
start_time = time.time()

threads = [threading.Thread(target=cpu_heavy_task) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

end_time = time.time()
print("Total execution time:", end_time - start_time, "seconds")

