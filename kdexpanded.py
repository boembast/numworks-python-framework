# This file contains most of the work of porting a few of the header and C++ files of Kandinsky
# The goal is to have this in the main code, but for now it is in a separate file for organization
# and easier testing across different files.

class KDPoint:
    class __struct:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    def __init__(self, x, y):
        self._struct = self.__struct(x, y)

    def __repr__(self):
        return "KDPoint(x={0}, y={1})".format(self.x(), self.y())
    def __iter__(self):
        yield self.x()
        yield self.y()
    
    def struct(self):
        return self._struct

    def x(self):
        return self._struct.x
    def y(self):
        return self._struct.y
    def translatedBy(self, point):
        return KDPoint(self.x() + point.x(), self.y() + point.y())
    def relativeTo(self, other):
        return self.translatedBy(other.opposite())
    def opposite(self):
        return KDPoint(-self.x(), -self.y())
    def __eq__(self, other):
        return self.x() == other.x() and self.y() == other.y()
    def __ne__(self, other):
        return not self.__eq__(other)

    def squareDistanceTo(self, other):
        return (self.x() - other.x())**2 + (self.y() - other.y())**2

    @staticmethod
    def KDPointZero():
        return KDPoint(0, 0)

class KDRect:
    class __struct:
        def __init__(self, x, y, w, h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
    def __init__(self, x, y, w, h):
        self._struct = self.__struct(x, y, w, h)

    def __repr__(self):
        return "KDRect(x={0}, y={1}, w={2}, h={3})".format(self.x(), self.y(), self.width(), self.height())
    def __iter__(self):
        yield self.x()
        yield self.y()
        yield self.width()
        yield self.height()

    def struct(self):
        return self._struct

    def x(self):
        return self._struct.x
    def y(self):
        return self._struct.y
    def origin(self):
        return (self.x(), self.y())
    def width(self):
        return self._struct.w
    def height(self):
        return self._struct.h
    def size(self):
        return (self.width(), self.height())
    def top(self):
        return self.y()
    def right(self):
        return self.x() + self.width() - 1
    def bottom(self):
        return self.y() + self.height() - 1
    def left(self):
        return self.x()

    def topLeft(self):
        return (self.left(), self.top())
    def topRight(self):
        return (self.right(), self.top())
    def bottomLeft(self):   
        return (self.left(), self.bottom())
    def bottomRight(self):
        return (self.right(), self.bottom())
    def isValid(self):
        return self.width() > 0 and self.height() > 0

    def __eq__(self, other):
        return (self.x() == other.x() and self.y() == other.y() and
                self.width() == other.width() and self.height() == other.height())
    def __ne__(self, other):
        return not self.__eq__(other)

    def setOrigin(self, point):
        self._struct = self.__struct(point.x(), point.y(), self._struct.w, self._struct.h)
    def setSize(self, w, h):
        self._struct = self.__struct(self._struct.x, self._struct.y, w, h)

    def translatedBy(self, point):
        return KDRect(self.x() + point.x(), self.y() + point.y(), self.width(), self.height())
    def relativeTo(self, other):
        return KDRect(self.x() - other.x(), self.y() - other.y(), self.width(), self.height())
    def movedTo(self, point):
        return KDRect(point.x(), point.y(), self.width(), self.height())

    def intersects(self, other):
        return not (self.right() < other.left() or self.left() > other.right() or
                    self.bottom() < other.top() or self.top() > other.bottom())
    def intersectedWith(self, other):
        if not self.intersects(other):
            return KDRect(0, 0, 0, 0)
        intersectionLeft = max(self.left(), other.left())
        intersectionTop = max(self.top(), other.top())
        intersectionRight = min(self.right(), other.right())
        intersectionBottom = min(self.bottom(), other.bottom())
        return KDRect(intersectionLeft, intersectionTop, 
                      intersectionRight - intersectionLeft + 1, 
                      intersectionBottom - intersectionTop + 1)
    def unionedWith(self, other):
        unionLeft = min(self.left(), other.left())
        unionTop = min(self.top(), other.top())
        unionRight = max(self.right(), other.right())
        unionBottom = max(self.bottom(), other.bottom())
        return KDRect(unionLeft, unionTop, 
                      unionRight - unionLeft + 1, 
                      unionBottom - unionTop + 1)
    def differencedWith(self, other):
        if self.isEmpty() or other.isEmpty():
            return [self]
        if not self.intersects(other):
            return [self]
        intersection = self.intersectedWith(other)
        result = []
        if self.top() < intersection.top():
            result.append(KDRect(self.left(), self.top(), self.width(), intersection.top() - self.top()))
        if self.bottom() > intersection.bottom():
            result.append(KDRect(self.left(), intersection.bottom() + 1, self.width(), self.bottom() - intersection.bottom()))
        if self.left() < intersection.left():
            result.append(KDRect(self.left(), intersection.top(), intersection.left() - self.left(), intersection.height()))
        if self.right() > intersection.right():
            result.append(KDRect(intersection.right() + 1, intersection.top(), self.right() - intersection.right(), intersection.height()))
        return result

    def contains(self, point):
        return (self.left() <= point.x() <= self.right() and
                self.top() <= point.y() <= self.bottom())
    def containsRect(self, other):
        return (self.left() <= other.left() and self.right() >= other.right() and
                self.top() <= other.top() and self.bottom() >= other.bottom())
    def isEmpty(self):
        return self.width() <= 0 or self.height() <= 0
    @staticmethod
    def KDRectZero():
        return KDRect(0, 0, 0, 0)

class KDString:
    class __struct:
        def __init__(self, x, y, w, h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
    def __init__(self, string, point, color1="black", color2="white"): # FIXME: Remove color1 and color2 from the constructor, as they are not used in the struct.
        self.string = string
        self.string_old = ""
        self._struct = self.__struct(point.x(), point.y(), 0, 0)
        self._updateStruct()
        self.color1 = color1
        self.color2 = color2
    def __repr__(self):
        return "KDString(s={0}, point={1}, color1={2}, color2={3})".format(self.string, self.point, self.color1, self.color2)
    def __str__(self):
        return self.string
    def __iter__(self):
        return iter(self.string)
    def __len__(self):
        return len(self.string)

    def _updateStruct(self):
        if self.string == self.string_old:
            return
        self.string_old = self.string
        lines = self.string.split("\n")
        max_width = max(len(line) for line in lines) * 10
        height = len(lines) * 18
        self._struct = self.__struct(self._struct.x, self._struct.y, max_width, height)

    def struct(self):
        self._updateStruct()
        return self._struct

    def x(self):
        self._updateStruct()
        return self._struct.x
    def y(self):
        self._updateStruct()
        return self._struct.y
    def origin(self):
        return (self.x(), self.y())
    def width(self):
        self._updateStruct()
        return self._struct.w
    def height(self):
        self._updateStruct()
        return self._struct.h
    def size(self):
        return (self.width(), self.height())
    def top(self):
        return self.y()
    def right(self):
        return self.x() + self.width() - 1
    def bottom(self):
        return self.y() + self.height() - 1
    def left(self):
        return self.x()

    def topLeft(self):
        return (self.left(), self.top())
    def topRight(self):
        return (self.right(), self.top())
    def bottomLeft(self):   
        return (self.left(), self.bottom())
    def bottomRight(self):
        return (self.right(), self.bottom())
    def isValid(self):
        return self.width() > 0 and self.height() > 0

    def __eq__(self, other):
        return (self.x() == other.x() and self.y() == other.y() and
                self.width() == other.width() and self.height() == other.height())
    def __ne__(self, other):
        return not self.__eq__(other)

    def setOrigin(self, point):
        self._struct = self.__struct(point.x(), point.y(), self._struct.w, self._struct.h)

    def contains(self, point):
        return (self.left() <= point.x() <= self.right() and
                self.top() <= point.y() <= self.bottom())
    def containsRect(self, other):
        return (self.left() <= other.left() and self.right() >= other.right() and
                self.top() <= other.top() and self.bottom() >= other.bottom())
    def isEmpty(self):
        return self.width() <= 0 or self.height() <= 0

    def charpos(self, index):
        if index < 0 or index >= len(self.string):
            raise IndexError("Index out of range")
        lines = self.string.split("\n")
        current_index = 0
        for line_number, line in enumerate(lines):
            if current_index + len(line) > index:
                char_x = (index - current_index) * 10
                char_y = line_number * 18
                print(line_number, line, current_index, index, line[index - current_index])
                return KDRect(self.x() + char_x, self.y() + char_y, 10, 18)
            current_index += len(line)
        raise IndexError("Index out of range")

    def yieldcharrect(self):
        lines = self.string.split("\n")
        for line_number,line in enumerate(lines):
            yield "next", KDRect.KDRectZero()
            for char_index, char in enumerate(line):
                yield (char, KDRect(self.x() + char_index * 10, self.y() + line_number * 18, 10, 18))