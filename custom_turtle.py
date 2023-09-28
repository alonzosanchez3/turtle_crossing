from turtle import Turtle

class CustomTurtle(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.setheading(90)
    self.goto(0,-230)

  def move(self):
    self.goto(0, self.ycor() + 20)
  
