from typing import Any, Iterable, Iterator, Protocol, Union

class BaseElement:
    """
    This is the base element that all other elements inherit from.
    To be specific, only all static elements should inherit from this class. 
    All interactible elements should inherit from BaseInteractible.
    It contains the basic properties and methods that all elements should have.
    """
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name: str = name
        self.x: int = x
        self.y: int = y
    def _draw(self, force: bool = False) -> None:
        """
        This method is called when the element is drawn to the screen.
        It should be overridden by the child class to implement the drawing logic.
        """
        print("Warning: {}._draw() called but not implemented".format(self.__class__.__name__))
    def _bounds(self) -> None:
        """
        This method is called when the element's bounds are needed.
        It should be overridden by the child class to implement the bounds logic.
        """
        print("Warning: {}._bounds() called but not implemented".format(self.__class__.__name__))
    

class BaseInteractible(BaseElement):
    def __init__(self, name: str, x: int, y: int) -> None: ...
    def _activate(self) -> None: ...

BUTTON_LABEL_FORCE_FIT: bool
DEBUG_PRINT: bool

draworder: list[BaseElement]

def debugprint(*args: Any, **kwargs: Any) -> None: ...

colors: dict[str, tuple[str | tuple[int, int, int], str | tuple[int, int, int]]]

def getcolor(element: str | BaseElement, selected: bool = False) -> tuple[str | tuple[int, int, int], str | tuple[int, int, int]]:
    """
    Docstring for getcolor

    :param element: The class to get the color for. 
    :param selected: Whether the element is selected or not.
    :return: Colors for not selected or selected state.
    :rtype: tuple
    """

def textpixelsize(text: str) -> tuple[int, int]:
    """
    Returns the width and height of a text string in pixels.
    """

class rect(BaseElement):
    def __init__(self, name: str, x: int, y: int, w: int, h: int, color: str = 'red') -> None: ...
    def _draw(self, force: bool = False) -> None: ...
    def getrect() -> tuple[int, int, int, int]: ...
    def chpos(x,y) -> None: ...
    @staticmethod
    def overlaps(r1: tuple[int, int, int, int], r2: tuple[int, int, int, int]) -> bool: ...
