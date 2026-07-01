DEBUG_PRINT = False


def debugprint(*args, **kwargs):
    if DEBUG_PRINT:
        print(*args, **kwargs)

def textpixelsize(text:str):
    lines = text.split("\n")
    max_width = max(len(line) for line in lines)
    height = len(lines)
    return max_width * 10, height * 18

colors = {
    'DEBUG': ('pink', 'cyan'),
    'Button': ('gray', (173, 173, 255)),
    'BaseElement': ('pink', 'cyan'),
    'BaseInteractible': ('pink', 'cyan')
}

class BaseElement:
    def __init__(self,name,x,y,w,h,validprops=["name","x","y","w","h"]):
        if any(i < 0 for i in [x,y,w,h]):
            raise ValueError("x({}), y({}), w({}) and h({}) for {} '{}' must be non-negative".format(x, y, w, h, self.__class__.__name__, name))
        self.name,self.x,self.y,self.w,self.h=name,x,y,w,h
        self._conf = {} # Configuration dictionary for subclasses to use
        self.appendable = True
        if validprops is not None:
            self._validprops = validprops
    def _draw(self,force=False):
        print("Warning: {}._draw() called but not implemented".format(self.__class__.__name__))
        return "problem"
    def getcolor(self,selected=False):
        debugprint("Getting color for",self.__class__.__name__, "selected:", selected)
        return colors.get(self.__class__.__name__,('purple','yellow'))[1 if selected else 0]
    def getbounds(self):
        return self.x,self.y,self.w,self.h
    def change(self,**kwargs):
        for k,v in kwargs.items():
            if not k in self._validprops:
                raise ValueError("Invalid property name: {}".format(k))
            debugprint("Changing",self.name,"property",k,"from",getattr(self,k),"to",v)
            setattr(self, k, v)

    def overlapswith(self, r2):
        ax, ay, aw, ah = self.getbounds()
        bx, by, bw, bh = r2
        return (
            bx + bw > ax and
            ax + aw > bx and 
            by + bh > ay and
            ay + ah > by
            )
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
    @staticmethod
    def temporaryobject(self, *args, **kwargs):
        """
        Create a temporary object of the same class as self with the given arguments.
        This is useful for creating temporary objects for comparison or other purposes.
        Name is not possible to be set.
        """
        temporary = self.__class__("temp", *args, **kwargs)
        temporary.appendable = False
        return temporary

class BaseInteractible(BaseElement):
    def __init__(self,name,x,y,w,h,validprops=None):
        super().__init__(name,x,y,w,h,validprops)
    def _activate(self):
        print("Warning: {}._activate() called but not implemented".format(self.__class__.__name__))
    def getcolor(self,selected=False):
        debugprint("Getting color for",self.__class__.__name__, "selected:", selected)
        return colors.get(self.__class__.__name__,('purple','yellow'))[1 if selected else 0]