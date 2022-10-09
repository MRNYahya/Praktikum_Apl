import numpy as np
import matplotlib.pyplot as plt

penjualan_pria = [3,5,6,4]
penjualan_wanita = [1,0,8,9]

labels = ['Baju', 'Celana', 'Sepatu','Topi']
x = np.arange(len(labels))
width = 0.20
fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, penjualan_pria, width, label='Pria')
rects2 = ax.bar(x + width / 2, penjualan_wanita, width, label='Wanita')

ax.set_ylabel('Penjualan')
ax.set_title('Grafik Penjualan')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
fig.tight_layout()
plt.show()