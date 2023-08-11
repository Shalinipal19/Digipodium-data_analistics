from turtle import *
speed('fastest')
bgcolor('white')
colors = ['red','black','yellow','green','blue']

i = 0
while True:
    pencolor(colors[i%4])
    fd(10+i)
    lt(200)

    i += 1
mainloop()