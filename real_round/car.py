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



class Car:
    rides = []
    def __init__(self):
        self.rides = []

    def add_journey(self, ride):
        self.journey.append(ride)
