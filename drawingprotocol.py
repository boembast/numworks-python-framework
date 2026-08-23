import kandinsky as kd
from time import sleep
import ion

# This file is for designing a predefined way for elements to draw themselves.

class Drawer:
    def __init__(self):
        self.elements = { # Dictionary of per element: name : (drawing_function, caching_function)
            "pixel": self._set_pixel,
            "rect": self._fill_rect,
            "string": self._draw_string
        }
    def _set_pixel(self,x,y,color,_cache=False):
        if _cache:
            return [[x,y]]
        kd.set_pixel(x,y,color)
    def _fill_rect(self,x,y,w,h,color,_cache=False):
        if _cache:
            return [[x,y],[x+w,y],[x+w,y+h],[x,y+h]]
        kd.fill_rect(x,y,w,h,color)
    def _draw_string(self,s,x,y,color1="black",color2="white",_cache=False):
        if _cache:
            lines = s.split("\n")
            max_width = max(len(line) for line in lines) * 10
            height = len(lines) * 18
            return [[x,y],[x+max_width,y],[x+max_width,y+height],[x,y+height]]
        kd.draw_string(s,x,y,color1,color2)
    def draw(self, call):
        self.elements.get(call[0], lambda: None)(*call[1:])
    def cache(self, call):
        """
        The caching function returns the space a drawing call takes up, so that it can be used for collision detection and other purposes.
        """
        return self.elements.get(call[0], lambda: None)(*call[1:], _cache=True)
    def exec(self, *call):
        """
        Execute a drawing call, and return the space it takes up.
        """
        total_drawn = []
        for c in call:
            total_drawn.append(self.cache(c))
        return total_drawn

# Example usage:
myRectangle = ("rect", 10, 10, 50, 50, "red")

drawer = Drawer()
print(drawer.cache(myRectangle))
print(drawer.cache(("string", "Hello\nWorld", 20, 20, "black", "white")))