def read_data(filename):

    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))

    return numbers


def calculate_percentile(numbers, p):
    numbers.sort()
    n = len(numbers)
    i = ((n * p)/100) + .5

    return i


if __name__ == '__main__':
    data = read_data('idek.txt')
    percentile = calculate_percentile(data, 25)
    print('Percentile: {0}'.format(percentile))
