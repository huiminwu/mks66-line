from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0, 0, 250, 100, screen, color)
draw_line(0, 0, 10, 300, screen, color)

#for i in range(200) :
#    plot(screen, color, i, i)

display(screen)
save_extension(screen, 'img.png')
