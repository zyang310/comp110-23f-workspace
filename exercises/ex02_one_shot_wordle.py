"""Creating a simple wordle game using the concepts learned already."""

__author__ = "730713735"

secret_word: str = "python"
length = len(secret_word)
counter: int = 0

player_guess = input(f"What is your {length}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

color_boxes = ""

while len(player_guess) != len(secret_word):
    new_guess = input(f"That was not {length} letters! Try again: ")
    player_guess = new_guess

if player_guess != secret_word:
    while counter < length:
        if secret_word[counter] == player_guess[counter]:
            color_boxes = f"{color_boxes}{GREEN_BOX}"
        else:
            exist: bool = False
            counter2: int = 0
            while not exist and counter2 < length:
                if player_guess[counter] == secret_word[counter2]:
                    exist = True
                counter2 = counter2 + 1
            if exist:
                color_boxes = f"{color_boxes}{YELLOW_BOX}"
            else:
                color_boxes = f"{color_boxes}{WHITE_BOX}"
        counter = counter + 1
    print(color_boxes)
    print("Not quite. Play again soon!")

counter2 = 0
if player_guess == secret_word:
    while counter2 < length:
        if secret_word[counter2] == player_guess[counter2]:
            color_boxes = f"{color_boxes}{GREEN_BOX}"
        counter2 = counter2 + 1
    print(color_boxes)
    print("Woo! You got it!")
