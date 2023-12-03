#2. Design interface with Turtle (Play area, status area, scoreboard, selection, .gif etc)
#3. Marble placement using marble file to draw circles and marble guess panel and mouse clicks

from turtle import *
import random
from Marble import *

def draw_rectangle(myturtle, x_cor, y_cor, width, height, color = "black"):
    """Draw game area rectangles (starts top left corner)"""
    # Lift Turtle up and place it to desired coordinate
    myturtle.color(color)
    myturtle.penup()
    myturtle.goto(x_cor,y_cor)
    myturtle.pendown()
    for i in range(2):
        myturtle.forward(width)
        myturtle.right(90)
        myturtle.forward(height)
        myturtle.right(90)

def gif_register(t):
    """Sets up the gameboard including gif, and pensize"""
    # Set up the main screen
    t.screen.title("CS5001 MasterMind Code Game")
    t.speed(0)

    # Change pen size, set up window
    t.pensize(6)
    t.screen.setup(1000,800)

    # gif messages
    t.screen.register_shape("Final Project/leaderboard_error.gif")
    t.screen.register_shape("Final Project/file_error.gif")

    # Interactive gif buttons
    t.screen.addshape("Final Project/checkbutton.gif")
    t.screen.addshape("Final Project/xbutton.gif")  
    t.screen.addshape("Final Project/quit.gif") 

def gif_buttons(t, path, x_cor, y_cor):
    """Sets up gif buttons"""
    # Put gifs at desired location
    t.speed(0)
    t.shape(path)
    t.penup()  # To prevent drawing lines
    t.goto(x_cor, y_cor)  # Replace x1, y1 with the desired coordinates

def marble_win():
        """Winner message pop up then close the game"""
        # Create a new turtle for pop up window with winning message
        win_turtle = turtle.Screen()
        win_turtle.title("Win Window")
        win_turtle.addshape("Final Project/winner.gif")
        win_message = Turtle()
        gif_buttons(win_message, "Final Project/winner.gif", 0, 0)

        # Pause the message for a few seconds, then close everything
        win_turtle.update()
        win_turtle.getcanvas().after(3000, turtle.bye)  # Close after 2 seconds

def marble_lose():
        """loser message pop up then close the game"""
        # Create a new turtle for pop up window with winning message
        lose_turtle = turtle.Screen()
        lose_turtle.title("Lose Window")
        lose_turtle.addshape("Final Project/Lose.gif")
        lose_message = Turtle()
        gif_buttons(lose_message, "Final Project/Lose.gif", 0, 0)

        # Pause the message for a few seconds, then close everything
        lose_turtle.update()
        lose_turtle.getcanvas().after(3000, turtle.bye)  # Close after 2 seconds

def marble_quit(x_cor, y_cor):
    """Quit message pop up then close the game"""
    # Create a new turtle for pop up window with quit message
    quit_turtle = turtle.Screen()
    quit_turtle.title("Quit Window")
    quit_turtle.addshape("Final Project/quitmsg.gif")
    quit_message = Turtle()
    gif_buttons(quit_message, "Final Project/quitmsg.gif", 0, 0)

    # Pause the message for a few seconds, then close everything
    quit_turtle.update()
    quit_turtle.getcanvas().after(3000, turtle.bye)  # Close after 2 seconds

def file_error(x_cor, y_cor):
    """file error message pop up then close the game"""
    # Create a new turtle for pop up window with quit message
    file_turtle = turtle.Screen()
    file_turtle.title("File Error Window")
    file_turtle.addshape("Final Project/file_error.gif")
    file_message = Turtle()
    gif_buttons(file_message, "Final Project/file_error.gif", 0, 0)

    # Pause the message for a few seconds, then close everything
    file_message.update()
    file_message.getcanvas().after(3000, turtle.bye)  # Close after 2 seconds

def leader_error(x_cor, y_cor):
    """leaderboard error message pop up then close the game"""
    # Create a new turtle for pop up window with quit message
    leader_turtle = turtle.Screen()
    leader_turtle.title("Leaderboard Error Window")
    leader_turtle.addshape("Final Project/leaderboard_error.gif")
    leader_message = Turtle()
    gif_buttons(leader_message, "Final Project/leaderboard_error.gif", 0, 0)

    # Pause the message for a few seconds, then close everything
    leader_message.update()
    leader_message.getcanvas().after(3000, turtle.bye)  # Close after 2 seconds

# Global variables
colors = ["red", "blue", "green", "yellow", "purple", "black"]
marble_row = 0
marble_column = 0

