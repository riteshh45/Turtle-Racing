import turtle
from turtle import Turtle, Screen
import random

is_race_on=False
screen=Screen()

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Choose a color: ")

y_pos=[-70,-40,-10,20,50,80]
colors=["green","red","blue","pink","yellow","black"]

all_turtles=[]
for index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.setposition(-230, y_pos[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have won!. The {winning_color} is winning colour")
            else:
                print(f"You have lost!. The {winning_color} is winning colour")

        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)










screen.listen()





screen.exitonclick()
