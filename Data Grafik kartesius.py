import matplotlib.pyplot as plt

x_axis = [1.32, 2.41, -1.34, 0.42, 1.52, 1.37]
y_axis = [2017, 2018, 2019, 2020, 2021, 2022]

plt.title('Saham BBRI periode 2021')
plt.scatter(x_axis, y_axis, color="darkblue", marker='x', label='Margin')


plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.grid(True)
plt.legend()

plt.show()