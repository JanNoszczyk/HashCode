from pizza import Pizza
from os.path import join, splitext
import sys

# Call this file with an integer like 0 which specifies the first file in the list

# Defining input and output file paths
file_names = [
    "example.in",
    "small.in",
    "medium.in",
    "big.in"
]
file_name = file_names[int(sys.argv[1])]
input_path = join("input", file_name)
output_path = join("output", splitext(file_name)[0]+'.txt')

# Making object from path and storing it in pizza, calls the __init__ function in Pizza
pizza = Pizza(input_path)
# Print what is saved
print(pizza.pizza)

# Writing the output which is stored in pizza.output
pizza.writeOutput(output_path)