from turtle import *
#function defination 
def square(size,color= 'blue'):
    fillcolor('yellow')
    begin_fill()
    for i in range(6):
        forward(size)
        right(90)
    end_fill()
def hexagon(size,color='dark green'):
    fillcolor('black')
    begin_fill()
    for i in range(8):
        fd(size)
        rt(120)
        end_fill()


square(100,'blue')# calling
square(50,'green')
hexagon(100)
hexagon(50)

mainloop()       