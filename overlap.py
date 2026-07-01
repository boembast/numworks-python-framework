def overlaps(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return (
        bx + bw > ax and
        ax + aw > bx and 
        by + bh > ay and
        ay + ah > by
        )

lowerrect = (45,10,4,20)
higherrect = (20,0,30,40)

print(overlaps(higherrect, lowerrect))
print(overlaps(lowerrect, higherrect))
