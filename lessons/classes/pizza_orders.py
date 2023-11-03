"""Instantiating a Class"""

"""
This is where we instantiate the class we defined in classes.py
In order words, we're creating objects that belong to that class
"""



# import the class
# from <file_name>, <module_name> import <class>
from lessons.classes.pizza import Pizza


my_pizza: Pizza = Pizza("large", 10, True) # Constructor

#access/set/update attribute values
#my_pizza.size = "Large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True
my_pizza.toppings += 2

print("Size: ")
print(my_pizza.size)

# print("my_pizza: ")
# print(Pizza)

# print("pizza class: ")
# print(Pizza)

# Make sals_pizza size medium, 5 toppings, NOT GF
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """Function to Compute the price of a pizza"""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1.00
    return cost
# calling function
print(price(my_pizza))
print(price(sals_pizza))

#Calling method
print(my_pizza.price())
print(sals_pizza.price())

my_pizza.add_toppings(3)
print(my_pizza.price())

my_second_pizza: Pizza = my_pizza.add_toppings_new_orders(2)
print(my_second_pizza.toppings)
print(my_pizza.toppings)
