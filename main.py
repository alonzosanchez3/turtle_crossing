from turtle import Turtle, Screen
from custom_turtle import CustomTurtle
import time
from car_manager import CarManager

screen = Screen()
screen.setup(height=500, width=1000)
custom_turtle = CustomTurtle()
car_manager = CarManager()
screen.tracer(0)
screen.listen()
screen.onkey(custom_turtle.move, 'w')

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  car_manager.create_car()
  car_manager.move_cars()

  for car in car_manager.all_cars:
    if(car.distance(custom_turtle) < 20):
      game_is_on = False

  if custom_turtle.is_at_finish_line():
    custom_turtle.go_to_start()
    car_manager.level_up()




screen.exitonclick()