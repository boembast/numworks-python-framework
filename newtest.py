from kdexpanded import *

mystring = KDString("Hello World, but also\nI gave birth today\nAnd life is good",KDPoint(20,20))
collider = KDRect(50,0,50,50)

newlines = [[]]
line = 0
col = 0
curline = []
for char in mystring:
    #print(char, line, col,curline)
    if char == "\n":
        line += 1
        col = 0
        newlines[-1].append("".join(curline)) # Add the current line to the last line in newlines
        curline.clear() # Clear the current line for the next characters
        newlines.append([])
        continue
    #print(char,"at",mystring.x() + col * 10, mystring.y() + line * 18, 10, 18)
    if collider.containsRect(KDRect(mystring.x() + col * 10, mystring.y() + line * 18, 10, 18)):
        #print("Does overlap completely")
        if curline: # There were previous characters that did not collide
            newlines[-1].append("".join(curline)) # So add those characters to the last line
            curline.clear() # Clear the current line for the next characters
            newlines[-1].append(1) # And append a 1 to indicate there was one cell collision
        elif newlines[-1] and type(newlines[-1][-1]) == int: # There were no previous characters that did not collide but a collision was already detected in the last line
            newlines[-1][-1] += 1 # So we increase the last number to indicate another cell collision
        elif not newlines[-1]: # There were no previous characters that did not collide and no collision was detected in the last line
            newlines[-1].append(1) # So we append a 1 to indicate there was one cell collision
    else:
        #print("Does not overlap completely")
        curline.append(char)
    col += 1
newlines[-1].append("".join(curline)) # Add the last line to newlines
curline.clear() # Clear the current line for the next characters
print(newlines)

import kandinsky as kd

def print_newlines(linelist, x, y, color1="black", color2="white"):
    base_x = x
    base_y = y
    for line_number, line in enumerate(linelist):
        base_x = x
        for item in line:
            if type(item) == str:
                kd.draw_string(item, base_x, base_y + line_number * 18, color1, color2)
                base_x += len(item) * 10
            elif type(item) == int:
                base_x += item * 10

print_newlines(newlines, 20, 20, "black", "white")