import kandinsky as kd
from time import sleep
import ion

DEBUG_PRINT = False # Whether to print debug information.

# This file will contain all the UI classes that I've made before and want to actually use.
# For now I'm going to intergrate it using kdexpanded.py since it has all of the methods someone could ever dream of, actual implementation can contain less.

from kdexpanded import *

def debugprint(*args, **kwargs):
    if DEBUG_PRINT:
        print(*args, **kwargs)

class Text(KDString):
    def __init__(self,name,x,y,text,color='', bg=''):
        self.name = name
        super().__init__(text,KDPoint(x,y),color,bg)
    def _draw(self):
        for k,v in enumerate(self.string.split("\n")):
            kd.draw_string(v,self.x(),self.y()+k*18,self.color1,self.color2)

class Button(KDRect):
    border = 1
    def __init__(self,name,x,y,label,color='red'):
        self.name = name
        self.text = KDString(label,KDPoint(x+5, y+5),'black',color)
        super().__init__(x,y,self.text.width()+10,self.text.height()+10,color)
    def _draw(self):
        kd.fill_rect(self.x(),self.y(),self.width(),self.height(), "#555555")
        kd.fill_rect(self.x()+self.border,self.y()+self.border,self.width()-self.border*2,self.height()-self.border*2, self.color1)
        kd.draw_string(self.text.string,*self.text.origin(), self.text.color1, self.text.color2)
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
    border = 1
    def __init__(self,name,x,y,w,h,color):
        self.name = name
        self.input = KDString("",KDPoint(x+5,y+5),'black',color)
        super().__init__(x,y,w,h,color)
    def _draw(self):
        kd.fill_rect(self.x(),self.y(),self.width(),self.height(), "#555555")
        kd.fill_rect(self.x()+self.border,self.y()+self.border,self.width()-self.border*2,self.height()-self.border*2, self.color1)
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

class Toggle(KDRect):
    border = 1
    def __init__(self,name,x,y,label,color):
        self.name = name
        self.state = False
        self.text = KDString(label,KDPoint(x+5, y+5),'black',color)
        super().__init__(x,y,self.text.width()+40,self.text.height()+10,color)
    def _draw(self):
        kd.fill_rect(self.x(),self.y(),self.width(),self.height(), "#555555")
        kd.fill_rect(self.x()+self.border,self.y()+self.border,self.width()-self.border*2,self.height()-self.border*2, self.color1)
        kd.draw_string("[" + ("x" if self.state else " ") + "]" + self.text.string,*self.text.origin(), self.text.color1, self.text.color2)
    def width(self):
        return self.text.width() + 40
    def height(self):
        return self.text.height() + 10
    def setOrigin(self, point):
        super().setOrigin(point)
        self.text.setOrigin(point.translatedBy(KDPoint(5,5)))

class Screen:
    def __init__(self,name):
        self.name = name
        self.elements = []
    def add(self,element):
        if element not in self.elements:
            self.elements.append(element)
    def draw(self,*elements):
        for element in elements:
            if element not in self.elements:
                self.elements.append(element)
            element._draw()
    def refresh(self):
        for element in self.elements:
            element._draw()
