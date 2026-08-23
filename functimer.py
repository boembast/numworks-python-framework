from time import monotonic # Monotonic is used instead of a better alternative because on the Numworks calculator, there is no better alternative.

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = monotonic()
        result = f(*args, **kwargs)
        delta = monotonic() - t
        print('Function {} Time = {:6.3f}ms'.format(myname, delta * 1000))
        return result
    return new_func