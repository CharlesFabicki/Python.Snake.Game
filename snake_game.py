import turtle
import time
import random

delay = 0.08

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=1600, height=800)
wn.tracer(0)

# Create the segments list
segments = []

# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.direction = "stop"
head.shapesize(1.5, 1.5, 2)

# Set up the score display
score = 0
best_score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-540, 365)
score_display.write("Score: {}    Best Score: {}".format(score, best_score), align="center",
                    font=("Courier", 24, "bold"))


# Reset the score

def snake_died():
    global score
    score = 0
    score_display.clear()
    score_display.write("Score: {}    Best Score: {}".format(score, best_score), align="center",
                        font=("Courier", 24, "bold"))


def scoreboard():
    global score, best_score
    score += 1
    if score > best_score:
        best_score = score
    score_display.clear()
    score_display.write("Score: {}    Best Score: {}".format(score, best_score), align="center",
                        font=("Courier", 24, "bold"))


# Define a list of shapes and colors
shapes = ["circle", "square", "triangle", "turtle"]
colors = ["red", "blue", "green", "yellow", "purple", "orange", "white"]


# Function to update the food turtle's shape and color
def update_food():
    shape_num = random.randint(0, 3)
    color_num = random.randint(0, 6)
    food.shape(shapes[shape_num])
    food.color(colors[color_num])


def handle_collision():
    update_food()


# Create food for the snake
food = turtle.Turtle()
food.speed(0)
update_food()
food.penup()
food.goto(0, 100)


# Define the snake's movement functions
def move_up():
    if head.direction != "down":
        head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_left():
    if head.direction != "right":
        head.direction = "left"


def move_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Set up keyboard bindings
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Create the main game loop
while True:
    wn.update()

    # Check for collision with the wall
    if head.xcor() > 770 or head.xcor() < -770 or head.ycor() > 370 or head.ycor() < -370:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        snake_died()

    # Check for collision with the food
    if head.distance(food) < 20:
        handle_collision()
        scoreboard()
        # Move the food to a random location
        x = random.randint(-770, 770)
        y = random.randint(-370, 370)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score by 1

    # Move the end segments first in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with the snake's body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            snake_died()

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segment list
            segments.clear()

    time.sleep(delay)
