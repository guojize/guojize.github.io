#Import Statements
import turtle
import random
import time
import sys

#Global Variables
screen = turtle.Screen()
screen.tracer(0)
screen.title('Breakout')
screen.screensize(600, 400)
screen.colormode(255)
screen.tracer(0)
globalScreenSize = screen.screensize()
globalBallSize = 10.0
turtle.mode('logo')
ballTurtle = turtle.Turtle()
ballTurtle.shape('circle')
ballTurtle.shapesize(1, 1)
ballTurtle.penup()
ballDirection = random.randint(-60, 60)
ballTurtle.left(ballDirection)
gameSpeed = 0.15
randomRotate = 10

globalSideGapRatio = 0.025
globalWidthGap = globalScreenSize[0] * globalSideGapRatio
globalHeightGap = globalWidthGap * 2.0
widthBrick = ((globalScreenSize[0] - (2 * globalWidthGap)) / 10)
heightBrick = 20

blocks = []
numBricksRow = 10
numRows = 4
paddleSize = (60, 10)
moveDistance = 20
paddleTurtle = turtle.Turtle()
paddleTurtle.penup()
paddleTurtle.goto((0, -200))
paddleTurtle.right(90)
paddleTurtle.shape('square')
paddleTurtle.shapesize(paddleSize[1] / 20, paddleSize[0] / 20)

#Helper Functions
#Method that returns the location of the left side of the ball as a float
leftOfBall = lambda: ballTurtle.xcor() - 10

#Method that returns the location of the right side of the ball as a float
rightOfBall = lambda: ballTurtle.xcor() + 10

#Method that returns the location of the top side of the ball as a float
topOfBall = lambda: ballTurtle.ycor() + 10

#Method that returns the location of the bottom side of the ball as a float
bottomOfBall = lambda: ballTurtle.ycor() - 10

#Method that returns the location of the left side of the paddle as a float
leftOfPaddle = lambda: paddleTurtle.xcor() - paddleSize[0] // 2

#Method that returns the location of the right side of the paddle as a float
rightOfPaddle = lambda: paddleTurtle.xcor() + paddleSize[0] // 2

#Method that returns the location of the top side of the paddle as a float
topOfPaddle = lambda: paddleTurtle.ycor() + paddleSize[1] // 2

#Method that returns the location of the bottom side of the paddle as a float
bottomOfPaddle = lambda: paddleTurtle.ycor() - paddleSize[1] // 2

#Method that moves the ballTurtle at the gameSpeed
def moveBall():
    ballTurtle.forward(gameSpeed)

'''
#Method that returns the location of the X axis center of the paddle as a float
centerOfPaddleX = lambda: paddleTurtle.xcor()
#Method that returns the location of the Y axis center of the paddle as a float
centerOfPaddleY = lambda: paddleTurtle.ycor()

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

#Method that draws a border around the screen. Does not return anything
def drawOuterBox():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.pensize(3)
    drawer.penup()
    drawer.goto(globalScreenSize[0] // 2, -globalScreenSize[1] // 2)
    drawer.pendown()
    for i in range(3):
        drawer.forward(globalScreenSize[(i + 1) % 2])
        drawer.left(90)
    drawer.left(90)

#Method that moves the paddleTurtle left.
def pressLeftKey():
    paddleTurtle.backward(moveDistance)
    if leftOfPaddle() <= -globalScreenSize[0] // 2:
        paddleTurtle.forward(moveDistance)

#Method that moves the paddleTurtle right.
def pressRightKey():
    paddleTurtle.forward(moveDistance)
    if rightOfPaddle() >= globalScreenSize[0] // 2:
        paddleTurtle.backward(moveDistance)

out = {'w': False, 'a': False, 'd': False}

def checkBallCollision():
    w,a,s,d = globalScreenSize[1] // 2, -globalScreenSize[0] // 2, -globalScreenSize[1] // 2, globalScreenSize[0] // 2
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

    if bottomOfPaddle() <= bottomOfBall() <= topOfPaddle() and leftOfPaddle() <= rightOfBall() and leftOfBall() <= rightOfPaddle():
        walls.append('s')

    if not out['d'] and rightOfBall() >= d:
        walls.append('d')
        out['d'] = True
    elif out['d'] and rightOfBall() < d:
        out['d'] = False

    return walls

eps = lambda: random.random() * (2 * randomRotate) - randomRotate

def collide():
    walls = checkBallCollision()
    global ballDirection
    if len(walls) == 1:
        if walls[0] in ('w','s'):
            ballTurtle.left(180 - 2 * ballDirection + eps())
            ballDirection = 180 - ballDirection
        else:
            ballTurtle.left(-2 * ballDirection + eps())
            ballDirection = -ballDirection
    elif len(walls) == 2:
        ballTurtle.left(180 + eps())

drawOuterBox()
screen.onkey(pressLeftKey, "Left")
screen.onkey(pressRightKey, "Right")
screen.listen()
screen.update()
while True:
    moveBall()
    collide()
    screen.update()
turtle.done()
turtle.exit()
