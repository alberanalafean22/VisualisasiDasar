import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 0.58, 0.274)
s = np.sin(3.8 * np.pi * t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (V)')

plt.title('Gelombang Transmitter Panel surya ke inti generator')
plt.grid(True)

plt.show()