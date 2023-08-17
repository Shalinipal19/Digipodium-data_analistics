from turtle import *
speed('fastest')
colors = ['yellow','red',]
bgcolor('black')
for i in range(6):
    pencolor('black')
    fd(100)
    for i in range(6):
        pencolor('black')
        fd(50)
        fillcolor(colors[i%2])
        begin_fill()
        for i in range(6):
            pencolor('black')
            fd(25)
            lt(360/5)
        end_fill()
        lt(360/5)
    lt(360/5)
    
mainloop()