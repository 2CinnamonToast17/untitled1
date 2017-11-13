# Quad function Calc

import matplotlib.pyplot as plt

x_values = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
for x in x_values:
    y = x**2 + 2*x + 1
    print('x={0} y={1}'.format(x, y))
    plt.plot(x, y, marker='o')

plt.show()
