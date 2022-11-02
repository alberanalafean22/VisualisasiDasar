from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

y = [3, 2, 3, 4, 5, 11, 14, 14, 4]
x = [1,2,3,4,5,6,7,8,9]

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title('Data Jumlah Mahasiswa Jurusan Sains Institut Teknologi Sumatera')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xlabel('Program Studi')

ax.set_xticks(x)
ax.set_xticklabels((x = ["10-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "91-100"]))

plt.show()
print("sumber:pddikti.kemdikbud.go.id")