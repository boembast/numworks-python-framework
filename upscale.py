import kandinsky as kd
from time import sleep, monotonic
import ion

from functimer import timed_function

class steps:
    def __init__(self):
        self.steps = 0
    def __call__(self):
        self.steps += 1
    def __str__(self):
        return str(self.steps)

@timed_function
def draw_string_upscaled(text: str, scale: int, pos_x: int, pos_y: int):
    s = steps()
    kd.draw_string(text,pos_x,pos_y,"black","blue");s()
    textlength = len(text);s()
    for x in range(0+textlength*10-1,-1,-1):
        for y in range(17,-1,-1):
            kd.fill_rect(pos_x+x*scale, pos_y+y*scale, scale, scale, kd.get_pixel(pos_x+x, pos_y+y));s()
    print(f"Took {s} steps on {textlength} character(s)")

kd.draw_string("bob\nbob",0,0,"black","white")


draw_string_upscaled("b", 2, 0, 50)