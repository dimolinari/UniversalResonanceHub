import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

PARAMS = {
    "अ": (0.1, 0.3, 1.0),
    "म": (0.22, 0.35, 0.8),
    "ह": (0.17, 0.28, 1.2)
}

def duffing_modified(state, t, alpha, beta, gamma):
    x, y = state
    dxdt = y
    dydt = -alpha*y + beta*x - gamma*x**3 + 0.5*np.sin(2*np.pi*t)
    return [dxdt, dydt]

def generar_glifo(caracter, num_puntos=10000):
    alpha, beta, gamma = PARAMS.get(caracter, (0.2, 0.3, 1.0))
    t = np.linspace(0, 100, num_puntos)
    sol = odeint(duffing_modified, [0.01, 0.01], t, args=(alpha, beta, gamma))
    x, y = sol.T

    theta = np.arctan2(y, x)
    r = np.sqrt(x**2 + y**2)
    x_new = r * np.cos(theta + np.sin(r)*np.pi)
    y_new = r * np.sin(theta + np.cos(r)*np.pi)

    return x_new, y_new

if __name__ == "__main__":
    x, y = generar_glifo("ॐ")
    plt.figure(figsize=(8,8))
    plt.plot(x, y, 'k-', linewidth=0.1)
    plt.axis('equal')
    plt.axis('off')
    plt.savefig('om_fractal.png', dpi=1200)
