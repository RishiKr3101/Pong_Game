"""Main executable for the game."""

import turtle

wn = turtle.Screen()  # Create and setup Main Window
wn.title("Pong by @Rishi")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

pad_a = turtle.Turtle()  # Create and setup Player A's paddle
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

pad_b = turtle.Turtle()  # Create and setup Player B's paddle
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

ball = turtle.Turtle()  # Create and setup the ball
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

a = 0  # Player A score
b = 0  # Player B score

p = turtle.Turtle()  # Create turtle for drawing score text
p.speed(0)
p.color("white")
p.penup()
p.goto(0, 260)
p.hideturtle()
p.write("Player A : {}     Player B : {}".format(a, b), align="center", font=("Courier", 24, "normal"))


def pad_a_up():
    """Move paddle A up."""
    y = pad_a.ycor()
    y += 30
    pad_a.sety(y)


def pad_b_up():
    """Move paddle B up."""
    y = pad_b.ycor()
    y += 30
    pad_b.sety(y)


def pad_a_down():
    """Move paddle A down."""
    y = pad_a.ycor()
    y -= 30
    pad_a.sety(y)


def pad_b_down():
    """Move paddle B down."""
    y = pad_b.ycor()
    y -= 30
    pad_b.sety(y)


wn.listen()  # Bind keys for moving paddles
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

while True:  # Main update loop
    wn.update()

    ball.setx(ball.xcor()+ball.dx)  # Move ball
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(0)
        ball.sety(0)
        ball.dy *= -1
        ball.dx *= -1

        a = a+1
        p.clear()
        p.write("Player A : {}     Player B : {}".format(a, b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.sety(0)
        ball.dy *= -1
        ball.dx *= -1

        b = b + 1
        p.clear()
        p.write("Player A : {}     Player B : {}".format(a, b), align="center", font=("Courier", 24, "normal"))

    if (340 < ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 50) and (ball.ycor() > pad_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (ball.ycor() < pad_a.ycor() + 50) and (ball.ycor() > pad_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
