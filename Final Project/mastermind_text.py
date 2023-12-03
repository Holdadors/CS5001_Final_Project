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
            mind_list.append(user_guess) # Add color to current list
            print(mind_list) # print for visual effect
            if user_guess == "RESET":
                mind_list.clear()
        
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