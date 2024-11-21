# Rock, Paper, Scissors, Lizard, Spock

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
    print(f"Player One: {score1}  |  Player Two: {score2}")
    if score1 > score2:
        print("Player One wins!")
    elif score2 > score1:
        print("Player Two wins!")
    else:
        print("It is a draw!")



