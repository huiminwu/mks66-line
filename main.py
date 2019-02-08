from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#octant 1
draw_line(250, 250, 500, 350, screen, color)
#octant 2
draw_line(250, 250, 350, 500, screen, color)
#slope = 0
draw_line(250, 250, 250, 250, screen, color)
#slope = 1
draw_line(250, 250, 500, 500, screen, color)

#for i in range(200) :
#    plot(screen, color, i, i)

display(screen)
save_extension(screen, 'img.png')
