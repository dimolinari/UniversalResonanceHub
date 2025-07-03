# codificador_linguistico.py
# 📡 Módulo de traducción simbólica-cuántica de palabras a parámetros fractales
# Autor: Dicaoz – Eduardo Molina 🇪🇨

def palabra_a_fractal(palabra):
    """
    Convierte una palabra simbólica en parámetros fractales.
    Usa frecuencias culturales y resonancia simbólica.
    """
    freq = {"अ": 0.15, "म": 0.32, "ह": 0.21, "ॐ": 0.45}
    total = sum(freq.values())
    params = []

    for letra in palabra:
        if letra in freq:
            alpha = 0.1 + 0.2 * (freq[letra] / total)
            beta = 0.25 + 0.15 * (freq[letra] / total)
            gamma = 0.8 + 0.4 * (freq[letra] / total)
            params.append((alpha, beta, gamma))

    if not params:
        return 0.3, 0.3, 0.9  # Valores por defecto

    alpha_avg = sum([p[0] for p in params]) / len(params)
    beta_avg = sum([p[1] for p in params]) / len(params)
    gamma_avg = sum([p[2] for p in params]) / len(params)

    return alpha_avg, beta_avg, gamma_avg
