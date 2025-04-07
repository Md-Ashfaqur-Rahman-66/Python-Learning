# Simple Pong in Python 3 for begineers
# By Luban
# Part 1: Getting Started


import turtle
import winsound                 # Importing sound Module

wn = turtle.Screen()
wn.title("Pong Game by Luban")
wn.bgcolor("Black")
wn.setup(width=800, height= 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()         # 'turtle'= module, 'Turtle'= class
paddle_a.speed(0)
paddle_a.shape("square")           # default shape = 25 x 25 pixels
paddle_a.color("white")            # Color of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # Paddle width = 20, Height = 100
paddle_a.penup()                   # Remove the line
paddle_a.goto(-350, 0)             # Starting Position of the paddle (midpoint= center)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")                # default radius = 20+20 pixels
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .18                       # Move the ball 2 pixels right
ball.dy = .18                      # Move the ball 2 pixels up

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))  # Printing Score

# Function
def paddle_a_up():          # function for moving the paddle up
    y = paddle_a.ycor()     # Returns Y coordinate of the paddle
    y+= 20                  # Adding 20 pixels to the y coodinate
    paddle_a.sety(y)        # Setting new coordinate

def paddle_a_down():        # function for moving the paddle down
    y = paddle_a.ycor()     # Returns Y corordinate of the paddle
    y -= 20                 # substracting 20 pixels from the y coodinate
    paddle_a.sety(y)        # Setting new coordinate

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")          # assiging 'w' buttion for calling the 'paddle_a_up' function
wn.onkeypress(paddle_a_down,"s")        # assiging 's' buttion for calling the 'paddle_a_down' function
wn.onkeypress(paddle_b_up,"Up")         # assiging 'w' buttion for calling the 'paddle_a_up' function
wn.onkeypress(paddle_b_down,"Down")     # assiging 's' buttion for calling the 'paddle_a_down' function

# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor()>290:             # (600/2)-(20/2)=290; 600 = height of window, 20= Radius of ball
        ball.sety(290)              # Setting Y boundary
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)    # using 'bounce.wav' file in 'PlaySound' function of 'winsound' module; 'winsound.SND_ASYNC' = playing sound in only BG but not stoping the loop

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor()>390:             # (800/2)-(20/2) =390
        ball.goto(0, 0)             # setting X boundary
        ball.dx *= -1
        score_a += 1                # Updating Score
        pen.clear()                 # Clear the previous score
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))  # Printing new Score
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor()<-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))  # Printing new Score
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()>paddle_b.ycor()-50 and ball.ycor()<paddle_b.ycor()+50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()>paddle_a.ycor()-50 and ball.ycor()<paddle_a.ycor()+50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)



























