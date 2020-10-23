import multiprocessing as mp
import time
import threading


def job(q):
    res = 0
    for i in range(10000):
        res += i ** 2
    q.put(res)


def multithread():
    q = mp.Queue()
    t1 = threading.Thread(target=job, args=(q,))
    t2 = threading.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('thread', q.get()+q.get())


def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('process', q.get()+q.get())


def normal():
    res = 0
    for _ in range(2):
        for i in range(10000):
            res += i ** 2

    print('normal', res)


if __name__ == '__main__':
    start = time.time()
    normal()
    print('normal', time.time() - start)
    start = time.time()
    multicore()
    print('multicore', time.time() - start)
    start = time.time()
    multithread()
    print('multithread', time.time() - start)
