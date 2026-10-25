import kandinsky as kd
from time import sleep
import ion

DEBUG_PRINT = False # Whether to print debug information.

# This file will contain all the UI classes that I've made before and want to actually use.
# For now I'm going to intergrate it using kdexpanded.py since it has all of the methods someone could ever dream of, actual implementation can contain less.

from kdexpanded import *

ELEMENT_COLORS = {
    'DEBUG': ('pink', 'cyan'),
    'Button': ('gray', (173, 173, 255)),
    'BaseElement': ('pink', 'cyan'),
    'BaseInteractible': ('pink', 'cyan')
}

def debugprint(*args, **kwargs):
    if DEBUG_PRINT:
        print(*args, **kwargs)

class BaseElement(KDRect):
    def __init__(self,name,x,y,w,h):
        self.name = name
        super().__init__(x,y,w,h)
    def _draw(self):
        print("Warning: {}._draw() called but not implemented".format(self.__class__.__name__))
        return "problem"

class Text(KDString):
    def __init__(self,name,x,y,text,color='', bg=''):
        self.name = name
        super().__init__(text,KDPoint(x,y),color,bg)
    def _draw(self):
        for k,v in enumerate(self.string.split("\n")):
            kd.draw_string(v,self.x(),self.y()+k*18,self.color1,self.color2)

class Button(KDRect):
    def __init__(self,name,x,y,label,color='red'):
        self.name = name
        self.focus = False
        self.text = KDString(label,KDPoint(x+5, y+5),'black',color)
        super().__init__(x,y,self.text.width()+10,self.text.height()+10,color)
    def _draw(self):
        kd.fill_rect(self.x(),self.y(),self.width(),self.height(), self.color1)
        kd.draw_string(self.text.string,*self.text.origin(), self.text.color1, self.text.color2)
    def x(self):
        return super().x()
    def y(self):
        return super().y()
    def width(self):
        return self.text.width() + 10
    def height(self):
        return self.text.height() + 10
    def setOrigin(self, point):
        super().setOrigin(point)
        self.text.setOrigin(point.translatedBy(KDPoint(5,5)))
    def setSize(self, width, height):
        pass # Buttons should not be resized, they should be resized by changing the label.

class Input(KDRect):
    def __init__(self,name,x,y,w,h,color):
        self.name = name
        self.input = KDString("",KDPoint(x+5,y+5),'black',color)
        super().__init__(x,y,w,h,color)
    def _draw(self):
        kd.fill_rect(self.x(),self.y(),self.width(),self.height(), self.color1)
        kd.draw_string(self.input.string,*self.input.origin(), self.input.color1, self.input.color2)
    def x(self):
        return super().x()
    def y(self):
        return super().y()
    def width(self):
        return super().width()
    def height(self):
        return super().height()
    def setOrigin(self, point):
        super().setOrigin(point)
        self.input.setOrigin(point.translatedBy(KDPoint(5,5)))
    def setSize(self, width, height):
        super().setSize(width, height)
    def setText(self, text):
        self.input.string = text
        self._draw()
