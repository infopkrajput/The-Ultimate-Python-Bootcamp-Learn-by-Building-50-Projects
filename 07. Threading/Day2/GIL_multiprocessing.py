from multiprocessing import Process, current_process
import time

def crunch_number():
    print(f"Started the count process: {current_process().name}")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Finished the count process: {current_process().name}")

if __name__ == "__main__":
    start = time.time()

    process1 = Process(target=crunch_number, name="Process-1")
    process2 = Process(target=crunch_number, name="Process-2")

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.time()
    print(f"total time taken: {end - start:.2f} seconds")