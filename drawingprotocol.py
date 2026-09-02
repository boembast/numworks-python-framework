import kandinsky as kd
from time import sleep

# This file is for designing a predefined way for elements to draw themselves.

class Drawer:
    def __init__(self):
        self.elements = { # Dictionary of per element; name: drawing_function
            "pixel": self._set_pixel,
            "rect": self._fill_rect,
            "string": self._draw_string
        }
        self.contents = {}
    def _set_pixel(self,x,y,color):
        kd.set_pixel(x,y,color)
    def _fill_rect(self,x,y,w,h,color):
        kd.fill_rect(x,y,w,h,color)
    def _draw_string(self,s:str,x,y,color1="black",color2="white"):
        for line_number, line in enumerate(s.split('\n')): # str.splitlines() IS NOT IN NUMWORKS
            kd.draw_string(line,x,y+line_number*18,color1,color2)
    def draw(self, identifier):
         if isinstance(identifier, tuple):
            self.elements.get(identifier[0], lambda: None)(*identifier[1:])
            return
         if identifier not in self.contents.keys():
            raise ValueError("Identifier '{identifier}' not found in contents.".format(identifier=identifier))
         call = self.contents[identifier]
         self.elements.get(call[0], lambda: None)(*call[1:])
    def cache(self, call):
        pointer = max(self.contents.keys(), default=-1)+1
        self.contents[pointer] = call
        return pointer
    def modify(self, identifier, new_call):
        if identifier not in self.contents.keys():
            raise ValueError("Identifier '{identifier}' not found in contents.".format(identifier=identifier))
        self.contents[identifier] = new_call
    def remove(self, identifier):
        if identifier not in self.contents.keys():
            raise ValueError("Identifier '{identifier}' not found in contents.".format(identifier=identifier))
        del self.contents[identifier]
    def exec(self, *call):
        pointers = []
        for c in call:
            pointers.append(self.cache(c))
        return pointers

# Example usage:
# myRectangle = ("rect", 10, 10, 50, 50, "red")
# myString = ("string", "Hello\nWorld", 20, 20, "black", "white")

# drawer = Drawer()
# myRectanglePointer = drawer.cache(myRectangle)
# myStringPointer = drawer.cache(myString)

# drawer.draw(myRectanglePointer)
# drawer.draw(myStringPointer)
# drawer.modify(myRectanglePointer, ("rect", 10, 10, 100, 100, "blue"))
# drawer.draw(myRectanglePointer)
# drawer.remove(myRectanglePointer)
# drawer.draw(("pixel", 15, 15, "green"))