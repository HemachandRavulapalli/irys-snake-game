import turtle
import time
import random


win = turtle.Screen()
win.title("Snake Game - Irys Style")
win.bgcolor("#0a0f1a")
win.setup(width=600, height=600)
win.tracer(0)


shapes = [
    "Up", "Down", "Left", "Right",
    "Horizontal_", "Vertical",
    "Top_Right", "Bottom_Left", "Left_Top", "Right_Bottom_",
    "food_resized"
]
for shape in shapes:
    win.register_shape(f"media/{shape}.gif")


def draw_hex_background():
    hex_drawer = turtle.Turtle()
    hex_drawer.hideturtle()
    hex_drawer.speed(0)
    hex_drawer.color("#111a2b")
    side = 20
    dx = side * 3**0.5
    dy = side * 1.5
    for x in range(-300, 340, int(dx)):
        for y in range(-300, 340, int(dy)):
            draw_single_hex(hex_drawer, x, y, side)

def draw_single_hex(t, x, y, side):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    for _ in range(6):
        t.forward(side)
        t.left(60)
    t.penup()

draw_hex_background()


score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("#00ffff")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 22, "bold"))


head = turtle.Turtle()
head.speed(0)
head.shape("media/Right.gif")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("media/food_resized.gif")
food.penup()
food.goto(0, 100)


segments = []


def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.shape("media/Up.gif")

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("media/Down.gif")

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.shape("media/Left.gif")

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.shape("media/Right.gif")

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)


win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")

def get_segment_shape(prev, curr, next_):
    if prev.xcor() == next_.xcor():
        return "media/Vertical.gif"
    elif prev.ycor() == next_.ycor():
        return "media/Horizontal_.gif"
    else:
        dx1 = curr.xcor() - prev.xcor()
        dy1 = curr.ycor() - prev.ycor()
        dx2 = next_.xcor() - curr.xcor()
        dy2 = next_.ycor() - curr.ycor()
        if (dx1, dy1, dx2, dy2) in [
            (0, 20, 20, 0), (20, 0, 0, 20)]: return "media/Top_Right.gif"
        elif (dx1, dy1, dx2, dy2) in [
            (0, -20, -20, 0), (-20, 0, 0, -20)]: return "media/Bottom_Left.gif"
        elif (dx1, dy1, dx2, dy2) in [
            (-20, 0, 0, 20), (0, 20, -20, 0)]: return "media/Left_Top.gif"
        elif (dx1, dy1, dx2, dy2) in [
            (0, -20, 20, 0), (20, 0, 0, -20)]: return "media/Right_Bottom_.gif"
        return "media/Horizontal_.gif"


delay = 0.1
while True:
    win.update()

    
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 22, "bold"))


    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.goto(1000, 1000)  
        new_segment.shape("media/Horizontal_.gif")
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 22, "bold"))

    
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    
    for i in range(len(segments)):
        if i == 0:
            if head.direction in ["left", "right"]:
                segments[i].shape("media/Horizontal_.gif")
            else:
                segments[i].shape("media/Vertical.gif")
        elif i < len(segments) - 1:
            segments[i].shape(get_segment_shape(segments[i-1], segments[i], segments[i+1]))
        else:
            segments[i].shape("media/Horizontal_.gif")  

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 22, "bold"))

    time.sleep(delay)
