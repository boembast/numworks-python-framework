import kandinsky as kd
from time import sleep
import ion

from base import *

# New kbd_intr key is going to be 14 aka KEY_XNT.

#FLAGS
BUTTON_LABEL_FORCE_FIT = False # Whether to extend a button's width to fit its label.
DEBUG_PRINT = False # Whether to print debug information. Does not affect warnings.
#END_FLAGS

#DO NOT TOUCH
draworder = []

class Screen:
    def __init__(self,name):
        self.name=name
        self._content = []
    def __name__(self):
        return self.__class__.__name__
    def add(self,elemtype,*args,**kwargs):
        """
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
        element._draw(force=True)
    
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

    def draw(self,overwrite=False):
        global draworder
        if overwrite:
            kd.fill_rect(0,0,320,240,'white')
            draworder = []
        draw(*self._content)

def debugprint(*args, **kwargs):
    if DEBUG_PRINT:
        print(*args, **kwargs)



# element_name: list(nonselected_color[, selected_color])
colors = {
    'DEBUG': ('pink', 'cyan'),
    'button': ('gray', (173, 173, 255))
}


def getcolor(element,selected=False):
    debugprint("Getting color for",element.__class__.__name__, "selected:", selected)
    element = element if isinstance(element, str) else element.__class__.__name__
    return colors.get(element, ('purple','yellow'))[1 if selected else 0]

def textpixelsize(text:str):
    lines = text.split("\n")
    max_width = max(len(line) for line in lines)
    height = len(lines)
    return max_width * 10, height * 18

class Rect(BaseElement):
    def __init__(self,name,x,y,w,h,color='red'):
        super().__init__(name,x,y,["x","y","w","h","color"])
        self.w,self.h=w,h
        self.color=color

    def _draw(self,force=False):
        kd.fill_rect(self.x,self.y,self.w,self.h, self.color)
        debugprint("Drew",self.name,self.color)

    def change(self,**kwargs):
        for k,v in kwargs.items():
            if not k in self._validprops:
                raise ValueError("Invalid property name: {}".format(k))
            debugprint("Changing",self.name,"property",k,"from",getattr(self,k),"to",v)
            setattr(self, k, v)

class Button(BaseInteractible):
    def __init__(self,name,x,y,w=None,h=None,color='red',label=""):
        super().__init__(name,x,y,['x','y','w','h','color','label'])
        self.w = w if w is not None else textpixelsize(label)[0] + 10
        self.h = h if h is not None else textpixelsize(label)[1] + 10
        self.color=color
        if len(label)*10 > self.w-10:
            if BUTTON_LABEL_FORCE_FIT:
                self.w = len(label)*10 + 10
            else:
                print("Warning: Label '{}' is too long for button '{}'".format(label,name))
        self.label=label
        self.active=False
        self.BORDER = 1
    def _draw(self,force=False):
        gottencolor = getcolor(self, selected=self.active)
        kd.fill_rect(self.x,self.y,self.w,self.h, self.color)
        kd.fill_rect(self.x+self.BORDER,self.y+self.BORDER,self.w-2*self.BORDER,self.h-2*self.BORDER, gottencolor)
        kd.draw_string(self.label,self.x+5,self.y+5,'black',gottencolor)
        debugprint("Drew",self.name,self.color)
    def _activate(self):
        """
        Toggle activation
        """
        debugprint("Activated",self.name)
        self.active=not self.active
        gottencolor = getcolor(self, selected=self.active)
        kd.fill_rect(self.x+self.BORDER,self.y+self.BORDER,self.w-2*self.BORDER,self.h-2*self.BORDER, gottencolor)
        kd.draw_string(self.label,self.x+5,self.y+5,'black',gottencolor)
        debugprint("Redrew",self.name,self.color)

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

#Example elements
# Element("test",10,10)._draw() #Prints warning to indicate that ._draw() has to be implemented in a subclass
# beggin = rect("beggin",10,10,55,30,'red')
# sample = rect("sample",10,20,10,10,'blue')
# otherone = rect("otherone",10,30,10,10,'green')
# more = rect("more",10,40,10,10,'yellow')
# draw(beggin,sample,otherone,more)
# sleep(1)
# draw(beggin)

BUTTON_LABEL_FORCE_FIT = True

DEBUG_PRINT = True

# firstbutton = button("testbutton",10,10,color='red',label='Test but very long text now')
# draw(firstbutton)
# while not ion.keydown(ion.KEY_OK): pass
# firstbutton._activate()
# draw(firstbutton)

home = Screen("home")
home.add(Button,"testbutton",10,10,color='red',label='Test but very long text now')
home.draw()
sleep(1)
home.find("testbutton")._activate()
home.draw()