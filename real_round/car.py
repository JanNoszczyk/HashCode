def read(file_path):
    # reads the file to self.piza
    with open(file_path) as f:
        lines = f.readline()
        # Save information from first row
        rows, columns, vehicles, rides, bonuses, steps = lines.split(' ')
        steps = steps[:-2]
        rides = []
        content = [x.strip() for x in lines]
        for i in range(1, len(lines)):
            # TODO Needs doing line by line after line 1
            position_start, position_end, time_start, time_end = tuple(map(int, lines[0].split(' ')))
            rides.append(Ride(position_start, position_end, time_start, time_end))
    return int(rows), int(columns), int(vehicles), int(rides), int(bonuses), int(steps), rides


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

    def will_make_it(self, start_time):
        return start_time - self.distance() < self.time_end

class Car:
    rides = []
    start_time = []
    done = []
    def __init__(self):
        self.rides = []

    def add_journey(self, ride):


        self.journey.append(ride)
        return
