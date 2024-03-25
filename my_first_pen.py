from turtle import Turtle

pen = Turtle()

screen = pen.getscreen()
screen.bgcolor('#B60149')

steps = 100 
iterations = 30 
pen.speed('fastest')
angle = 90 

pen.pensize(5)
pen.penup()
pen.setpos(-50,-50)
pen.pendown()

my_colours = ['red', 'yellow', 'blue', 'green', 'purple', 'orange', 'black']


for i in range(iterations): 
    pen.color(my_colours[i % len(my_colours)])
    for x in range(4): 
        pen.fd(steps)
        pen.left(angle)
        steps += 5 


pen.screen.mainloop()
