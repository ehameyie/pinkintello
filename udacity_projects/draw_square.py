import turtle
    
def draw_square(sissi):
    for count in range (1,5):
        sissi.forward(100)
        sissi.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    #create turtle Bog which draws a square
    bog = turtle.Turtle()
    bog.shape("turtle")
    bog.color("yellow")
    bog.speed(10)

    for count in range (1,36):
        draw_square(bog)
        bog.right(10)
    

    #create turtle Angie that draws a circle
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("green")
    angie.speed(6)
    angie.circle(50)

    #create turtle jess with a triangle
    jess = turtle.Turtle()
    jess.shape("turtle")
    jess.color("red")
    jess.speed(10)
    jess.forward(180)
    jess.right(45)
    jess.forward(180)
    jess.right(157.5)
    jess.forward(1.85*180)
    
    window.exitonclick()

draw_art()

# tried to add a loop with while but unsuccessful
# total_turns = 4
# turn_count = 0
# while(turn_count < total_turns):
# turn_count = turn_count + 1
