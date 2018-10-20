import datetime

def timed(f):
    def wrapper():
        t1 = datetime.datetime.now()
        f()
        t2 = datetime.datetime.now()
        print("Function {} took {} to execute.".format(f.__name__, t2 - t1))
    return wrapper

def time_function(f, *args, **kwargs):
    t = datetime.datetime.now()
    f(*args, **kwargs)
    return datetime.datetime.now() - t
