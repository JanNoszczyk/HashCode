from os.path import join

class Thing:
    """Class"""
    file_names = [
        "example.in",
        "small.in",
        "medium.in",
        "large.in"
    ]
    input = ""
    output = ""

    def __init__(self, number):
        filename = self.file_names[number]
        path = join("input", filename)
        print("Reading file:", path)
        self.input = self.read(path)

    def read(self, file_path):
        with open(file_path, mode="r") as f:
            data_array = f.readlines()

    def writeOutput(self, file_path):
        with open(file_path, mode="w") as f:
            f.write(self.output)



