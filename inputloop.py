import kandinsky as kd
from time import sleep
import ion

ALL_KEYS = [x for x in range(0,53) if x not in (7,9,10,11,35,41,47)] # Constant list of all keys to improve space and time efficiency.

def inputloop():
    while True:
        for i in ALL_KEYS:
            if ion.keydown(i):
                return i

print(inputloop())