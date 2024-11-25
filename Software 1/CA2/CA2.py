# Import random and sys modules
import random
import sys

# Set return to main menu as "n" (game repeats until it is set to "y")
returnToMainMenu = "n"

# Declare a function called mainMenu which prints menu options and asks user to input a choice.
def mainMenu():
    print("")
    print("-------------------MAIN MENU---------------------------")
    print("1. Rock, Paper, Scissors, Lizard, Spock")
    print("2. Hangman")
    print("3. Exit")
    print("----------------------------------------------")
    # Input is returned whenever the function mainMenu is called.
    return int(input("Please choose one of the above options (enter 1, 2 or 3): "))

# --------------------------------------------------------- ROCK PAPER SCISSORS LIZRAD SPOCK ------------------------------------------------------------

# Infinite loop until user chooses to exit.
while True:
    # Returned input from function mainMenu is stored in variable called menu_choice
    menu_choice = mainMenu()
    # if 1 is entered, game 1 starts
    if menu_choice == 1:
        while returnToMainMenu == "n":
            print("")
            print("-----------------------------ROCK, PAPER, SCISSORS, LIZARD, SPOCK-------------------------------------")

            # Store possible words in a list
            choices = ["rock", "paper", "scissors", "lizard", "spock"]
            # Initialize scores for player 1 and player 2
            score1 = 0
            score2 = 0

            # Until one player has reached a score of 3 points
            while score1 < 3 and score2 < 3:
                    # store player one's choice in a variable and make lowercase
                    player1_choice = input("Player 1, make a choice: ").lower()
                    # verify the choice is one of the possible choices from word list above
                    while player1_choice not in choices:
                        print("Please choose from the 5 options of the game.")
                        player1_choice = input("Player 1, make a choice: ").lower()
                    # store player two's choice in a variable and make lowercase
                    player2_choice = input("Player 2, make a choice: ").lower()
                    # verify the choice is one of the possible choices from word list above
                    while player2_choice not in choices:
                        print("Please choose from the 5 options of the game.")
                        player2_choice = input("Player 2, make a choice: ").lower()
            

            # Player 1 chooses Scissors            
                    if player1_choice == "scissors" and player2_choice == "paper":
                        print("Scissors cuts paper!")
                        # Increase player one's score by 1 point
                        score1 += 1
                        # Display scores
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "scissors" and player2_choice == "rock":
                        print("Rock crushes scissors!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "scissors" and player2_choice == "lizard":
                        print("Scissors decapitates lizard!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "scissors" and player2_choice == "spock":
                        print("Spock smashes scissors!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == player2_choice:
                        print("Draw!")
                        score1 += 1
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
            
            # Comments are the same for each of the choices below...

            # Player 1 chooses Paper            
                    if player1_choice == "paper" and player2_choice == "scissors":
                        print("Scissors cuts paper!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "paper" and player2_choice == "rock":
                        print("Paper covers rock!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "paper" and player2_choice == "lizard":
                        print("Lizard eats paper!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "paper" and player2_choice == "spock":
                        print("Paper disproves Spock!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")

            # Player 1 chooses Rock            
                    if player1_choice == "rock" and player2_choice == "scissors":
                        print("Rock smashes scissors!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "rock" and player2_choice == "paper":
                        print("Paper covers rock!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "rock" and player2_choice == "lizard":
                        print("Rock crushes lizard!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "rock" and player2_choice == "spock":
                        print("Spock vaporizes rock!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")

            # Player 1 chooses Lizard           
                    if player1_choice == "lizard" and player2_choice == "scissors":
                        print("Scissors decapitates lizard!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "lizard" and player2_choice == "paper":
                        print("Lizard eats paper!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "lizard" and player2_choice == "rock":
                        print("Rock crushes lizard!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "lizard" and player2_choice == "spock":
                        print("Lizard poisons Spock!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")

            # Player 1 chooses Spock           
                    if player1_choice == "spock" and player2_choice == "scissors":
                        print("Spock smashes scissors!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "spock" and player2_choice == "paper":
                        print("Paper disproves Spock!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "spock" and player2_choice == "rock":
                        print("Spock vaporizes rock!")
                        score1 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
                    elif player1_choice == "spock" and player2_choice == "lizard":
                        print("Lizard poisons Spock!")
                        score2 += 1
                        print(f"Player One: {score1}  |  Player Two: {score2}")
                        print("---------------------------------------------------")
            else:
                # One of the players or both has reached 3 points
                # Print results and score for each player
                print("RESULT")
                print(f"Player One: {score1}  |  Player Two: {score2}")
                # Calculate winner and announce who won
                if score1 > score2:
                    print("Player One wins!")
                    print("---------------------------------------------------")
                elif score2 > score1:
                    print("Player Two wins!")
                    print("---------------------------------------------------")
                else:
                    # Announce draw in the case that points are equal
                    print("It is a draw!")
                    print("---------------------------------------------------")
            
            # Allow option to return to main menu
            returnToMainMenu = input("Do you want to return to main menu? (Y/N): ").lower()
            # Return if choice is yes
            if returnToMainMenu == "y":
                # end the loop
                break
            else:
                # start game again
                print("Let's play again!")
                menu_choice = 1
                print("---------------------------------------------------")



    # ------------------------------------------------------ HANGMAN --------------------------------------------------------------------------------------

    # if menu choice is 2, start game 2
    elif menu_choice == 2:
        returnToMainMenu = "n"
        # Until return to main menu is "y", repeat loop of game
        while returnToMainMenu == "n":
            print("")
            print("-----------------------------HANGMAN-------------------------------------")
            # List of possible words
            words = ['baubles' , 'guards' , 'boneshaker' , 'drudges' , 'medicide' , 'full-bottom' , 'coagulase' , 'simmer' , 'bunnia' , 'tremie' , 'muttonheads' , 'roughneck' , 'creds' , 'timber-line' , 'emberiza' , 'dominionism' , 'sunsets' , 'cucujo' , 'earthbank' , 'streaks' , 'extravagate' , 'conjuncture' , 'elongator' , 'ology' , 'cutworms' , 'refusion' , 'levitator' , 'unbowel' , 'keenness' , 'droschka' , 'darnels' , 'flammables' , 'wildtype' , 'gypsy' , 'retrainee' , 'piaga' , 'giddy-head' , 'rastafarianism' , 'selenology' , 'hymenoptera' , 'wrist-drop' , 'triggermen' , 'multilingualism' , 'cloaths' , 'hemophobia' , 'retrofit' , 'commandments' , 'unglue' , 'inshining' , 'nicholas' , 'hotfoot' , 'pubkeeper' , 'gas-tank' , 'uprun' , 'stabler' , 'doctrinaires' , 'akathisia' , 'ribcage' , 'neurophysicist' , 'unappropriate']

            # A random word is chosen from the list but hidden from view (not displayed)
            word = random.choice(words)

            # Initialize lives at 9
            lives = 9

            # Display an underscore for each letter of the chosen word
            display = ["_"] * len(word)
            # Display the length of the word in underscores
            print("The word is: " + " ".join(display))

            # Until lives are 0, loop the following
            while lives > 0:
                # Request a letter as input and make lowercase
                letter = input("Please guess a letter: ").lower()
                # If the letter id contained in the word
                if letter in word:
                    # Replace the undercore with the letter
                    for i in range(0, len(word)):
                        if word[i] == letter:
                            display[i] = letter
                    # Display the new version of the word with correct letters and underscores
                    print("Well done, the word is: " + " ".join(display))
                    print("----------------------------------------------")
                    # When all underscores have been replaced
                    if "_" not in display:
                        # Display congratulations and the correct word
                        print(f"Congratulations, the word is: {word}!")
                        print("----------------------------------------------")
                        # End the loop
                        break
                else: # Else the letter is not in the word
                    # Remove one life
                    lives -= 1
                    print("Unlucky, try again!")
                    # Display lives remaining
                    print(f"Lives left: {lives}")
                    print("----------------------------------------------")
            else: # when lives reach zero
                print("You have run out of lives!")
                print("----------------------------------------------")

            # Allow option to return to main menu
            returnToMainMenu = input("Do you want to return to main menu? (Y/N): ").lower()
            if returnToMainMenu == "y":
                break
            else:
                print("Let's play again!")
                menu_choice = 1
                print("---------------------------------------------------")

    # If "Exit" is chosen
    elif menu_choice == "3":
        print("")
        print("You have exited the menu.")
        # Exit the app
        sys.exit()
    
    # In the case that neither 1, 2 or 3 is chosen, request again
    else:
        print("You must choose option 1, 2 or 3.")
        menu_choice = int(input("Please choose one of the above options (enter 1, 2 or 3): "))