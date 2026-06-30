import kandinsky as kd
from time import sleep
import ion

from base import *

DEBUG_PRINT = True

if DEBUG_PRINT:
    print("Debug printing is enabled")

draworder = []

class Screen:
    def __init__(self,name):
        self.name=name
        self._content = []
    def __name__(self):
        return self.__class__.__name__
    def add(self,elemtype,name,**kwargs):
        """
        The element type should be specified first, either as string or the class itself. Then the arguments for the element's constructor should be specified. The element will be created and added to the screen.
        """
        if isinstance(elemtype, str):
            elemtype = globals().get(elemtype)
        elif not issubclass(elemtype, BaseElement):
            raise ValueError("Screen.add() only accepts BaseElement subclasses or string to specify element type")
        element = elemtype(name, 30, len(self._content)*30,None, None **kwargs)
        self._content.append(element)
        return element

    def find(self,elementname,count=-1):
        found = []
        for elem in self._content:
            if elem.name == elementname:
                found.append(elem)
            if len(found) == count:
                break
        return found
    
    def draw(self,overwrite=False):
        global draworder
        if overwrite:
            kd.fill_rect(0,0,320,240,'white')
            draworder = []
        draw(*self._content)

class Button(BaseInteractible):
    def __init__(self,name,label,x,y,w=None,h=None,color='blue'):
        super().__init__(name,x,y,0,0)
        self.w = w if w is not None else textpixelsize(label)[0] + 10
        self.h = h if h is not None else textpixelsize(label)[1] + 10
        self.label = label
        self.color = color
        self.active = False
        self.BORDER = 1

    def _draw(self,force=False):
        gottencolor = self.getcolor(selected=self.active)
        kd.fill_rect(self.x,self.y,self.w,self.h, self.color)
        kd.fill_rect(self.x+self.BORDER,self.y+self.BORDER,self.w-2*self.BORDER,self.h-2*self.BORDER, gottencolor)
        kd.draw_string(self.label,self.x+5,self.y+5,'black',gottencolor)
        debugprint("Drew",self.name,self.color)
    
    def _activate(self):
        """
        Toggle activation
        """
        self.active = not self.active
        debugprint("Activated",self.name,"now active:",self.active)

class TextLabel(BaseElement):
    def __init__(self,name,text,x,y,w=None,h=None,color='white'):
        super().__init__(name,x,y,0,0)
        self.w = w if w is not None else textpixelsize(text)[0] + 2
        self.h = h if h is not None else textpixelsize(text)[1] + 2
        self.text = text
        self.color = color

    def _draw(self,force=False):
        kd.fill_rect(self.x,self.y,self.w,self.h, self.color)
        kd.draw_string(self.text,self.x+1,self.y+1,'black',self.color)
        debugprint("Drew",self.name,self.color)

class OrderedContainer(BaseElement):
    def __init__(self,name,x,y):
        super().__init__(name,x,y,0,0)
        self.name=name
        self._content = []
        self.__name__ = self.__class__.__name__
        self.appendable = False

    def _append(self,element):
        self._content.append(element)
        edgelist = []
        for elem in self._content:
            edgelist.append(elem.getbounds())
        minx = min([e[0] for e in edgelist])
        miny = min([e[1] for e in edgelist])
        maxx = max([e[0]+e[2] for e in edgelist])
        maxy = max([e[1]+e[3] for e in edgelist])
        self.x = minx
        self.y = miny
        self.w = maxx - minx
        self.h = maxy - miny
        

    def directadd(self,*element, relative = True):
        for elem in element:
            if not isinstance(elem, BaseElement):
                print("Warning: Screen.directadd() only accepts BaseElement instances and derived classes")
                continue
            if relative:
                elem.x += self.x
                elem.y += self.y
            self._append(elem)
    def find(self,elementname):
        for elem in self._content:
            if elem.name == elementname:
                return elem

    def _draw(self,force=False):
        for elem in self._content:
            draw(elem)

def draw(*which):
    """
    Draw or redraw one or multiple elements on the screen.
    """
    global draworder
    for elem in which:
        if not isinstance(elem, BaseElement):
            print("Warning: draw() called with non-BaseElement argument:", elem)
            continue
        if not elem in draworder:
            elem._draw(force=True)
            if elem.appendable:
                draworder.append(elem)
            # sleep(0.5) # Sleep to make the drawing process visible
            continue
        current = draworder.index(elem)
        elem._draw()
        # sleep(0.5)
        for i in draworder[current+1:]:
            if elem.overlapswith(i.getbounds()):
                i._draw()
                # sleep(0.5)

beep = Button("beep", "Beep", 0, 0, color='blue')
boop = Button("boop", "Boop", 0, 50, color='green')
container = OrderedContainer("container", 10, 10)
container.directadd(beep,boop)
draw(container)
print(container.getbounds())
sleep(1)
beep._activate()
draw(container)