from _typeshed import Incomplete, Self
from collections.abc import Generator
from typing import Union

KDColor = Union[str, tuple[int, int, int]]

class KDPoint:
    """
    Represents a point on the screen with x and y coordinates.

    The iterator of this class yields the x and y coordinates in order.
    """
    def __init__(self, x: int, y: int, color1: 'KDColor' = "") -> None:
        """
        Initializes a new KDPoint with the given coordinates.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
            color1 (str, optional): An optional color attribute for the point. Defaults to an empty string. This can be used with `kandinsky.set_pixel`.

        You can also use the static `.KDPointZero()` method to create a KDPoint at the origin (0, 0).
        See this method for more information.

        Examples:
            Create a point at coordinates (10, 20)
            >>> point = KDPoint(10, 20)
            >>> point.x()
            10
            >>> point.struct()
            [10, 20]

            Create a point at the origin
            >>> origin = KDPoint.KDPointZero()
            >>> origin.x()
            0
            >>> origin.struct()
            [0, 0]
        """
    def __iter__(self): ...
    def __repr__(self) -> str:
        """
        Returns a string representation of the KDPoint in the format "KDPoint(x=<x>, y=<y>)".
        """
    def struct(self) -> list[int]:
        """
        Returns the internal structure of the KDPoint as a list of two integers [x, y].
        """
    def x(self) -> int:
        """
        Returns the x-coordinate of the KDPoint.
        """
    def y(self) -> int:
        """
        Returns the y-coordinate of the KDPoint.
        """
    def translatedBy(self, point: 'KDPoint') -> 'KDPoint':
        """
        Returns self translated by the given KDPoint.
        So additive.
        """
    def relativeTo(self, other: 'KDPoint') -> 'KDPoint':
        """
        Returns self relative to the given KDPoint.
        This is equivalent to translating self by the opposite of other.
        So subtractive.
        """
    def opposite(self) -> 'KDPoint':
        """
        Returns self with both coordinates negated.
        """
    def __eq__(self, other: 'KDPoint') -> bool: ...
    def __ne__(self, other: 'KDPoint') -> bool: ...
    def squareDistanceTo(self, other: 'KDPoint') -> int:
        """
        Returns the square of the distance between this point and the other point.
        Aka it applies the pythagorean theorem.
        """
    @staticmethod
    def KDPointZero() -> 'KDPoint':
        """
        Returns a KDPoint at the origin (0, 0).
        """

