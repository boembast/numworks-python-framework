from base import *

class OrderedContainer:
    """
    An OrderedContainer is a container that holds elements.
    It is used to group elements together and draw them in order.
    """
    def __init__(self,name: str,x: int,y: int):
        """
        Initialize a container.

        Note that the coordinates of the container 
        are the new origin point of any elements in 
        the container.

        :param name: name of the container
        :param x: x-coordinate of the container
        :param y: y-coordinate of the container
        """
    def directadd(self,*element: BaseElement, relative: bool = True):
        """
        Add an element to the container.

        :param element: one or more elements to be added.
        :param relative: whether the element's coordinates are relative to the container or absolute
        """