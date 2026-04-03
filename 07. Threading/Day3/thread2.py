import threading
import time

def prepare_coffee(type_of_coffee, wait_time):
    print(f"Preparing {type_of_coffee}...")
    time.sleep(wait_time)
    print(f"{type_of_coffee} is ready.")
    
t1 = threading.Thread(target=prepare_coffee, args=("Espresso", 4))
t2 = threading.Thread(target=prepare_coffee, args=("Latte", 3))

t1.start()
t2.start()

t1.join()
t2.join()

print("Coffee is ready!")
print("Enjoy your coffee!")
