from multiprocessing import Process
import time

def cpu_heavy_task():
    print("Starting CPU heavy task...")
    count = 0
    for i in range(10**8):
        count += i
    print("CPU heavy task completed. Count:", count)

if __name__ == "__main__":
    start_time = time.time()
    processes = [Process(target=cpu_heavy_task) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    end_time = time.time()
    print("Total execution time:", end_time - start_time, "seconds")
    