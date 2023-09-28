from turtle import Turtle

class CustomTurtle(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.setheading(90)
    self.goto(0,-230)

  def move(self):
    print('called')
    self.goto(0, self.ycor() + 20)
    print(self.ycor() + 20)

  def is_at_finish_line(self):
    if self.ycor() > 230:
      print('this was true')
      return True
    else:
      return False

  def go_to_start(self):
    self.goto(0, -230)
