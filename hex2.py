from turtle import *
#hexagon
speed('fastest')
pencolor('black')
pensize(2)
for i in range(80):
    fd(10-i)
    rt(60)
    circle(80,360)
    dot(10,'yellow')
mainloop()    