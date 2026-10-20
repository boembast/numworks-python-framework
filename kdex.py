# Size over readability version
class KDPoint:
    _STRUCT_X = 0
    _STRUCT_Y = 1
    def __init__(self, x, y, color1=""):
        self.__struct, self.color1 = [x, y], color1
    def __repr__(self):
        return "KDPoint(x={0}, y={1})".format(self.x(), self.y())
    def __iter__(self):
        yield self.x()
        yield self.y()
    struct = lambda self: self.__struct
    x= lambda self: self.__struct[self._STRUCT_X]
    y= lambda self: self.__struct[self._STRUCT_Y]
    translatedBy = lambda self, point: KDPoint(self.x() + point.x(), self.y() + point.y())
    relativeTo = lambda self, other: self.translatedBy(other.opposite())
    opposite = lambda self: KDPoint(-self.x(), -self.y())
    def __eq__(self, other):
        return self.x() == other.x() and self.y() == other.y()
    def __ne__(self, other):
        return not self.__eq__(other)
    squareDistanceTo = lambda self, other: (self.x() - other.x())**2 + (self.y() - other.y())**2
    @staticmethod
    def KDPointZero():
        return KDPoint(0, 0)
class KDRect:
    _STRUCT_X = 0
    _STRUCT_Y = 1
    _STRUCT_W = 2
    _STRUCT_H = 3
    def __init__(self, x, y, w, h,color1=""):
        self.__struct, self.color1 = [x, y, w, h], color1
    def __repr__(self):
        return "KDRect(x={0}, y={1}, w={2}, h={3})".format(self.x(), self.y(), self.width(), self.height())
    def __iter__(self):
        yield self.x()
        yield self.y()
        yield self.width()
        yield self.height()
    struct = lambda self: self.__struct
    x = lambda self: self.__struct[self._STRUCT_X]
    y = lambda self: self.__struct[self._STRUCT_Y]
    origin = lambda self: (self.x(), self.y())
    width = lambda self: self.__struct[self._STRUCT_W]
    height = lambda self: self.__struct[self._STRUCT_H]
    size = lambda self: (self.width(), self.height())
    top = lambda self: self.y()
    right = lambda self: self.x() + self.width() - 1
    bottom = lambda self: self.y() + self.height() - 1
    left = lambda self: self.x()
    topleft = lambda self: (self.left(), self.top())
    topRight = lambda self: (self.right(), self.top())
    bottomLeft = lambda self: (self.left(), self.bottom())
    bottomRight = lambda self: (self.right(), self.bottom())
    isValid = lambda self: self.width() > 0 and self.height() > 0
    def __eq__(self, other):
        return (self.struct() == other.struct())
    def __ne__(self, other):
        return not self.__eq__(other)
    def setOrigin(self, point):
        self.__struct[:2] = [point.x(), point.y()]
    def setSize(self, w, h):
        self.__struct[2:] = [w, h]
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
        return KDRect((intersectionLeft:=max(self.left(), other.left())), 
                      (intersectionTop:=max(self.top(), other.top())), 
                      min(self.right(), other.right()) - intersectionLeft + 1, 
                      min(self.bottom(), other.bottom()) - intersectionTop + 1
                      ) if self.intersects(other) else KDRect(0, 0, 0, 0)
    def unionedWith(self, other):
        return KDRect((unionLeft:=min(self.left(), other.left())), 
                      (unionTop:=min(self.top(), other.top())), 
                      max(self.right(), other.right()) - unionLeft + 1, 
                      max(self.bottom(), other.bottom()) - unionTop + 1)
    def differencedWith(self, other):
        if self.isEmpty() or other.isEmpty() or not self.intersects(other):
            return [self]
        intersection, result = self.intersectedWith(other), []
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
    @staticmethod
    def fromtuple(tuple):
        return KDRect(tuple[1], tuple[2], tuple[3], tuple[4])

class KDString:
    _STRUCT_X = 0
    _STRUCT_Y = 1
    _STRUCT_W = 2
    _STRUCT_H = 3
    def __init__(self, string, point, color1="black", color2="white"): # FIXME: Remove color1 and color2 from the constructor, as they are not used in the struct.
        self.string = string
        self.string_old = ""
        self.__struct = [point.x(), point.y(), 0, 0]
        self._updateStruct()
        self.color1 = color1
        self.color2 = color2
    def __repr__(self):
        return "KDString(s={0}, point={1}, color1={2}, color2={3})".format(self.string, self.origin(), self.color1, self.color2)
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
        self.__struct[2:] = max(len(line) for line in lines) * 10, len(lines) * 18
    def struct(self):
        self._updateStruct()
        return self.__struct
    x = lambda self: self.__struct[self._STRUCT_X]
    y = lambda self: self.__struct[self._STRUCT_Y]
    origin = lambda self: (self.x(), self.y())
    def width(self):
        self._updateStruct()
        return self.__struct[self._STRUCT_W]
    def height(self):
        self._updateStruct()
        return self.__struct[self._STRUCT_H]
    size = lambda self: (self.width(), self.height())
    top = lambda self: self.y()
    right = lambda self: self.x() + self.width() - 1
    bottom = lambda self: self.y() + self.height() - 1
    left = lambda self: self.x()
    topleft = lambda self: (self.left(), self.top())
    topRight = lambda self: (self.right(), self.top())
    bottomLeft = lambda self: (self.left(), self.bottom())
    bottomRight = lambda self: (self.right(), self.bottom())
    isValid = lambda self: self.width() > 0 and self.height() > 0
    def __eq__(self, other):
        return (self.x() == other.x() and self.y() == other.y() and
                self.width() == other.width() and self.height() == other.height())
    def __ne__(self, other):
        return not self.__eq__(other)
    def setOrigin(self, point):
        self.__struct[:2] = [point.x(), point.y()]
    def contains(self, point):
        return (self.left() <= point.x() <= self.right() and
                self.top() <= point.y() <= self.bottom())
    def containsRect(self, other):
        return (self.left() <= other.left() and self.right() >= other.right() and
                self.top() <= other.top() and self.bottom() >= other.bottom())
    def isEmpty(self):
        return self.width() <= 0 or self.height() <= 0
    def charpos(self, index): # TODO: Is this necessary? Could be removed
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
        for line_number,line in enumerate(self.string.split("\n")):
            yield "next", KDRect.KDRectZero()
            for char_index, char in enumerate(line):
                yield (char, KDRect(self.x() + char_index * 10, self.y() + line_number * 18, 10, 18))

    @staticmethod
    def fromtuple(tuple):
        return KDString(tuple[1], KDPoint(tuple[2], tuple[3]), tuple[4], tuple[5])