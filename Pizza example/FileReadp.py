import numpy as np

filename = 'medium.in'

#Save each line as column
with open(filename) as f:
    Data_array = f.readlines()

#Remove newlines, whitespaces etc
Data_array = [x.strip() for x in Data_array]

#Save information from first row
First_line = [int(i) for i in Data_array[0].split()]
Number_rows = First_line[0]
Number_columns = First_line[1]
Min_ingredient= First_line[2]
Max_cells = First_line[3]

#List each character as array entry
Data_array = [list(x) for x in Data_array]
#Store as numpy array
Numpy_array = np.array(Data_array)
#Remove first line
Numpy_array = np.delete(Numpy_array, 0, 0)

#Print stuff
print(Numpy_array)
print ("Number of rows %s." % Number_rows)
print ("Number of columns %s." % Number_columns)
print ("Minimum ingredient of each type %s." % Min_ingredient)
print ("Max number of cellls %s." % Max_cells)
