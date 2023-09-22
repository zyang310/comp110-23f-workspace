"""Creating Wordle Game Using Functions."""

__author__ = "730713735"

secret = "codes"


def contains_char(word: str, letter: str) -> bool:
    """This function checks whether a letter is in a word."""
    assert len(letter) == 1
    counter: int = 0 
    while counter < len(word):
        if letter == word[counter]:
            return True
        counter = counter + 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """This function gives white, yellow, or green boxes for each letter depending on if they are correct or not."""
    assert len(guess) == len(secret_word)
    
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    counter: int = 0
    colorboxes: str = ""
    length = len(secret_word)
    
    while counter < length:
        if contains_char(secret_word, guess[counter]):
            if guess[counter] == secret_word[counter]:
                colorboxes = colorboxes + GREEN_BOX   
            else:
                colorboxes = colorboxes + YELLOW_BOX
        else:
            colorboxes = colorboxes + WHITE_BOX
        
        counter = counter + 1

    return colorboxes


def input_guess(desired_length: int) -> str: 
    """This function takes the user's guess at a desired length."""
    word: str = input(f"Enter a {desired_length} character word: ")
    while len(word) != desired_length:
        new_word: str = input(f"That wasn't {desired_length} chars! Try again: ")
        word = new_word
    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 6
    turns_taken: int = 0
    win: bool = False
    while turns_taken < turns and not win:
        print(f"=== Turn {turns_taken + 1}/6 ===")
        word = input_guess(len(secret))
        print(emojified(secret, word))
        if word == secret:
            win = True
        else:
            turns_taken = turns_taken + 1
    if win:
        print(f"You won in {turns_taken + 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tommorow!")


if __name__ == "__main__":
    main()