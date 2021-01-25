import pygal
from die import Die

# input Die information
d = input("input two number and split by space for die1 and die2: ").split()

# Create a D6
die1 = Die(int(d[0]))
die2 = Die(int(d[1]))

print("die1 and die2 done.")

# Make some rolls, and store results in a list.
rtimes = input("rolling times:")

print("rolling and Analyze the results.....")

results = []
for roll_num in range(int(rtimes)):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print("done.\ngenerating Bar-histogram...")

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D" + d[0] + " and a D" + d[1] + " Dice " + rtimes + " times."

# Generating x_labels of bar
hist.x_labels= [str(subscript) for subscript in range(2, max_result + 1)]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D' + d[0] + ' D' + d[1], frequencies)

print("done.")

sf_name = input("input save-filename:")

hist.render_to_file(sf_name + ".svg")
