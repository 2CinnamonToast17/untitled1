import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Number')
    plt.ylabel('Ratio')
    plt.title('Ratio between consecutive Fibo. numbers')
    plt.show()


def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 2
    d = []
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        d.append(c / b)
        a = b
        b = c

    draw_graph(range(1, 101), d)

    return series




fibo(100)



