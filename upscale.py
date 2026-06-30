import kandinsky as kd
from time import sleep, monotonic
import ion

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = monotonic()
        result = f(*args, **kwargs)
        delta = monotonic() - t
        print('Function {} Time = {:6.3f}ms'.format(myname, delta * 1000))
        return result
    return new_func

@timed_function
def draw_string_upscaled(text: str, scale: int, pos_x: int, pos_y: int):
    kd.draw_string(text,pos_x,pos_y,"black","blue")
    textlength = len(text)
    for x in range(0+textlength*10-1,-1,-1):
        for y in range(17,-1,-1):
            kd.fill_rect(pos_x+x*scale, pos_y+y*scale, scale, scale, kd.get_pixel(pos_x+x, pos_y+y))

kd.draw_string("bob\nbob",0,0,"black","white")


draw_string_upscaled("bob", 2, 0, 50)