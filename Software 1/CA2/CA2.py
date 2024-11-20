import random

# print("1. Rock, Paper, Scissors, Lizard, Spock")
# print("2. Hangman")
# print("3. Exit")
# menu_choice = int(input("Please choose one of the above options (enter 1, 2 or 3): "))

# # HANGMAN
# if menu_choice == 2:

words = ['baubles' , 'guards' , 'boneshaker' , 'drudges' , 'medicide' , 'full-bottom' , 'coagulase' , 'simmer' , 'bunnia' , 'tremie' , 'muttonheads' , 'roughneck' , 'creds' , 'timber-line' , 'emberiza' , 'dominionism' , 'sunsets' , 'cucujo' , 'earthbank' , 'streaks' , 'extravagate' , 'conjuncture' , 'elongator' , 'ology' , 'cutworms' , 'refusion' , 'levitator' , 'unbowel' , 'keenness' , 'droschka' , 'darnels' , 'flammables' , 'wildtype' , 'gypsy' , 'retrainee' , 'piaga' , 'giddy-head' , 'rastafarianism' , 'selenology' , 'hymenoptera' , 'wrist-drop' , 'triggermen' , 'multilingualism' , 'cloaths' , 'hemophobia' , 'retrofit' , 'commandments' , 'unglue' , 'inshining' , 'nicholas' , 'hotfoot' , 'pubkeeper' , 'gas-tank' , 'uprun' , 'stabler' , 'doctrinaires' , 'akathisia' , 'ribcage' , 'neurophysicist' , 'unappropriate']

word = random.choice(words)

lives = 9

display = ["_"] * len(word)
print("The word is " + " ".join(display))

while lives > 0:
    letter = input("Please guess a letter: ").lower()
    if letter in word:
        for i in range(0, len(word)):
            if word[i] == letter:
                display[i] = letter
        print("Well done, the word is " + " ".join(display))
        if "_" not in display:
            print(f"Congratulations, the word is {word}!")
    else:
        lives -= 1
        print("Unlucky, try again!")
        print(f"Lives left: {lives}")
else:
    print("You have run out of lives!")

