import kandinsky as kd
from time import sleep
import ion

from kdexpanded import KDRect, KDPoint, KDString

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
            return KDPoint(x,y)
        kd.set_pixel(x,y,color)
    def _fill_rect(self,x,y,w,h,color,_cache=False):
        if _cache:
            return KDRect(x,y,w,h)
        kd.fill_rect(x,y,w,h,color)
    def _draw_string(self,s:str,x,y,color1="black",color2="white",_cache=False):
        if _cache:
            return KDString(s, KDPoint(x,y), color1, color2)
        for line_number, line in enumerate(s.splitlines()):
            kd.draw_string(line,x,y+line_number*18,color1,color2)
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

drawer.draw(("string", "Hello\nWorld", 20, 20, "black", "white"))