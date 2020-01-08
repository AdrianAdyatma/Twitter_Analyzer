import time
import threading


def Threading(arg):
    while True:
        time.sleep(1)
        p = "tr" + str(arg)
        print(p)


if __name__ == "__main__":
    t = time.time()

    thread1 = threading.Thread(target=Threading, args=(1,))
    thread2 = threading.Thread(target=Threading, args=(2,))
    thread3 = threading.Thread(target=Threading, args=(3,))
    thread4 = threading.Thread(target=Threading, args=(4,))
    thread5 = threading.Thread(target=Threading, args=(5,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print("Took", time.time() - t)
