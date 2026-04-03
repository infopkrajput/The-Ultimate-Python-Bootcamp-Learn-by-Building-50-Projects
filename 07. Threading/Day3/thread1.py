import threading
import time 

def boil_milk():
    print("Boiling milk...")
    time.sleep(5)
    print("Milk is boiled.")

def toast_bun():
    print("Toasting bun...")
    time.sleep(3)
    print("Bun is toasted.")
    

if __name__ == "__main__":
    
    start_time = time.time()
    
    thread1 = threading.Thread(target=boil_milk)
    thread2 = threading.Thread(target=toast_bun)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Breakfast is ready!")
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    