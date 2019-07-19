#Import Statements
import turtle
import random
import time
import sys

#Global Variables
screen = turtle.Screen()
screen.title('C4C Y1A Breakout')
screen.screensize(600,400)
screen.colormode(255)
screen.tracer(0)
globalScreenSize = screen.screensize()
globalWidth = globalScreenSize[0]
globalHeight = globalScreenSize[1]
globalPlaySize = (0.9 * globalWidth, 0.9 * globalHeight)
globalBallSize = 10.0
turtle.mode('logo')
ballTurtle = turtle.Turtle()
ballTurtle.penup()
ballDirection = random.randint(-90,90)
ballTurtle.left(ballDirection)
gameSpeed = 1 / 4
randomRotate = 5

#Method that returns the location of the left side of the ball as a float
leftOfBall = lambda: ballTurtle.xcor() - 5

#Method that returns the location of the right side of the ball as a float
rightOfBall = lambda: ballTurtle.xcor() + 5

#Method that returns the location of the top side of the ball as a float
topOfBall = lambda: ballTurtle.ycor() + 5

#Method that returns the location of the bottom side of the ball as a float
bottomOfBall = lambda: ballTurtle.ycor() - 5

#Method that draws a border around the screen. Does not return anything
def drawOuterBox():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.pensize(3)
    drawer.speed(0)
    drawer.penup()
    drawer.goto(globalPlaySize[0] // 2 + 22.5, -globalPlaySize[1] // 2 - 22.5)
    drawer.pendown()
    for i in range(4):
        drawer.forward(globalPlaySize[(i + 1) % 2] + 61)
        drawer.left(90)

#Method that draws the ball to the screen. Does not return anything
def drawBall():
    ballTurtle.shape("circle")
    ballTurtle.shapesize(1,1)

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
'''

#Method that moves the ballTurtle at the gameSpeed
def moveBall():
    ballTurtle.forward(gameSpeed)

#Method that checks the collisions between the ball and the wall. Does not return anything
#Hint #1: use the methods you wrote like leftOfBall() and leftOfWall()
out = {'w': False, 'a': False, 's': False, 'd': False}

def checkBallWallCollision():
    w,a,s,d = globalHeight // 2,-globalWidth // 2,-globalHeight // 2,globalWidth // 2
    walls = []
    if not out['w'] and topOfBall() >= w:
        walls.append('w')
        out['w'] = True
    elif out['w'] and topOfBall() < w:
        out['w'] = False

    if not out['a'] and leftOfBall() <= a:
        walls.append('a')
        out['a'] = True
    elif out['a'] and leftOfBall() > a:
        out['a'] = False

    if not out['s'] and bottomOfBall() <= s:
        walls.append('s')
        out['s'] = True
    elif out['s'] and bottomOfBall() > s:
        out['s'] = False

    if not out['d'] and rightOfBall() >= d:
        walls.append('d')
        out['d'] = True
    elif out['d'] and rightOfBall() < d:
        out['d'] = False

    if walls:
        print('collides',walls)
    return walls

eps = lambda: random.random() * (2 * randomRotate) - randomRotate

def collide():
    walls = checkBallWallCollision()
    global ballDirection
    if len(walls) == 1:
        if walls[0] in ('w','s'):
            ballTurtle.left(180 - 2 * ballDirection + eps())
            ballDirection = 180 - ballDirection
        else:
            ballTurtle.left(-2 * ballDirection)
            ballDirection = -ballDirection
    elif len(walls) == 2:
        ballTurtle.left(180 + eps())

drawOuterBox()
drawBall()
row = 0
while True:
    collide()
    moveBall()
    screen.update()
