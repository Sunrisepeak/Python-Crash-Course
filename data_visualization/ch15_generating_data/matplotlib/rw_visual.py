import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(10000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi = 128, figsize = (5, 3))

    # printing
    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_value,
        rw.y_value,
        c = point_numbers,
        cmap = plt.cm.Greens,
        s = 5 
    );

    # Emphasize the first and last points.
    plt.scatter(0, 0, c = 'yellow', s = 100);
    plt.scatter(rw.x_value[-1], rw.y_value[-1] , c = 'red', s = 100);

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    
    user_cmd = input("Make another Walk_Picture?(y/n)")
    if user_cmd == 'n':
        break
