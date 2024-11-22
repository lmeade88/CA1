import random
import sys

returnToMainMenu = "n"

def mainMenu():
    print("")
    print("-------------------MAIN MENU---------------------------")
    print("1. Rock, Paper, Scissors, Lizard, Spock")
    print("2. Hangman")
    print("3. Exit")
    print("----------------------------------------------")
    return int(input("Please choose one of the above options (enter 1, 2 or 3): "))

# --------------------------------------------------------- ROCK PAPER SCISSORS LIZRAD SPOCK ------------------------------------------------------------
while True:
    menu_choice = mainMenu()
    if menu_choice == 1:
        while returnToMainMenu == "n":
            print("")
            print("-----------------------------ROCK, PAPER, SCISSORS, LIZARD, SPOCK-------------------------------------")

            choices = ["rock", "paper", "scissors", "lizard", "spock"]
            score1 = 0
            score2 = 0

            while score1 < 3 and score2 < 3:
                    player1_choice = input("Player 1, make a choice: ").lower()
                    while player1_choice not in choices:
                        print("Please choose from the 5 options of the game.")
                        player1_choice = input("Player 1, make a choice: ").lower()
                    player2_choice = input("Player 2, make a choice: ").lower()
                    while player2_choice not in choices:
                        print("Please choose from the 5 options of the game.")
                        player2_choice = input("Player 2, make a choice: ").lower()

            # Player 1 chooses Scissors            
                    if player1_choice == "scissors" and player2_choice == "paper":
                        print("Scissors cuts paper!")
                        score1 += 1
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
                print("RESULT")
                print(f"Player One: {score1}  |  Player Two: {score2}")
                if score1 > score2:
                    print("Player One wins!")
                    print("---------------------------------------------------")
                elif score2 > score1:
                    print("Player Two wins!")
                    print("---------------------------------------------------")
                else:
                    print("It is a draw!")
                    print("---------------------------------------------------")
            
            returnToMainMenu = input("Do you want to return to main menu? (Y/N): ").lower()
            if returnToMainMenu == "y":
                break
            else:
                print("Let's play again!")
                menu_choice = 1
                print("---------------------------------------------------")



    # ------------------------------------------------------ HANGMAN --------------------------------------------------------------------------------------

    elif menu_choice == 2:
        returnToMainMenu = "n"
        while returnToMainMenu == "n":
            print("")
            print("-----------------------------HANGMAN-------------------------------------")
            words = ['baubles' , 'guards' , 'boneshaker' , 'drudges' , 'medicide' , 'full-bottom' , 'coagulase' , 'simmer' , 'bunnia' , 'tremie' , 'muttonheads' , 'roughneck' , 'creds' , 'timber-line' , 'emberiza' , 'dominionism' , 'sunsets' , 'cucujo' , 'earthbank' , 'streaks' , 'extravagate' , 'conjuncture' , 'elongator' , 'ology' , 'cutworms' , 'refusion' , 'levitator' , 'unbowel' , 'keenness' , 'droschka' , 'darnels' , 'flammables' , 'wildtype' , 'gypsy' , 'retrainee' , 'piaga' , 'giddy-head' , 'rastafarianism' , 'selenology' , 'hymenoptera' , 'wrist-drop' , 'triggermen' , 'multilingualism' , 'cloaths' , 'hemophobia' , 'retrofit' , 'commandments' , 'unglue' , 'inshining' , 'nicholas' , 'hotfoot' , 'pubkeeper' , 'gas-tank' , 'uprun' , 'stabler' , 'doctrinaires' , 'akathisia' , 'ribcage' , 'neurophysicist' , 'unappropriate']

            word = random.choice(words)

            lives = 9

            display = ["_"] * len(word)
            print("The word is: " + " ".join(display))

            while lives > 0:
                letter = input("Please guess a letter: ").lower()
                if letter in word:
                    for i in range(0, len(word)):
                        if word[i] == letter:
                            display[i] = letter
                    print("Well done, the word is: " + " ".join(display))
                    print("----------------------------------------------")
                    if "_" not in display:
                        print(f"Congratulations, the word is: {word}!")
                        print("----------------------------------------------")
                        break
                else:
                    lives -= 1
                    print("Unlucky, try again!")
                    print(f"Lives left: {lives}")
                    print("----------------------------------------------")
            else:
                print("You have run out of lives!")
                print("----------------------------------------------")

            returnToMainMenu = input("Do you want to return to main menu? (Y/N): ").lower()
            if returnToMainMenu == "y":
                break
            else:
                print("Let's play again!")
                menu_choice = 1
                print("---------------------------------------------------")

    elif menu_choice == "3":
        print("")
        print("You have exited the menu.")
        sys.exit()
    
    else:
        print("You must choose option 1, 2 or 3.")
        menu_choice = int(input("Please choose one of the above options (enter 1, 2 or 3): "))