from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y0
    B = -1 * (x1 - x0)
    delX = x1 - x0 + 0.0
    delY = y1 - y0 + 0.0
    slope = delY / delX
    if (slope < 1 and slope > 0) :
        # OCTANT 1
        d = 2 * A + B
        while x <= x1:
            plot(screen, color, x,y)
            if d > 0:
                y = y + 1
                d = d + 2 * B
            x = x + 1
            d = d + 2 * A
    elif (slope > 1) :
        # OCTANT 2
        d = A + 2 * B
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                x = x + 1
                d = d + 2 * A
            y = y + 1
            d = d + 2 * B
