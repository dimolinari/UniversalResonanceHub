from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

SIMBOLOS_QUANTICOS = {
    "𓋹": np.array([[1, 0], [0, 0]]),  # Ojo de Horus (|0⟩⟨0|)
    "𓆄": np.array([[0, 0], [0, 1]]),  # Ojo de Ra (|1⟩⟨1|)
    "𝋠": np.array([[0, 1j], [-1j, 0]]) # Cero Maya (σ_y)
}

def circuito_simbolico(simbolos):
    qc = QuantumCircuit(len(simbolos))
    for idx, simbolo in enumerate(simbolos):
        if simbolo in SIMBOLOS_QUANTICOS:
            qc.unitary(SIMBOLOS_QUANTICOS[simbolo], [idx], label=simbolo)

    for i in range(len(simbolos)-1):
        qc.cz(i, i+1)
    qc.cz(len(simbolos)-1, 0)
    return qc

if __name__ == "__main__":
    comando = ["𓋹", "𝋠", "𓆄"]
    qc = circuito_simbolico(comando)
    simulador = AerSimulator()
    resultado = simulador.run(transpile(qc, simulador), shots=1000).result()
    print(resultado.get_counts())
