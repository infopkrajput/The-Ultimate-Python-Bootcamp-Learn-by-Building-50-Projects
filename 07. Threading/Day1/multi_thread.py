import threading
import time

def take_orders():
    for i in range(1, 6):
        print("Taking order", i)
        time.sleep(1)
    print("All orders taken")

def prepare_food():
    for i in range(1, 6):
        print("Preparing food", i)
        time.sleep(1.5)
    print("All food prepared")

if __name__ == "__main__":
    order_thread = threading.Thread(target=take_orders)
    food_thread = threading.Thread(target=prepare_food)

    order_thread.start()
    food_thread.start()

    order_thread.join()
    food_thread.join()

    print("Restaurant is ready to serve customers")
    