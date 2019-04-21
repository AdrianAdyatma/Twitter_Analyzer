import time
import threading


def Threading(arg):
    while True:
        time.sleep(1)
        print('THREAD', arg)


if __name__ == "__main__":
    t = time.time()

    thread1 = threading.Thread(target=Threading, args=(1,))
    thread1.start()

    thread2 = threading.Thread(target=Threading, args=(2,))
    thread2.start()

    thread1.join()
    thread2.join()

    print("Took", time.time() - t)
