import threading
import time


def job2():
    global queue
    A = 0
    for i in range(10100):
        A += 1
    queue.append(A)


if __name__ == '__main__':
    t1 = threading.Thread(target=job2)
    t2 = threading.Thread(target=job2)
    t3 = threading.Thread(target=job2)
    t4 = threading.Thread(target=job2)
    # lock = threading.Lock()

    start = time.time()
    A = 0
    for i in range(10100 * 4):
        A += 1
    print("A", A)

    print("time of t1", time.time() - start)
    start = time.time()
    A = 0
    queue = []
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t4.join()
    for ele in queue:
        A += ele
    print(A)
    print('time of t2 is', time.time() - start)
    print('all done')
