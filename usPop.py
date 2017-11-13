import csv
import matplotlib.pyplot as plt


def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Date')
    plt.ylabel('Population')
    plt.show()


def read_csv(filename):
    date = []
    population = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            date.append(int(row[0]))
            population.append(int(row[1]))
        return date, population

if __name__ == '__main__':
    date, population = read_csv('POPTOTUSA647NWDB.csv')
    scatter_plot(date, population)
