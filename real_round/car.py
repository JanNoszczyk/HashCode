from random import shuffle
import math
import time

def read(file_path):
    # reads the file to self.piza
    with open(file_path) as f:
        lines = f.readlines()
        # Save information from first row
        rows, columns, vehicles, number_rides, bonuses, steps = lines[0].split(' ')
        #print(steps)
        #steps = steps[:-2]
        #print(steps)
        rides = []
        content = [x.strip() for x in lines]
        for i in range(1, len(lines)):
            # TODO Needs doing line by line after line 1
            #print(lines[i])
            position_start_x, position_start_y, position_end_x, position_end_y, \
                time_start, time_end = tuple(map(int, lines[i].split(' ')))
            rides.append(Ride((position_start_x, position_start_y), \
                (position_end_x, position_end_y), time_start, time_end, i-1))
            #rides.append(Ride((position_start_x, position_start_y), \
            #    (position_end_x, position_end_y), time_start, time_end))
    return int(rows), int(columns), int(vehicles), int(number_rides), int(bonuses), \
              int(steps), rides
              
def output_cars(cars, file_path):
    with open(file_path, "w") as f:
        for car in cars:
            ids = []
            for ride in car.rides:
                ids.append(str(ride.id))
                final_list = [str(len(ids))] + ids
                string = " ".join(final_list)
            f.write(string + "\n")
                
def distance(start_x, start_y, end_x, end_y):
    return abs(start_x-end_x) + abs(start_y-end_y)

def distance(start_position, end_position):
    return abs(start_position[0]-end_position[0]) + \
        abs(start_position[1]-end_position[1])

def best_ride_NR(rides, car, t, cars, inpt_numbers):
    #good_rides = []
    best_ride = ""
    best_scoring = -math.inf
    for j in range(len(rides)):
        if rides[j].been_taken:
            continue
            print("bad: ride not removed")
            time.sleep(10)
        if rides[j].time_end < t:
            del(rides[j])
            print("removed ride %s" %j)
            #time.sleep(1)            
        finish_time = rides[j].finish_at(car.busy_till, car.next_position)
        if finish_time > rides[j].time_end:
            continue
        if rides[j].time_end > inpt_numbers['T']:
            print("end_time > T!!")
            time.sleep(10)
        time_till_journey_start = max(distance(car.next_position,rides[j].position_start), \
                rides[j].time_start-t)
        gets_bonus = (t+distance(car.next_position,rides[j].position_start)<=rides[j].time_start)
        
        if False:
          min_dist_other_car = math.inf #stochastic?
          for i in range(len(cars)):
              if cars[i] == car:
                  continue
              dist = distance(cars[i].next_position,rides[j].position_end)
              min_dist_other_car = min(min_dist_other_car,dist)
         
        if True:
          min_dist_other_car = math.inf #stochastic!
          rand_idices = list(range(len(cars)))
          shuffle(rand_idices)
          for i in rand_idices[1:min(20,len(cars))]:
              if cars[i] == car:
                  continue
              dist = distance(cars[i].next_position,rides[j].position_end)
              min_dist_other_car = min(min_dist_other_car,dist)        
          
        time_till_completion = time_till_journey_start + rides[j].distance
        score_gain = (gets_bonus)*inpt_numbers['B'] + rides[j].distance
        waiting_time = time_till_journey_start - distance(car.next_position,rides[j].position_start)
        could_be_later_time = rides[j].time_end - finish_time
        
        if finish_time != t + time_till_completion:
            print("bad1!!")
            print(str(finish_time - ( t + time_till_completion)))           
            print(str(finish_time)+" "+str(t)+" "+str(time_till_completion))           
            time.sleep(3)
        
        #ride_scoring = score_gain * 1.0 / time_till_completion
        #ride_scoring = (gets_bonus)*Bonus - waiting_time
        #ride_scoring = rides[j].distance + (gets_bonus)*Bonus - waiting_time
        #ride_scoring = ( score_gain * 1.0 / time_till_completion ) / \
        #    (time_till_completion + could_be_later_time)
        ride_scoring =  score_gain / time_till_completion \
              + 1.0/10 * min_dist_other_car / math.sqrt( \
              inpt_numbers['Rows'] * inpt_numbers['Cols'] / min(20.0,inpt_numbers['Cars']) )
        #being far is only good if it is <distance or so
        
        if ride_scoring > best_scoring:
            best_ride = j
            best_scoring = ride_scoring
    #if best_ride=="":
    #    print("bad2!!")
    return best_ride, best_scoring
            
        
class Ride:
    id = ""
    position_start = []
    position_end = []
    time_start = ""
    time_end = ""
    been_taken = False
    distance = 0
    
    def __init__(self, position_start, position_end, time_start, time_end, id):
        self.position_start = position_start
        self.position_end = position_end
        self.time_start = time_start
        self.time_end = time_end
        self.id = id
        self.distance = distance(position_start, position_end)

    def distance(self):
        return abs(self.position_start[0]-self.position_start[0]) + abs(self.position_start[1]-self.position_end[1])

    def in_time(self, start_time):
        return start_time - self.distance() < self.time_end
        
    def finish_at(self, car_start_time, car_position):
        arrive_time = car_start_time + distance(car_position,self.position_start)
        ride_start_time = max(arrive_time,self.time_start)
        ride_end_time = ride_start_time + distance(self.position_start,self.position_end)
        return ride_end_time

   
        
        
class Car:
    rides = []
    start_time = []
    done = []
    is_busy = False
    busy_till = 0
    next_position = [0,0] #position where next ride ends
    id = ''
    
    def __init__(self, id):
        self.rides = []
        self.id = id

    def add_journey(self, start_time, ride):
        #print("ride added tried")
        #if ride.in_time(start_time) and not self.is_busy:
        #if ride.in_time(start_time):
        if True:
            self.rides.append(ride)
            print("ride %s added for car %s" % (str(ride.id),str(self.id)) )
            ride.been_taken = True
            #if rides.length() = 0:
            '''
            if len(rides) == 0:
                self.busy_till = ride.finish_at(busy_till,[0,0])                
            else:
                self.busy_till = ride.finish_at(busy_till,rides[-1].position_end)
            '''
            self.busy_till = ride.finish_at(self.busy_till,self.next_position)
            next_position = ride.position_end
        else:
            print("bad!!")
            time.sleep(3)
    #def busy_until(
            
            
    def is_busy(self, start_time, end_time):
        for ride in self.rides:
            if (start_time > ride.time_start \
                and start_time < ride.time_end) \
                or (end_time > ride.time \
                and end_time < self.end_time):
                return True
        return False

