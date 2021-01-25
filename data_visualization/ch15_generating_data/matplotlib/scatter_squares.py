import matplotlib.pyplot as plt

x_value = list(range(1, 151));
y_value = [x ** 0.8 for x in x_value];
y2_value = [x ** 1 for x in x_value];
y3_value = [x ** 1.2  for x in x_value];

plt.scatter(x_value, y_value, edgecolor = 'none', s = 4);
plt.scatter(
    x_value, y2_value,
    c = y2_value,
    cmap = plt.cm.Reds,
    edgecolor = 'none',
    s = 4
);
plt.scatter(x_value, y3_value, c = (0, 0.4, 0), edgecolor = 'none', s = 4);

plt.title("Compare Function", fontsize = 24);
plt.xlabel("value", fontsize = 14);
plt.ylabel("S value", fontsize = 14);

plt.tick_params(axis = 'both', which = 'major', labelsize = 14);

#plt.show();

plt.savefig("cmp_func.png", bbox_inches = 'tight');
