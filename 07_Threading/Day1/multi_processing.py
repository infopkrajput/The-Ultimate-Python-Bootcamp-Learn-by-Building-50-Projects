from multiprocessing import Process
import os
import time


def do_work(worker_name, seconds):
    print(f"{worker_name} started in process id {os.getpid()}")

    for step in range(1, 4):
        print(f"{worker_name} is doing step {step}")
        time.sleep(seconds)

    print(f"{worker_name} finished")


if __name__ == "__main__":
    start_time = time.time()

    process_1 = Process(target=do_work, args=("Worker 1", 1))
    process_2 = Process(target=do_work, args=("Worker 2", 3))
    process_3 = Process(target=do_work, args=("Worker 3", 5))

    process_1.start()
    process_2.start()
    process_3.start()

    process_1.join()
    process_2.join()
    process_3.join()

    end_time = time.time()
    print(f"All processes finished in {end_time - start_time:.2f} seconds")
