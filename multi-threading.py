# From https://realpython.com/lessons/threading-python-overview/

import time


def myfunc():
    print("hello")
    time.sleep(5)
    return True

if __name__ == "__main__":
    myfunc()
    