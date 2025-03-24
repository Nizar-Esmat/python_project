import turtle
import coordinates 




# Create a turtle object
t = turtle.Turtle()
turtle.setup(500, 600)
t.hideturtle()
t._color("#f0f0f0")

face_one_start = (0, 120)
face_two_start = (0, -30)
face_there_start = (0, -220)

t.speed(2)
def draw_face(face, start):
    t.penup()
    t.goto(start)
    t.pendown()
    t.color("#000000")
    t.begin_fill()
    for i in range(len(face[0])):
       x , y =  face[0][i]
       t.goto(x , y)
       
    for i in range(len(face[1])):
       x , y =  face[1][i]
       t.goto(x , y)
    t.end_fill()
       

draw_face(coordinates.face_one, face_one_start)
draw_face(coordinates.face_two, face_two_start)
draw_face(coordinates.face_three, face_there_start)