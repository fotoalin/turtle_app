import turtle
import random

# Screen Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Catch the Falling Object Game")
screen.tracer(0)

# Player Setup
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.shapesize(stretch_wid=1, stretch_len=5)
player.penup()
player.goto(0, -250)

# Falling Object Setup
falling_object = turtle.Turtle()
falling_object.shape("circle")
falling_object.color("red")
falling_object.penup()
falling_object.speed(0)
falling_object.goto(random.randint(-290, 290), 290)
falling_object.dy = -6  # Change this value to adjust the falling speed

# Score
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Move Player with Increased Step and Immediate Screen Update
def player_go_left():
    x = player.xcor()
    x -= 40  # Increase the step size for faster movement
    if x < -280:
        x = -280
    player.setx(x)
    screen.update()  # Update the screen immediately after moving

def player_go_right():
    x = player.xcor()
    x += 40  # Increase the step size for faster movement
    if x > 280:
        x = 280
    player.setx(x)
    screen.update()  # Update the screen immediately after moving

# Keyboard Bindings
screen.listen()
screen.onkeypress(player_go_left, "Left")
screen.onkeypress(player_go_right, "Right")

# Main Game Loop
while True:
    screen.update()

    # Move Falling Object
    falling_object.sety(falling_object.ycor() + falling_object.dy)

    # Check for collision with player
    if falling_object.distance(player) < 20:
        falling_object.goto(random.randint(-290, 290), 290)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Check for missing the object
    if falling_object.ycor() < -290:
        falling_object.goto(random.randint(-290, 290), 290)
        score_display.clear()
        score_display.write("Game Over", align="center", font=("Courier", 24, "normal"))
        break  # Ends the game

turtle.done()

