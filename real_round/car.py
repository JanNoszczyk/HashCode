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
            print(lines[i])
            position_start_x, position_start_y, position_end_x, position_end_y, \
                time_start, time_end = tuple(map(int, lines[i].split(' ')))
            rides.append(Ride((position_start_x, position_start_y), \
                (position_end_x, position_end_y), time_start, time_end))
    return int(rows), int(columns), int(vehicles), int(number_rides), int(bonuses), \
              int(steps), rides


def distance(start_x, start_y, end_x, end_y):
    return abs(start_x-end_x) + abs(start_y-end_y)

class Ride:
    position_start = []
    position_end = []
    time_start = ""
    time_end = ""

    def __init__(self, position_start, position_end, time_start, time_end):
        self.position_start = position_start
        self.position_end = position_end

    def distance(self):
        return abs(self.position_start[0]-self.position_start[0]) + abs(self.position_start[1]-self.position_end[1])

    def in_time(self, start_time):
        return start_time - self.distance() < self.time_end

class Car:
    rides = []
    start_time = []
    done = []
    def __init__(self):
        self.rides = []

    def add_journey(self, start_time, ride):
        if ride.in_time(start_time) and not Car.is_busy():
            self.journey.append(ride)

    def is_busy(self, start_time, end_time):
        for ride in self.rides:
            if start_time > ride.time_start \
                and start_time < ride.time_end \
                and end_time > ride.time \
                and end_time < self.end_time:
