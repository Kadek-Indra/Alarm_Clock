import threading
import time


pesan = 1

def task_one():
    for n in range(5):
        print(f"Pesan {pesan}")
        time.sleep(1)

def task_two():
    for n in range(5):
            print(f"Chat {pesan}")
            time.sleep(1)

thread1 = threading.Thread(target=task_one)
thread2 = threading.Thread(target=task_two)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("END")