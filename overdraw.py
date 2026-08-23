import kandinsky as kd
from time import sleep
import ion

from base import *

class Screen:
    def __init__(self,name):
        self.name=name
        self._content = []
    def getclassname(self):
        return self.__class__.__name__
    def add(self,elemtype,*args,**kwargs): #TODO: Scheduled for removal
        """
        <b>This function is deprecated, use Screen.directadd() instead.</b>

        The element type should be specified first, either as string or the class itself. Then the arguments for the element's constructor should be specified. The element will be created and added to the screen.
        """
        if isinstance(elemtype, str):
            elemtype = globals().get(elemtype)
        elif not issubclass(elemtype, BaseElement):
            raise ValueError("Screen.add() only accepts BaseElement subclasses or string to specify element type")
        element = elemtype(*args,**kwargs)
        self._content.append(element)
        return element

    def find(self,elementname,count=-1):
        for elem in self._content:
            if elem.name == elementname:
                return elem

    def directadd(self,element):
        if not isinstance(element, BaseElement):
            raise ValueError("Screen.directadd() only accepts BaseElement instances")
        self._content.append(element)
    
    def activate(self,elementprop):
        # If the contents list does not contain an element with this name
        if not (isinstance(elementprop, int) or isinstance(elementprop, str)):
            raise ValueError("Screen.activate() only accepts index of an element or their names")
        if isinstance(elementprop, int):
            element = self._content[elementprop%len(self._content)]
        elif isinstance(elementprop, str):
            found = self.find(elementprop,1)
            if isinstance(found, tuple):
                raise ValueError("Multiple elements found with name '{}'".format(elementprop))
            element = found
        if element:
            element._activate()

    def _draw(self,overwrite=False):
        self.draw(overwrite)

    def draw(self,overwrite=False):
        global draworder
        if overwrite:
            kd.fill_rect(0,0,320,240,'white')
            draworder = []
        draw(*self._content)

class Rect(BaseElement):
    def __init__(self,name,x,y,w,h,fillcolor="black",validprops=["name","x","y","w","h","fillcolor"]):
        super().__init__(name,x,y,w,h,validprops)
        self.fillcolor = fillcolor
    def _draw(self,force=False):
        kd.fill_rect(self.x,self.y,self.w,self.h,self.fillcolor)

def draw(*which):
    """
    Draw or redraw one or multiple elements on the screen.
    """
    global draworder
    for elem in which:
        if not isinstance(elem, BaseElement):
            print("Warning: draw() called with non-BaseElement argument:{", elem,"}; Ignoring")
            continue
        if not elem in draworder:
            elem._draw(force=True)
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