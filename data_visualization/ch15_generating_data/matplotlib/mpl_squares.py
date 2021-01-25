from matplotlib import pyplot as plt

input_values = list(range(0, 6))
squares = [v**2 for v in range(0, 6)]
plt.plot(input_values, squares, linewidth = 5)

plt.title("Square Numbers", fontsize = 16)
plt.xlabel("Value", fontsize = 10)
plt.ylabel("SValue", fontsize = 10)

plt.tick_params(axis = 'both', labelsize = 14)

plt.show()
