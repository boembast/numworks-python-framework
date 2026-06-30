import kandinsky as kd
from time import sleep
draworder = []
# Class to store data about an element

class pos:
    def __init__(self,x,y):
        self.x,self.y=x,y
class Element:
    def __init__(self,name,x,y):
        self.name,self.x,self.y=name,x,y
        self._hist=(name,x,y)
    def _draw(self,force=False):
        print("Warning: {}._draw() called but not implemented".format(self.__class__.__name__))
    def _bounds(self):
        print("Warning: {}._bounds() called but not implemented".format(self.__class__.__name__))

class rect(Element):
    def __init__(self,name,x,y,w,h,color='red'):
        super().__init__(name,x,y)
        self.w,self.h=w,h
        self.color=color
        self._hist=(name,x,y,w,h,color)

    def _draw(self,force=False):
        kd.fill_rect(self.x,self.y,self.w,self.h, self.color)
        print("Drew",self.name,self.color)

    
    def getrect(self):
        return self.x,self.y,self.w,self.h

    def chpos(self,x,y):
        self.x,self.y=x,y
    
    @staticmethod
    def overlaps(r1, r2):
        ax, ay, aw, ah = r1
        bx, by, bw, bh = r2
        return (
            bx + bw > ax and
            ax + aw > bx and 
            by + bh > ay and
            ay + ah > by
            )


def draw(*which):
    """
    Draw or redraw one or multiple elements on the screen.
    """
    global draworder
    for elem in which:
        if not elem in draworder:
            elem._draw(force=True)
            draworder.append(elem)
            sleep(0.5) # Sleep to make the drawing process visible
            continue
        current = draworder.index(elem)
        elem._draw()
        sleep(0.5)
        for i in draworder[current+1:]:
            if rect.overlaps(rect.getrect(elem), rect.getrect(i)):
                i._draw()
                sleep(0.5)
    

#Example elements
Element("test",10,10)._draw() #Prints warning to indicate that ._draw() has to be implemented in a subclass
beggin = rect("beggin",10,10,55,30,'red')
sample = rect("sample",10,20,10,10,'blue')
otherone = rect("otherone",10,30,10,10,'green')
more = rect("more",10,40,10,10,'yellow')
draw(beggin,sample,otherone,more)
sleep(1)
draw(beggin)