"""
The coast redwood tree species, Sequoia sempervirens, includes some of
the oldest and tallest living organisms on Earth. Details concerning individual trees
are given in the tab-delimited text file redwood-data.txt, available at https://scipython.com/ex/bbd. 
(Data courtesy of the Gymnosperm database, www.conifers.org/cu/Sequoia.php)
Write a Python program to read in this data and report the tallest tree and the tree
with the greatest diameter.
"""

redwood_file = r'C:\Users\manym\Documents\Coding\Scipython-book\Chapter 2 - The core python language I\2.6 File Input, Output\redwood-data.txt'
f = open(redwood_file, 'r')
names = []
locations = []
diameters = []  # in m
heights = []  # in m

# Another way to skip the header lines, found inthe online solution
# f.readline()
# f.readline()
for i,line in enumerate(f):
    if i>1:
        fields = line.split('\t')
        names.append(fields[0])
        locations.append(fields[1])
        diameters.append(float(fields[2]))
        heights.append(float(fields[3]))
f.close()
# To find index of maximum element in a list called values use: values.index(max(values))
max_height = heights.index(max(heights))
max_width = diameters.index(max(diameters))
print('The tallest tree is {name} with height {height:.2f} m'.format(name=names[max_height], height=heights[max_height]))
print('The widest tree is {name} with diameter {diameter:.2f} m'.format(name=names[max_width], diameter=diameters[max_width]))