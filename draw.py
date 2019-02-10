from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y0
    B = -1 * (x1 - x0)
    delX = x1 - x0 + 0.0
    delY = y1 - y0 + 0.0
    if (delX == 0):
        print("line is vertical")
        #from bottom to top
        while y < y1:
            plot(screen, color, x, y)
            y = y + 1
        #from top to bottom
        while y > y1:
            plot(screen, color, x, y)
            y = y - 1
    elif (delY == 0):
        print("line is horizantal")
        #for left to right
        while x < x1:
            plot(screen, color, x, y)
            x = x + 1
        #for right to left
        while x > x1:
            plot(screen, color, x, y)
            x = x - 1
    else:
        slope = delY / delX
        if (delY > 0): #if in quadrant 1 and 2
            if (delX > 0):
                #quadrant 1
                if (slope < 1):
                    #octant 1
                    print("octant 1 line")
                    d = 2 * A + B
                    while x <= x1:
                        plot(screen, color, x,y)
                        if d > 0:
                            y = y + 1
                            d = d + 2 * B
                        x = x + 1
                        d = d + 2 * A
                else:
                    #octant 2
                    print("octant 2 line")
                    d = A + 2 * B
                    while y <= y1:
                        plot(screen, color, x, y)
                        if d < 0:
                            x = x + 1
                            d = d + 2 * A
                        y = y + 1
                        d = d + 2 * B

            else:
                #quadrant 2
                if (slope < -1):
                    #octant 3
                    print("octant 3 line")
                    d = 2 * B - A
                    while y <= y1:
                        plot(screen, color, x, y)
                        if d > 0:
                            x = x - 1
                            d = d - 2 * A
                        y = y + 1
                        d = d + 2 * B

                else:
                    #octant 4
                    print("octant 4 line")
                    d = B - 2 * A
                    while x >= x1:
                        plot(screen, color, x, y)
                        if d < 0:
                            y = y + 1
                            d = d + 2 * B
                        x = x - 1
                        d = d - 2 * A

        else:  #if in quadrant 3 and 4
            if (delX < 0):
                #quadrant 3
                if (slope < 1) :
                    #octant 5
                    print("octant 5 line")
                    d = -2 * A - B
                    while x >= x1:
                        plot(screen, color, x, y)
                        if d > 0:
                            y = y - 1
                            d = d - 2 * B
                        x = x - 1
                        d = d - 2 * A
                else:
                    #octant 6
                    print("octant 6 line")
                    d = -2 * B - A
                    while y >= y1:
                        plot(screen, color, x, y)
                        if d < 0:
                            x = x - 1
                            d = d - 2 * A
                        y = y - 1
                        d = d - 2 * B
            else:
                #quadrant 4
                if (slope < -1 ) :
                    #octant 7
                    print("octant 7 line")
                    d = A - 2 * B
                    while y >= y1:
                        plot(screen, color, x,y)
                        if d > 0:
                            x = x + 1
                            d = d + 2 * A
                        y = y - 1
                        d = d - 2 * B
                else:
                    #octant 8
                    print("octant 8 line")
                    d = 2 * A - B
                    while x <= x1:
                        plot(screen, color, x,y)
                        if d < 0:
                            y = y - 1
                            d = d - 2 * B
                        x = x + 1
                        d = d + 2 * A
