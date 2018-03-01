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
        print("Reading file: %s", path)
        input = self.read(path)

    def read(self, file_path):
        return "test"





