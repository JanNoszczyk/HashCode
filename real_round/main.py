from car import read
from os.path import join, splitext
import sys

# Call this file with an integer like 0 which specifies the first file in the list
# Defining input and output file paths
file_names = [
    "a_example.in",
    "b_should_be_easy.in",
    "c_no_hurry.in",
    "d_metropolis.in",
    "e_high_bonus.in"
]
file_name = file_names[int(sys.argv[1])]
input_path = join("input", file_name)
output_path = join("output", splitext(file_name)[0]+'.txt')

# reading file
rows, columns, vehicles, rides, bonuses, steps, rides = read(input_path)
