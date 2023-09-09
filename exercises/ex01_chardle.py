"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730713735"

word = str(input("Enter a 5-character word: "))

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_letter = str(input("Enter a single character: "))

if len(single_letter) != 1:
    print("Error: Character must be a single character")
    exit()

counter = 0

print("Searching for " + single_letter + " in " + word)
if single_letter == word[0]:
    print(single_letter + " found at index 0")
    counter += 1

if single_letter == word[1]:
    print(single_letter + " found at index 1")
    counter += 1

if single_letter == word[2]:
    print(single_letter + " found at index 2")
    counter += 1

if single_letter == word[3]:
    print(single_letter + " found at index 3")
    counter += 1

if single_letter == word[4]:
    print(single_letter + " found at index 4")
    counter += 1

if counter > 1:
    print(str(counter) + " instances of " + single_letter + " found in " + word)

elif counter == 1:
    print(str(counter) + " instance of " + single_letter + " found in " + word)
    
else:
    print("No instances of " + single_letter + " found in " + word)