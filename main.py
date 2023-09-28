from turtle import Turtle, Screen
from custom_turtle import CustomTurtle
import time

screen = Screen()
screen.setup(height=500, width=1000)
custom_turtle = CustomTurtle()
screen.tracer(0)
screen.listen()
screen.onkey(custom_turtle.move, 'w')

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)


screen.exitonclick()