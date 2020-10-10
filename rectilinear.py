import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


def model(y, t, k):
    dydt = -k * y
    return dydt

y0 = 5
t = np.linspace(0, 20)

k = 1
y = odeint(model, y0, t, args=(k,))
plt.plot(t, y, linewidth=2, label=f'k={k}')

k = 0.2
y = odeint(model, y0, t, args=(k,))
plt.plot(t, y, linewidth=2, label=f'k={k}')

k = 0.3
y = odeint(model, y0, t, args=(k,))
plt.plot(t, y, linewidth=2, label=f'k={k}')

plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()