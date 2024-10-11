""" Write a program to read in the data from the file swallow-speeds.txt (available
at https://scipython.com/ex/bda) and use it to calculate the average air-speed velocity
of an (unladen) African swallow. Use exceptions to handle the processing of lines
that do not contain valid data points.
"""

# Read the file
filename = r'C:\Users\manym\Documents\Coding\Scipython book\Chapter 4 - The core python language II\4.1 Errors and Exceptions\swallow-speeds.txt'
f = open(filename, 'r')
lines = f.readlines()
f.close()

# Calculate the average velocity
sum = 0  # total sum of velocities
num = 0  # n to divide by in the end
for line in lines:
    try:
        sum += float(line)  # sum valid values
    except ValueError:
        # print(f'{line} is not a valid number.')
        pass
    else:
        num += 1  # count if the line was valid
print("The average velocity of the African swallow is {vel:.2f} m/s.".format(vel=sum/num))

# print(lines)
