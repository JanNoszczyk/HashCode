from car import read, Car, output_cars, best_ride_NR
from os.path import join, splitext
import sys
import math
import time

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
inpt_numbers = {'Rows': rows, 'Cols': columns, 'Cars': vehicles, 'Rides': number_rides, \
                     'B': bonuses, 'T': steps}
print("Started %s with " % file_name)
print(inpt_numbers) 

with open(join("constants", splitext(file_name)[0]+'.txt'), "w") as f:
    for key, val in inpt_numbers.items():
        #w.writerow([key, val])
        f.write(str([key, val])+"\n")
                     
cars = []
for i in range(vehicles):
    cars.append(Car(i))

'''
for i in range(len(cars)):
    cars[i].add_journey(0, rides[i])
'''
'''
for t in range(steps):
    if ( t % math.ceil(steps/10) == 0):
        print("Starting step %s" % t)
        time.sleep(3)
    for i in range(len(cars)):
        if cars[i].busy_till == t:
            best_ride, score = best_ride_NR(rides, cars[i], t, cars, inpt_numbers)
            if best_ride!="":
                cars[i].add_journey(t, rides[best_ride])            
                print(str(score))
'''
                
carst = []
#carst = ("",) * inpt_numbers['T']
#carst = [[],] * inpt_numbers['T']
carst =  [[] for _ in range(inpt_numbers['T'])]
carst[0] = cars
ride_count = 0                
for t in range(steps):
    #print(len(carst[t]))
    if ( t % math.ceil(steps/10) == 0):
        print("Starting step %s, %s of %s rides so far. (%s left)" % \
              (t, ride_count, number_rides, len(rides)))
        time.sleep(3)
    elif ( t % math.ceil(steps/100) == 0):
        print("%s %% of steps, %s of %s rides so far. (%s left)" % \
              (t/math.ceil(steps/100), ride_count, number_rides, len(rides)))
    for car in carst[t]:
        best_ride, score = best_ride_NR(rides, car, t, cars, inpt_numbers)
        if best_ride!="":
            #car.add_journey(t, rides[best_ride])            
            car.add_journey(t, rides.pop(best_ride))            
            print("score: "+str(score))
            if car.busy_till == 1:
                print("baad")
                time.sleep(5)
            (carst[car.busy_till]).append(car)
            #print(car.busy_till)
            #print(len(carst[car.busy_till]))
            ride_count += 1
                
output_cars(cars, output_path)
