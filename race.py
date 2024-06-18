from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race Betting Game")

colors = ["red", "orange", "magenta", "blue", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
x_positions = -230
all_turtles = []

# Ask user to make a bet
user_bet = screen.textinput(title="Make your bids!", prompt="Which turtle will win the game? Enter a color: ")

# Display user's bet on the screen
if user_bet:
    bet_turtle = Turtle()
    bet_turtle.hideturtle()
    bet_turtle.penup()
    bet_turtle.goto(-200, 150)
    bet_turtle.write(f"You bet on: {user_bet}", align="left", font=("Arial", 12, "normal"))

# Create turtles and set up initial positions
for idx in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.goto(x=x_positions, y=y_positions[idx])
    turtle.color(colors[idx])
    all_turtles.append(turtle)

race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                result = f"You won! The {winning_color} turtle is the winner!"
            else:
                result = f"You lost! The {winning_color} turtle won."
            
            # Display result on the screen
            result_turtle = Turtle()
            result_turtle.hideturtle()
            result_turtle.penup()
            result_turtle.goto(-200, 120)
            result_turtle.write(result, align="left", font=("Arial", 12, "normal"))

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Keep the window open until the user closes it
screen.mainloop()
