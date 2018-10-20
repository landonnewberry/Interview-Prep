import datetime

def timed(f):
    def wrapper():
        t1 = datetime.datetime.now()
        f()
        t2 = datetime.datetime.now()
        print("Function {} took {} to execute.".format(f.__name__, t2 - t1))
    return wrapper

def time_sort(f, a):
    t1 = datetime.datetime.now()
    f(a)
    return datetime.datetime.now() - t1
