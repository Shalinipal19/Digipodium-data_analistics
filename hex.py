from turtle import *
#hexagon
speed('fastest')
pencolor('black')
pensize(2)
for i in range(80):
    fd(100-i)
    rt(60)
    circle(80,270)
    dot(10,'yellow')
mainloop()    