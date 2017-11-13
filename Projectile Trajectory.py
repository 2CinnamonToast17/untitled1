from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval

    return numbers


def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    tflight = 2*u*math.sin(theta)/g
    print(tflight, 'seconds for this trajectory')
    # Find time intervals
    intervals = frange(0, tflight, 0.001)

    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        

        draw_graph(x, y)



l = int(input('How Many Trajectories do you want? '))
for i in range(1, l+1):
    if __name__ == '__main__':
        try:
            u = float(input('Enter the initial velocity (m/s): '))
            theta = float(input('Enter the angle of projection (degrees): '))
        except ValueError:
            print('You entered an invalid input')
        else:
            draw_trajectory(u, theta)


plt.show()
