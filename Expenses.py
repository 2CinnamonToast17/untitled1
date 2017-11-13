import matplotlib.pyplot as plt

def createBarChart(data, labels):
    # Number of Bars
    num_bars = len(data)

    #This list is the point on the y-axis where each Bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')

    # Set Label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title('Total Expenditures')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # Number of MONEY I SPENT
    amount = []
    # Corresponding categories
    categories = []

c = int(input('How many categories would you like?'))
for i in range(1, c+1):
    a = input('Enter Category: ')
    b = int(input('Enter Expenditure: '))
    categories.append(a)
    amount.append(b)

createBarChart(amount, categories)
