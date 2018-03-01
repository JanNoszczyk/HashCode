import numpy as np
import sys

class Pizza:
    """Class"""
    path = ""
    file_type = 0
    pizza = []
    rows = 0
    columns = 0
    min_ingredients = 0
    max_cells = 0
    output = ""

    def __init__(self, path):
        self.path = path
        print("Reading file:", path)
        self.input = self.read(path)

    def read(self, file_path):
        # Save each line as column
        with open(file_path) as f:
            first_line = f.readline()
            # Save information from first row
            self.rows, self.columns, self.min_ingredients, self.max_cells = tuple(map(int, first_line.split(' ')))
            grid = []
            for i in range(self.rows):
                grid.append(f.readline().rstrip())
            self.pizza = grid

    def writeOutput(self, file_path):
        with open(file_path, mode="w") as f:
            f.write(self.output)



