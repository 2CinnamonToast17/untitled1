from collections import Counter
# Calculating the mean of numbers stored in a file


def read_data(filename):

    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))

    return numbers


def calculate_mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s / n

    return mean


def find_differences(numbers):
    # Find the mean
    mean = calculate_mean(numbers)
    # Find the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num - mean)

    return diff


def calculate_variance(numbers):
    # Find the List of differences
    diff = find_differences(numbers)
    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
        # Find The Variance
        sum_squared_diff = sum(squared_diff)
        varience = sum_squared_diff/len(numbers)

        return varience


def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    # Find the median
    if N % 2 == 0:
        # if N is even
        m1 = N / 2
        m2 = (N / 2) + 1
        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N + 1)/2
        # Convert to integer, match position
        m = int(m) - 1
        median = numbers[m]

    return median


def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

if __name__ == '__main__':
    data = read_data('idek.txt')
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data)
    std = variance ** 0.5
    print('Mean: {0}'.format(mean))
    print('Median: {0}'.format(median))
    print('Mode: {0}'.format(mode))
    print('The variance of the list of numbers is {0}'.format(variance))
    print('The standard deviation of the list of numbers is {0}'.format(std))