class KDRect:
    def __init__(self, x: int, y: int, w: int, h: int, color1: 'KDColor' = "") -> None: #TODO: There should also be a way to pass a tuple to the constructor, not sure how to implement that against type-checking and such yet.
        """
        Initializes a new KDRect with the given position and size.

        Args:
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            w (int): The width of the rectangle.
            h (int): The height of the rectangle.

        You can also use the static `.fromtuple()` method to create a KDRect from the tuple representation of rectangle elements.
        See this method for more information.

        See the example below.
        
        Examples:
            Create a rectangle at position (10, 20) with width 100 and height 50
            >>> rect = KDRect(10, 20, 100, 50)
            >>> rect.x()
            10
            >>> rect.struct()
            [10, 20, 100, 50]

            Create a rectangle from a tuple representation
            >>> rect = KDRect.fromtuple(('rect', 25, 30, 10, 30))
            >>> rect.x()
            25
            >>> rect.struct()
            [25, 30, 10, 30]

        """
    def __iter__(self): ...
    def __repr__(self) -> str:
        """
        Returns a string representation of the KDRect in the format "KDRect(x=<x>, y=<y>, w=<w>, h=<h>)".
        """
    def struct(self) -> tuple[int, int, int, int]:
        """
        Returns the internal structure of the KDRect as a tuple of four integers (x, y, w, h).
        """
    def x(self) -> int:
        """
        Returns the x-coordinate of the top-left corner of the KDRect.
        """
    def y(self) -> int:
        """
        Returns the y-coordinate of the top-left corner of the KDRect.
        """
    def origin(self) -> tuple[int, int]:
        """
        Returns the coordinates of the top-left corner of the KDRect as a tuple (x, y).
        """
    def width(self) -> int:
        """
        Returns the width of the KDRect.
        """
    def height(self) -> int:
        """
        Returns the height of the KDRect.
        """
    def size(self) -> tuple[int, int]:
        """
        Returns the size of the KDRect as a tuple (width, height).
        """
    def top(self) -> int:
        """
        Returns the y-coordinate of the top edge of the KDRect.
        """
    def right(self) -> int:
        """
        Returns the x-coordinate of the right edge of the KDRect.
        This is calculated as x + width - 1
        """
    def bottom(self) -> int:
        """
        Returns the y-coordinate of the bottom edge of the KDRect.
        This is calculated as y + height - 1
        """
    def left(self) -> int:
        """
        Returns the x-coordinate of the left edge of the KDRect.
        """
    def topLeft(self) -> tuple[int, int]:
        """
        Returns the coordinates of the top-left corner of the KDRect as a tuple (x, y).
        """
    def topRight(self) -> tuple[int, int]:
        """
        Returns the coordinates of the top-right corner of the KDRect as a tuple (x, y).
        This is calculated as (x + width - 1, y)
        """
    def bottomLeft(self) -> tuple[int, int]:
        """
        Returns the coordinates of the bottom-left corner of the KDRect as a tuple (x, y).
        This is calculated as (x, y + height - 1)
        """
    def bottomRight(self) -> tuple[int, int]:
        """
        Returns the coordinates of the bottom-right corner of the KDRect as a tuple (x, y).
        This is calculated as (x + width - 1, y + height - 1)
        """
    def isValid(self) -> bool:
        """
        Returns True if the KDRect has a positive width and height, otherwise False.
        """
    def __eq__(self, other: 'KDRect') -> bool: ...
    def __ne__(self, other: 'KDRect') -> bool: ...
    def setOrigin(self, point: 'KDPoint') -> None:
        """
        Sets the origin (top-left corner) of the KDRect to the given KDPoint.

        Args:
            point (KDPoint): The new origin point for the rectangle.
        """
    def setSize(self, w: int, h: int) -> None:
        """
        Sets the size of the KDRect to the given width and height.

        Args:
            w (int): The new width of the rectangle.
            h (int): The new height of the rectangle.
        """
    def translatedBy(self, point: 'KDPoint') -> 'KDRect':
        """
        Returns a new KDRect that is self translated by the given KDPoint.

        Args:
            point (KDPoint): The point by which to translate the rectangle.
        """
    def relativeTo(self, other: 'KDPoint') -> 'KDRect':
        """
        Returns a new KDRect that is self relative to the given KDPoint.
        This is equivalent to translating self by the opposite of other.

        Args:
            other (KDPoint): The point relative to which the rectangle will be adjusted.
        """
    def movedTo(self, point: 'KDPoint') -> 'KDRect':
        """
        Returns a new KDRect of self with the origin as the given KDPoint.

        Args:
            point (KDPoint): The new top-left corner for the rectangle.
        """
    def intersects(self, other: 'KDRect') -> bool:
        """
        Returns True if there is overlap between self and the given KDRect, otherwise False.

        Args:
            other (KDRect): The rectangle to check for intersection with self.
        """
    def intersectedWith(self, other: 'KDRect') -> 'KDRect':
        """
        Returns a new KDRect that is the intersection of self and the given KDRect.
        If there is no intersection, returns an empty KDRect.
        Intersection meaning overlap.

        Args:
            other (KDRect): The rectangle to intersect with self.
        """
    def unionedWith(self, other: 'KDRect') -> 'KDRect':
        """
        Returns a new KDRect that is the smallest rectangle that contains both self and the given KDRect.

        Args:
            other (KDRect): The rectangle to union with self.
        """
    def differencedWith(self:KDRect, other: 'KDRect') -> list['KDRect']:
        """
        Returns a list of KDRects that represent the area of self that is not overlapped by the given KDRect.
        If there is no overlap, returns a list containing self.
        If self is completely overlapped by other, returns an empty list
        You can also check complete overlap with `.containsRect(other)`.

        Args:
            other (KDRect): The rectangle to subtract from self.
        """
    def contains(self, point: 'KDPoint') -> bool:
        """
        Whether the given KDPoint is inside self.
        Edge counts as inside.

        Args:
            point (KDPoint): The point to check for containment within self.
        """
    def containsRect(self, other: 'KDRect') -> bool:
        """
        Whether the given KDRect is completely inside self.
        Edge counts as inside.

        Args:
            other (KDRect): The rectangle to check for containment within self.
        """
    def isEmpty(self) -> bool:
        """
        Whether the width or height is not positive (`<= 0`).
        """
    @staticmethod
    def KDRectZero() -> 'KDRect':
        """
        Returns a KDRect at the origin (0, 0) with width and height of 0.
        """
    @staticmethod
    def fromtuple(tuple) -> 'KDRect':
        """
        Creates a KDRect from a tuple representation of rectangle elements.
        The tuple should be in the format ('rect', x, y, w, h).

        Args:
            tuple (tuple): A tuple representing the rectangle.

        Returns:
            KDRect: A new KDRect instance created from the tuple.
        """

