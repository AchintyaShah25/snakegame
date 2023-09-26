from turtle import Turtle
START = [(0, 0), (-20, 0), (-40,0)]
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snakes = []
        self.snake_sex()
        self.head = self.snakes[0]

    def snake_sex(self):
        for pos in START:
            self.add_snake(pos)

    def add_snake(self,pos):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(pos)
        self.snakes.append(body)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for move in range(len(self.snakes)-1, 0, -1):
            xcor = self.snakes[move - 1].xcor()
            ycor = self.snakes[move - 1].ycor()
            self.snakes[move].goto(xcor, ycor)
        self.head.forward(DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
