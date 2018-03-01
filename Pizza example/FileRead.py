import numpy as np
import sys

filenames = 'example.in','small.in','medium.in','big.in'
print("Using input file Nr %s" % sys.argv[1])
filename = filenames[int(sys.argv[1])]

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

#Remove first line
Data_array = Data_array[1:]
#List each character as array entry
Data_array = [list(x) for x in Data_array]
#Store as numpy array
Numpy_array = np.array(Data_array)

#Print stuff
print(Numpy_array)
print ("Number of rows %s." % Number_rows)
print ("Number of columns %s." % Number_columns)
print ("Minimum ingredient of each type %s." % Min_ingredient)
print ("Max number of cellls %s." % Max_cells)
print(Numpy_array.shape)

#BP was here
Pizza = (Numpy_array=="M")*1
print(Pizza)

#Find minimal pieces within rows
Number_slices = 0;
Slices = []

for i in range(Number_rows):
  line = Pizza[i,:]
  slice_started = False
  for j in range(Number_columns):
    if(not slice_started): #Start new piece if necessarry
      #print("Slice started: %s %s" % (i,j))
      start_piece = j
      length = 0
      Number_0s = 0
      Number_1s = 0
      slice_started = True
    #Add piece to current slice
    length=length+1
    if(line[j]==0):
      Number_0s += 1
    else:
      Number_1s += 1
    if(Number_0s>=Min_ingredient and Number_1s>=Min_ingredient): #Finish slice
      slice = i,start_piece,i,j
      print ("New slice: (%s,%s) to (%s,%s)." % (i,start_piece,i,j))
      Number_slices += 1
      Slices += [slice]
      slice_started = False
    if(length>=Max_cells): #Piece would be too large, so start new one.
      slice_started = False #Start new slice
  

#Write to output file
outfilename = "output_" + filename[:-3] + ".txt"

outputfile = open(outfilename,'w') 
outputfile.write(str(Number_slices) + "\n")
for k in range(Number_slices):
  #outputfile.write(str(Slices[k])[1:-1] + "\n")
  #outputfile.write(''.join(map(str, Slices[k])) + "\n")
  outputfile.write(str(Slices[k]).replace(",","")[1:-1] + "\n") 
outputfile.close() 








