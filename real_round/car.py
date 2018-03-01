def read(file_path):
    # reads the file to self.piza
    with open(file_path) as f:
        lines = f.readlines()
        # Save information from first row
        rows, columns, vehicles, number_rides, bonuses, steps = lines[0].split(' ')
        steps = steps[:-2]
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
                ids.append(ride.id)
                final_list = [len(ids)] + ids
                string = " ".join(final_list)
                f.write(string+"\n")         
              
def distance(start_x, start_y, end_x, end_y):
    return abs(start_x-end_x) + abs(start_y-end_y)

def distance(start_position, end_position):
    return abs(start_position[0]-end_position[0]) + \
        abs(start_position[1]-end_position[1])

class Ride:
    id = ""
    position_start = []
    position_end = []
    time_start = ""
    time_end = ""

    def __init__(self, position_start, position_end, time_start, time_end, id):
        self.position_start = position_start
        self.position_end = position_end
        self.time_start = time_start
        self.time_end = time_end
        self.id = id
        

    def distance(self):
        return abs(self.position_start[0]-self.position_start[0]) + abs(self.position_start[1]-self.position_end[1])

    def in_time(self, start_time):
        return start_time - self.distance() < self.time_end
        
    def finish_at(self, car_start_time, car_position):
        arrive_time = car_start_time + distance(car_position,self.position_start)
        ride_start_time = max(arrive_time,self.time_start)
        ride_end_time = ride_start_time + distance(position_start,position_end)
        return ride_end_time

   
        
        
class Car:
    rides = []
    start_time = []
    done = []
    is_busy = False
    busy_till = 0
    next_position = [0,0] #position where next ride ends
    
    def __init__(self):
        self.rides = []

    def add_journey(self, start_time, ride):
        if ride.in_time(start_time) and not Car.is_busy:
            self.rides.append(ride)
            #if rides.length() = 0:
            '''
            if len(rides) == 0:
                self.busy_till = ride.finish_at(busy_till,[0,0])                
            else:
                self.busy_till = ride.finish_at(busy_till,rides[-1].position_end)
            '''
            self.busy_till = ride.finish_at(self.busy_till,self.next_position)
            next_position = ride.end_position
            
    #def busy_until(
            
            
    def is_busy(self, start_time, end_time):
        for ride in self.rides:
            if (start_time > ride.time_start \
                and start_time < ride.time_end) \
                or (end_time > ride.time \
                and end_time < self.end_time):
                return True
        return False

