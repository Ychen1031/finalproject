import turtle

def draw_heart():
    window = turtle.Screen()
    window.bgcolor("white")

    heart = turtle.Turtle()
    heart.color("red")
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

    heart.hideturtle()
    window.exitonclick()

if __name__ == "__main__":
    draw_heart()