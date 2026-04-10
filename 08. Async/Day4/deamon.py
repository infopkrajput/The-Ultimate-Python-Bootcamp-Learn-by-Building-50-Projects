import threading
import time

def monitor_temperature():
    while True:
        print("Monitoring temperature...")
        time.sleep(2)
        
threading.Thread(target=monitor_temperature, daemon=True).start()
print("Main thread is doing other work...")