#Import Statements
import turtle
import random
import time
import sys

#Global Variables
screen = turtle.Screen()
screen.screensize(600,400)
#screen.tracer(0)
globalScreenSize = screen.screensize()
globalWidth = globalScreenSize[0]
globalHeight = globalScreenSize[1]
globalPlaySize = (0.9 * globalWidth, 0.9 * globalHeight)
globalBallSize = 20.0
screen.colormode(255)

screen.title("C4C Y1A Breakout")
ballTurtle = turtle.Turtle()
#ballTurtle.hideturtle()
gameSpeed = 1

#Method that returns the location of the left side of the ball as a float
leftOfBall = lambda: (ballTurtle.xcor() - 0.5 * globalBallSize, ballTurtle.ycor())

#Method that returns the location of the right side of the ball as a float
rightOfBall = lambda: (ballTurtle.xcor() + 0.5 * globalBallSize, ballTurtle.ycor())

#Method that returns the location of the top side of the ball as a float
topOfBall = lambda: (ballTurtle.xcor(), ballTurtle.ycor() + 0.5 * globalBallSize)

#Method that returns the location of the bottom side of the ball as a float
bottomOfBall = lambda: (ballTurtle.xcor(), ballTurtle.ycor() - 0.5 * globalBallSize)

#Method that draws a border around the screen. Does not return anything
def drawOuterBox():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    drawer.penup()
    drawer.goto(-globalPlaySize[0] // 2, -globalPlaySize[1] // 2)
    drawer.pendown()
    for i in range(4):
        drawer.forward(globalPlaySize[i%2])
        drawer.left(90)
    turtle.done()
    #screen.update()

#Method that draws the ball to the screen. Does not return anything
def drawBall():
    #screen.clear()
    ballTurtle.pendown()
    # ballTurtle.shape("circle")
    # raise ValueError
    ballTurtle.forward(10)
    #screen.update()

drawOuterBox()
drawBall()
screen.exitonclick()

'''
#Method that returns the location of the left side of the wall as a float.
#Hint: Use globalWidth or globalHeight.
def leftOfWall():
    #Your code here

#Method that returns the location of the right side of the wall as a float.
def rightOfWall():
    #Your code here

#Method that returns the location of the top side of the wall as a float.
def topOfWall():
    #Your code here

#Method that returns the location of the bottom side of the wall as a float.
def bottomOfWall():
    #Your code here

#Method that moves the ballTurtle at the gameSpeed
def moveBall():
    #Your code here

#Method that checks the collisions between the ball and the wall. Does not return anything
#Hint #1: use the methods you wrote like leftOfBall() and leftOfWall()
def checkBallWallCollision():
    #Your code here

drawOuterBox()
drawBall()
while True:
    checkBallWallCollision()
    moveBall()
    screen.update()
    turtle.done()
    turtle.exit()
'''
