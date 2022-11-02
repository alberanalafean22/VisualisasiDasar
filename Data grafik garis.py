import matplotlib.pyplot as plt

y = [19750, 18450, 21780, 20900, 15670]
x = [18, 19, 20, 21, 22]
plt.plot(x, y)

plt.xlabel('tanggal')
plt.ylabel('Harga / liter')

plt.title('Harga Kosan di Sekitar ITERA 2022')
plt.grid(True)

plt.show()