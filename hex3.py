from turtle import *
#hexagon
speed('fastest')
pencolor('purple')
pensize(3)
for i in range(100):
    fd(10-i)
    rt(80)
    circle(100,360)
    dot(12,'red')
mainloop()    