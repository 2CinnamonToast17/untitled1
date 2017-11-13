
import matplotlib.pyplot as plt

greenbrea_temp = [67, 72, 73, 76, 79, 82, 84, 84, 79, 72, 68, 66, 63, 62]
plt.plot(range(10, 24), greenbrea_temp, marker='o')
sausalito_temp = [73, 75, 77, 80, 79, 80, 80, 77, 73, 69, 66, 63, 61, 59]
plt.plot(range(10, 24), sausalito_temp, marker='o')
plt.title("Blue = Greenbrea, Sausalito = Orange")
plt.suptitle("Greenbrea and Sausalito's Hourly weather", fontsize=15)
plt.xlabel("Time by hours")
plt.ylabel("Degrees in Fahrenheit")
plt.show()
