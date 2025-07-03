from sklearn.neighbors import KDTree
import numpy as np

class FractalKDStorage:
    def __init__(self):
        self.storage = []
        self.kdtree = None

    def agregar_glifo(self, glifo, metadata):
        # Comprime: guarda parámetros, semilla y centroide
        compressed_data = (
            metadata['parametros'],
            metadata['semilla'],
            np.mean(glifo, axis=0)
        )
        self.storage.append(compressed_data)

    def construir_indice(self):
        data_points = [x[2] for x in self.storage]
        self.kdtree = KDTree(np.array(data_points))

    def buscar_similar(self, glifo_muestra, k=5):
        query_point = np.mean(glifo_muestra, axis=0).reshape(1, -1)
        dist, idx = self.kdtree.query(query_point, k=k)
        return [self.storage[i] for i in idx[0]]
