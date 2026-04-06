from turtle import Turtle

class Snake():
    def __init__(self):
        self.position = [(-40,0), (-20,0), (0,0)]
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for i in range(len(self.position)):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.position[i])
            self.turtles.append(new_turtle)

    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.turtles[-1].forward(20) 

    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0, new_segment)

    def move_up(self):
        self.turtles[-1].setheading(90)
    def move_down(self):
        self.turtles[-1].setheading(270)
    def move_right(self):
        self.turtles[-1].setheading(0)
    def move_left(self):
        self.turtles[-1].setheading(180)