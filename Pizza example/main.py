from pizza import Pizza
from os.path import join

file_names = [
    "example.in",
    "small.in",
    "medium.in",
    "big.in"
]
path = join("input", file_names[0])

pizza = Pizza(path)
print(pizza.pizza)
