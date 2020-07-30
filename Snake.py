import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Python game by @nicecop123")
wn.bgcolor('#252621')
wn.setup(width=600, height= 600)
wn.tracer(0)

#Snake head:
phead = turtle.Turtle()
phead.speed(0)
phead.shape("square")
phead.color("#eaeae8")
phead.penup()
phead.goto(0,0)
phead.direction = "stop"

#snake food:
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('red')
food.penup()
food.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-260,-260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#Functions:
def death():
    time.sleep(1)
    phead.goto(0, 0)
    phead.direction = "stop"
    # hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    # clear the segments
    segments.clear()
    xrange = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100,
              120, 140, 160, 180, 200, 220, 240, 260, 280]
    yrange = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100,
              120, 140, 160, 180, 200, 220, 240, 260, 280]
    x = random.choice(xrange)
    y = random.choice(yrange)
    food.goto(x, y)
    # hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    # clear the segments
    segments.clear()
    #writing the score
    score = 0
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score, align="center"), font=("Courier", 24, "normal"))
    delay = 0.1
def go_up():
    if phead.direction != "down":
        phead.direction = "up"
def go_down():
    if phead.direction != "up":
        phead.direction = "down"
def go_right():
    if phead.direction != "left":
        phead.direction = "right"
def go_left():
    if phead.direction != "right":
        phead.direction = "left"

def move():
    if phead.direction == "up":
        y = phead.ycor()
        phead.sety(y+20)
    if phead.direction == "down":
        y = phead.ycor()
        phead.sety(y-20)
    if phead.direction == "right":
        x = phead.xcor()
        phead.setx(x+20)
    if phead.direction == "left":
        x = phead.xcor()
        phead.setx(x-20)

def easy():
    delay = 0.2
    death()

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")
wn.onkeypress(easy, "e")


#Main loop:
while True:
    wn.update()

    #checking for collision with borders
    if phead.xcor()>290 or phead.xcor()<-290 or phead.ycor()>290 or phead.ycor()<-290:
        death()

    #check for food
    if phead.distance(food) < 20:
        #common varaible
        xrange = [-280, -260, -240, -220, -200, -180, -160, -140, -120,-100, -80,-60,-40,-20,0,20,40,60,80,100,120,140,160,180,200,220,240,260,280]
        yrange = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100,120, 140, 160, 180, 200, 220, 240, 260, 280]
        x = random.choice(xrange)
        y = random.choice(yrange)
        food.goto(x, y)
        #add the segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('#eaeae8')
        new_segment.penup()
        segments.append(new_segment)

        #shortening the delay
        delay -= 0.001

        #increasing the score
        score = score + 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score, align = "center"),font=("Courier", 24, "normal"))

        xrange = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80,
                  100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
        yrange = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80,
                  100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
        x = random.choice(xrange)
        y = random.choice(yrange)
        food.goto(x, y)

    #making the body move
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    #making the second head move
    if len(segments) > 0:
        x = phead.xcor()
        y = phead.ycor()
        segments[0].goto(x, y)

    move()

    #Check for head collision with body segments
    for segment in segments:
        if segment.distance(phead) < 20:
            death()

    time.sleep(delay)
wn.mainloop()