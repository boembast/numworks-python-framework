from kdex import KDRect
#I'm not sure whether to keep these yet, so I'm just putting them here for now.

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