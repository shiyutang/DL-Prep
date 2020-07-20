import multiprocessing as mp


def job1(A, num, l):
    l.acquire()
    if num == 1:
        print('p1 start')
    else:
        print('p2 start')

    for i in range(10):
        print(A.value)
        A.value += num

    if num == 1:
        print('p1 finish')
    else:
        print('p2 finish ')
    l.release()


if __name__ == '__main__':
    A = mp.Value('i', 1)
    lock = mp.Lock()
    p1 = mp.Process(target=job1, args=(A, 3, lock,))  # 没有出现数值抢夺
    p2 = mp.Process(target=job1, args=(A, 1, lock,))
    p1.start()
    p2.start()  # 在p1 结束之后才开始
    # p1.join()
    # p2.join()
