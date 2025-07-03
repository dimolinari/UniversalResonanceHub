from glifo_generator import generar_glifo
import matplotlib.pyplot as plt
import numpy as np

# Glifo para el símbolo ॐ
x, y = generar_glifo("ॐ")

plt.figure(figsize=(8, 8))
plt.plot(x, y, 'b-', linewidth=0.1)
plt.axis('equal')
plt.axis('off')
plt.title("Glifo Fractal para ॐ", fontsize=12)
plt.savefig("om_fractal.png", dpi=1200)
plt.show()