def main():
    # Create turtle object
    t = Turtle()

    # Set up all gif messages
    gif_register(t)

    # Set up all gif buttons
    turtle_check = Turtle()
    turtle_X = Turtle()
    turtle_quit = Turtle()
    gif_buttons(turtle_check, "Final Project/checkbutton.gif", 0, -290)
    gif_buttons(turtle_X, "Final Project/xbutton.gif", 70, -290)
    gif_buttons(turtle_quit, "Final Project/quit.gif", 350, -290)

    # Draw masterlist
    draw_rectangle(t, -490, 390, 600, 600)

    # Draw masterlist big marbles and small marbles 
    marble_masterlist = []
    bulls_masterlist = []
    marble_y = 335
    bull_y = 362

    # 10 rows of big marbles
    for marble_rows in range(10):
        marble_list = []
        bulls_list = []
        marble_x = -410
        # 4 columns of big marbles
        for marble_columns in range(4):
            marble = Marble(Point(marble_x, marble_y), "blue", 20)
            marble.draw_empty()
            marble_list.append(marble)
            marble_x += 67
        marble_masterlist.append(marble_list)
        # Draw masterlist bulls and cows (2 x 2)
        for bull_row in range(2):
            marble_x = -62
            for bull_column in range(2):
                bulls = Marble(Point(marble_x, bull_y), "blue", 5)
                bulls.draw_empty()
                bulls_list.append(bulls)
                marble_x += 20
            bull_y -= 21  
        bulls_masterlist.append(bulls_list)          
        marble_y -= 59
        bull_y -= 17

    # Draw user manual
    draw_rectangle(t, -490, -220, 970, 165)

    # Draw user manual marbles 
    marble_x = -420
    marble_y = -310
    manual_list = []
    for i in range(6):
        global colors
        marble = Marble(Point(marble_x, marble_y), colors[i], 20)
        marble.draw()
        manual_list.append(marble)
        marble_x += 62
    
    # Draw leaderboard
    draw_rectangle(t, 150, 390, 310, 600, "blue")

    def select_color(x_cor, y_cor):
        """Select color to fill the marbles"""
        global marble_row
        global marble_column
        for manual_marble in manual_list:
            result = manual_marble.clicked_in_region(x_cor,y_cor)
            if result is True and marble_column < 4:
                manual_marble.draw_empty()
                chosen_color = manual_marble.get_color()
                marble_masterlist[marble_row][marble_column].set_color(chosen_color)
                marble_masterlist[marble_row][marble_column].draw()
                marble_column += 1

    def marble_check(x_cor, y_cor):
        """confirm selection"""
        global marble_row
        global marble_column
        color_list = []
        for marble in marble_masterlist[marble_row]:
            color_list.append(marble.color)

        # Check # of bulls and cows
        num_bulls = 0
        num_cows = 0
        for i in range(len(color_list)):
            if color_list[i] in secret_code:
                # If color is in the set
                if color_list[i] == secret_code[i]:
                    # Right color and position
                    num_bulls += 1
                else: 
                    # Right color wrong position
                    num_cows += 1
                # If there are 4 bulls:

        # If all colors are in the right location
        if num_bulls == 4:
            marble_win()

        # If marble is not equal to secret code, show # of bulls and cows
        for bulls in range(num_bulls):
            bulls_masterlist[marble_row][bulls].set_color("black")
            bulls_masterlist[marble_row][bulls].draw()

        for cows in range(num_cows):
            cows = cows + num_bulls
            bulls_masterlist[marble_row][cows].set_color("red")
            bulls_masterlist[marble_row][cows].draw()

        # Onto next guess
        marble_row += 1
        marble_column = 0
        
        # If secret code was not guessed after 10 guesses
        if marble_row == 10:
            marble_lose()

        # Restore manual marbles after check
        for manual_marble in manual_list:
            manual_marble.draw()

    def marble_X(x_cor, y_cor):
        """Remove selection"""
        global marble_row
        global marble_column
        marble_column = 0
        for i in range(4):
            marble_masterlist[marble_row][i].draw_empty()

    # Generate secret code
    colors = ["red", "blue", "green", "yellow", "purple", "black"]
    secret_code = random.sample(colors, 4)
    print(secret_code)

    # Function for clicking user manual
    t.screen.onclick(select_color)

    # Function for clicking check, X, and quit
    turtle_check.onclick(marble_check)
    turtle_X.onclick(marble_X)
    turtle_quit.onclick(marble_quit)

    t.screen.mainloop()

    
if __name__ == "__main__":
    main()