class KDString:
    """
    Represents a string on the screen with position and color attributes.
    It is special in the way that its width and height are dynamically calculated based on the string.
    This allows for greater compatibility with KDRect.
    """
    string: str
    string_old: str
    color1: KDColor
    color2: KDColor
    def __init__(self, string, point, color1: 'KDColor' = 'black', color2: 'KDColor' = 'white') -> None:
        """
        Initializes a new KDString with the given string, position, and colors.

        Args:
            string (str): The text string to be represented.
            point (KDPoint): The position of the string on the screen.
            color1 (KDColor, optional): The primary color of the string. Defaults to 'black'.
            color2 (KDColor, optional): The secondary color of the string. Defaults to 'white'.

        Note:
            The colors can be specified as either a string (e.g., 'red') or a tuple of RGB values (e.g., (255, 0, 0)).
        """
    def __iter__(self): ...
    def __len__(self) -> int:
        """
        Returns the length of the string.
        """
    def struct(self):
        """
        Returns the internal structure of the KDString as a list containing the position and size.
        The structure is in the format [x, y, width, height].
        """
    def x(self):
        """
        Returns the x-coordinate of the position of the KDString.
        """
    def y(self): 
        """
        Returns the y-coordinate of the position of the KDString.
        """
    def origin(self):
        """
        Returns the position of the KDString as a tuple (x, y).
        """
    def width(self): 
        """
        Returns the width of the KDString, calculated based on the length of the line with the most amount of characters.
        """
    def height(self):
        """
        Returns the height of the KDString, calculated based on the number of lines in the string.
        """
    def size(self):
        """
        Returns the size of the KDString as a tuple (width, height).
        """
    def top(self):
        """
        Returns the y-coordinate of the top edge of the KDString.
        """
    def right(self):
        """
        Returns the x-coordinate of the right edge of the KDString.
        This is calculated as x + width - 1
        """
    def bottom(self):
        """
        Returns the y-coordinate of the bottom edge of the KDString.
        This is calculated as y + height - 1
        """
    def left(self):
        """
        Returns the x-coordinate of the left edge of the KDString.
        This is calculated as x.
        """
    def topLeft(self):
        """
        Returns the position of the top-left corner of the KDString as a tuple (x, y).
        """
    def topRight(self):
        """
        Returns the position of the top-right corner of the KDString as a tuple (x, y).
        """
    def bottomLeft(self):
        """
        Returns the position of the bottom-left corner of the KDString as a tuple (x, y).
        """
    def bottomRight(self):
        """
        Returns the position of the bottom-right corner of the KDString as a tuple (x, y).
        """
    def isValid(self):
        """
        Returns True if the KDString has a positive width and height, otherwise False.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def setOrigin(self, point) -> None:
        """
        Sets the origin (top-left corner) of the KDString to the given KDPoint.

        Args:
            point (KDPoint): The new origin point for the string.
        """
    def contains(self, point):
        """
        Whether the given KDPoint is inside the string.
        Edge counts as inside.

        Args:
            point (KDPoint): The point to check for containment within self.
        """
    def containsRect(self, other):
        """
        Whether the given KDRect is completely inside the string.
        Edge counts as inside.

        Args:
            other (KDRect): The rectangle to check for containment within self.
        """
    def isEmpty(self):
        """
        Whether the width or height is not positive (`<= 0`).
        """
    def charpos(self, index):
        """
        Returns the rectangle of the first-found character at the given index as a KDRect.
        The index is zero-based, and if the index is out of bounds, it returns None.

        Args:
            index (int): The index of the character in the string.
        """
    def yieldcharrect(self) -> Generator[tuple[str, KDRect], None, None]:
        """
        Yields tuples of characters and their corresponding rectangles (KDRect) for each character in the string.
        The rectangles are calculated based on the position and size of the string.
        Whenever a newline character is encountered, yield returns `('next', KDRect.KDRectZero())` instead.
        ^ The functionality a bit more nuanced, but this is the gist of it.

        Yields:
            tuple[str, KDRect]: A tuple containing a character and its corresponding rectangle.
        """
    @staticmethod
    def fromtuple(tuple): ...
