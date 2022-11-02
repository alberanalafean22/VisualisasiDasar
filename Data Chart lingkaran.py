import matplotlib.pyplot as plt

labels = ['FISIKA', 'MATEMATIKA', 'KIMIA', 'BIOLOGI', 'SAINS ATMOSFER&KEPLANETAN','FARMASI','SAINS LINGKUNGAN KELAUTAN', 'SAINS AKTUARIA', 'SAINS DATA']
quantity = [226, 399, 375, 279, 323, 610, 102, 314, 263]
colors = ['green', 'pink', 'yellow', 'green','darkblue','green','lightskyblue','blue','blue']

plt.title('data jumlah mahasiswa sains itera')
plt.pie(quantity, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.show()

