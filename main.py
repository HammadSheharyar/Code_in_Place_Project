from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

# Globals
screen = Screen()
welcome_writer = Turtle()
snake = None
food = None
scoreboard = None
is_game_on = False
speed_delay = 0.1  # Default delay (medium)


def bind_keys():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def show_welcome():
    screen.clear()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("Snake Game")

    # Set your welcome background image (must be .gif format)
    screen.bgpic("welcome_bg.gif")

    # No text here, image includes instructions

    screen.listen()
    screen.onkey(lambda: set_difficulty("easy"), "e")
    screen.onkey(lambda: set_difficulty("medium"), "m")
    screen.onkey(lambda: set_difficulty("hard"), "h")


def set_difficulty(level):
    global speed_delay
    if level == "easy":
        speed_delay = 0.15
    elif level == "medium":
        speed_delay = 0.1
    elif level == "hard":
        speed_delay = 0.05

    start_game()


def start_game():
    global snake, food, scoreboard, is_game_on

    screen.clear()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    welcome_writer.clear()
    screen.bgpic("")  # Clear background image for the game

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    bind_keys()

    is_game_on = True
    game_loop()

    # After game over, allow restart by pressing 'r'
    screen.onkey(start_game, "r")


def game_loop():
    global is_game_on
    while is_game_on:
        screen.update()
        time.sleep(speed_delay)  # Speed based on difficulty
        snake.move()

        # Food collision
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_snake()
            scoreboard.increase_score()

        # Wall collision
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            scoreboard.reset_score()
            scoreboard.game_over()
            is_game_on = False

        # Self collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_score()
                scoreboard.game_over()
                is_game_on = False


# Setup screen and show welcome
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
show_welcome()
screen.mainloop()
