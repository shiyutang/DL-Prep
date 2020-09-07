def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)   # 发送生产的东西给消费者，不需要通过线程之间的锁机制切换
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()          # 不生产了，停用generator


customer = consumer()
produce(customer)
