import kandinsky as kd
from time import sleep
import ion

def inputloop():
    while True:
        for i in [x for x in range(0,53) if x not in (7,9,10,11,35,41,47)]:
            if ion.keydown(i):
                return i

print(inputloop())