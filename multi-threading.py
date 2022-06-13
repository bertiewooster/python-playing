# From https://realpython.com/lessons/threading-python-overview/

import threading
import time


def myfunc(name):
    print(f"myfunc started with {name}")
    time.sleep(5)
    print(f"myfunc ended")
    return True


if __name__ == "__main__":
    print(f"main started")
    t = threading.Thread(target=myfunc, args=["realpython"])
    t.start()
    print(f"main ended")
