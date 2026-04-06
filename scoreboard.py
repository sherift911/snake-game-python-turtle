from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}  High score: {self.high_score}", align="center", font=("Arial",24,"normal")) 

    
    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def get_highscore(self):
        with open("highscore.txt", "r") as file:
            return int(file.read())
            
    def saved_highscore(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))    

    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0, 0)
        if self.score > self.high_score:
            self.high_score = self.score
            self.saved_highscore()
            
        self.write(f" -------Game over------\n    Your Score: {self.score}\n\n    High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))