from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#octant 1
draw_line(250, 250, 400, 300, screen, color)
#octant 2
draw_line(250, 250, 300, 400, screen, color)
#octant 3
draw_line(250, 250, 200, 400, screen, color)
#octant 4
draw_line(250, 250, 100, 300, screen, color)
#octant 5
draw_line(250, 250, 100, 200, screen, color)
#octant 6
draw_line(250, 250, 200, 100, screen, color)
#octant 7
draw_line(250, 250, 300, 100, screen, color)
#octant 8
draw_line(250, 250, 400, 200, screen, color)
#slope = 0
draw_line(250, 250, 500, 250, screen, color)
draw_line(250, 250, 0, 250, screen, color)
#slope = undefined
draw_line(250, 250, 250, 500, screen, color)
draw_line(250, 250, 250, 0, screen, color)
#slope = 1
draw_line(250, 250, 500, 500, screen, color)
draw_line(250, 250, 0, 0, screen, color)
#slope = -1
draw_line(250, 250, 0, 500, screen, color)
draw_line(250, 250, 500, 0, screen, color)

#for i in range(200) :
#    plot(screen, color, i, i)

display(screen)
save_extension(screen, 'img.png')
