from car import read, Car, output_cars
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
rows, columns, vehicles, number_rides, bonuses, steps, rides = read(input_path)

cars = []
for i in range(vehicles):
    cars.append(Car())

'''
for i in range(len(cars)):
    cars[i].add_journey(0, rides[i])
'''
 
for t in range(steps):
    for i in range(len(cars)):
        if cars[i].busy_till <= t:
            for j in range(len(rides)):
                if not rides[j].been_taken:
                    #print("add tried")
                    cars[i].add_journey(0, rides[j])
                    break
                    
            

output_cars(cars, output_path)
