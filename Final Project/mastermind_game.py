"""
Jiajun Fang
CS 5001 Final Project Mastermind
11/29/2023
"""

"""
GAME MECHANICS
1. Player able to input user name
2. Player able to click on colors, checks, x, and quit
3. Player will have 10 guesses of the color sequence - black = right color and position,
red = right color wrong position.
4. Player get to select colors, and erase them by clicking x.
5. Player get to click check to finalize their colorpick
6. Scores are recorded by # of tries they took (lower the better)
7. No colors can be repeated, everytime a color is selected, the selection color will
dissapear. 
"""

"""
Do To List:
1. Text version mechanics (minimal text refinement)
2. Design interface with Turtle (Play area, status area, scoreboard, selection, .gif etc)
3. Marble placement using marble file to draw circles and marble guess panel and mouse clicks
4. Turn text mechanics into game rules (code generation, reset, accept marble guess, quit button)
5. Save scores with scoreboard and scoreboard.txt
6. Clean code, comments, try catch errors
7. Write design.txt (Write your design description. Do your final testing)
and any extra optional work (e.g. skinning your game). Wrap up any other outstanding task.
"""

import random

def main():

    colors = ["red", "blue", "green", "yellow", "purple", "black"]

    secret_code = random.sample(colors, 4)
    print(secret_code)
    # Generator: creates a list that contains 4 of the 6 colors in a list

    # User input and start
    user_name = input("Welcome to a game of Mastermind! Please enter your name: ")
    print(f"Hello! {user_name}, please play away! ")

    # initialize 
    master_mind_list = []
    game_status = True
    round_count = 0
    
    # game mechanic
    while game_status is True:
        round_count += 1
        # 10 Guesses
        mind_list = []
        while len(mind_list) < 4:
            # 4 Marbles to fill in
            user_guess = input("Pick a color, press enter to confirm, type 'RESET' to reset choices: ")
            if user_guess == "RESET":
                mind_list.clear()
            mind_list.append(user_guess) # Add color to current list
            print(mind_list) # print for visual effect
        
        master_mind_list.append(mind_list)
        num_bulls = 0
        num_cows = 0
        # game feedback
        for i in range(len(mind_list)):
            if mind_list[i] in secret_code:
                # If color is in the set
                if mind_list[i] == secret_code[i]:
                    # Right color and position
                    num_bulls += 1
                else: 
                    # Right color wrong position
                    num_cows += 1
        print(f"There are {num_bulls} bulls and {num_cows} cows ")

        # If there are 4 bulls:
        if num_bulls == 4:
            print("You won!")
            game_status = False
            break

        # If 10 tries are finished:
        if round_count == 10:
            print("You lose!")
            game_status = False
            break

        # Need to record game_status when ended for scoreboard

if __name__ == "__main__":
    main()