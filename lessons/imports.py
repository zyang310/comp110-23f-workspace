"""Practice importing from other modules"""

from lessons.my_functions import addition

if __name__ == "__main__":
    print("howdy")

print(addition.addition(1, 2))
