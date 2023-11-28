from turtle import Turtle

ALIGNMENT = "center"
FONT = ('COURIER', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAMEOVER", move=False, align=ALIGNMENT, font=FONT)

    def save_high_score(self):
        f = open("highscore.txt", "r")
        highscore = f.readline()

        score = int(highscore.split(",")[1])

        if self.score > score:
            f = open("highscore.txt", "w")
            f.write(f"highscore,{self.score}")
            f.close()
        else:
            f.close()