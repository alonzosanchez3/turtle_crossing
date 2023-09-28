from turtle import Turtle

FONT = ('Courier', 24, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.level = 0
    self.goto(-400, 220)
    self.level_up()

  def level_up(self):
    self.clear()
    self.level += 1
    self.write(f"Level: {self.level}", align="left", font=FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER!")
