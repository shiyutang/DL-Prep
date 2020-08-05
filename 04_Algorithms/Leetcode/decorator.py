import functools
import time


def log(text):
    def decorator(func):  # 带参数的decorator，
        @functools.wraps(func)  # 传入decorator的函数的属性如name等不发生改变（函数签名）
        def wrapper(*args, **kw):  # 内部可以接受从最外层到最内层的参数
            print('let\'s see if I can use {} and {}'.format(args, kw))
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('parames')  # 借助python 的@语法，在函数定义的时候行使装饰器的作用
def now(*args, **kwargs):  # wrapper 内部还可传入各种参数,但是要保证now 中也传入
    print(time.time())


# now = log()(now)
d = {'1': '4'}  # 传入kw 要从dict 中解包
now(*[1, 2, 3, 45], **d)  # 现在调用now，等效于调用wrapper，并增强now的功能
print(now.__name__)
