from turtle import Turtle

ALIGNMENT = "Left"
FONT = "Arial"


class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.color("black")
      self.penup()
      self.hideturtle()
      self.dict = {"states":[], "x": [], "y":[]}
      self.update_scoreboard()

   def update_scoreboard(self):
      self.clear()
      # for state in self.states:
      #    self.goto(obj.x, obj.y)
      #    self.write(arg=f"{state}", move=False, align=ALIGNMENT, font=(FONT, 15, "normal"))


   def l_increase_score(self):
      self.l_score+=1
      self.update_scoreboard()

   def r_increase_score(self):
      self.r_score+=1
      self.update_scoreboard()

   def game_over(self):
      self.goto(0,0)
      self.color("red")
      self.write(arg="GAME OVER", move=False, align="center", font=(FONT, 15, "bold"))

   def win(self):
      self.goto(0,0)
      self.color("red")
      self.write(arg="YOU WIN!", move=False, align="center", font=(FONT, 45, "bold"))