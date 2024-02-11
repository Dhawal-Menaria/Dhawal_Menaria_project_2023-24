import turtle
import random
import time
import sys  

def Dscreensaver():

    def screensaver(speed):
        turtle.clear()
        turtle.color("white")
        turtle.write("Dhawal Menaria", font=("Arial", 24, "bold"))
        time.sleep(1 / speed)  


    def move_turtle():
        x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
        y = random.randint(-turtle.window_height() // 2, turtle.window_height() // 2)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()


    screen = turtle.Screen()
    screen.setup(width=0, height=0)  
    screen.bgcolor("black")
    screen.tracer(0)  
    screen.delay(0)   
    screen.title("Dhawal's Screen Saver")

    screen.setup(width=1.0, height=1.0)


    turtle.speed(0)  
    turtle.hideturtle()


    try:
        while True:
            move_turtle()
            screensaver(2)  
            screen.update()  
            turtle.clear()   

    except turtle.Terminator:
        pass
