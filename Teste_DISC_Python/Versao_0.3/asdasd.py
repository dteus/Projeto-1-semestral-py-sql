medidas = [12.95, 8.36, 9.39, 7.26, 4.32, 9.30, 7.36, 4.31, 9.30, 9.39]
medidas.sort()
min = min(medidas)
max = max(medidas)
print(medidas)
print(f'minimo: {min}')
print(f'maximo: {max}')
print(f'media: {sum(medidas)/float(len(medidas))}')

import matplotlib.pyplot as plt
import numpy as np
data = {1: 12.95, 2: 8.36, 3: 9.39, 4: 7.26, 5: 4.32, 6: 9.30, 7: 7.36, 8: 4.31, 9: 9.30, 10: 9.39}

N = 21
x = np.linspace(0, 10,10)
y = [4.31, 4.32, 7.26, 7.36, 8.36, 9.3, 9.3, 9.39, 9.39, 12.95]
# fit a linear curve and estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')

plt.show()