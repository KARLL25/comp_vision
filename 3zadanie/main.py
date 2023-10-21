import numpy as np
from skimage.morphology import label, binary_erosion

space = np.load(r"stars.npy")

threshold = 0
binary_space = space > threshold


plus_mask = np.array([[1, 0, 0, 0, 1],   
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0],
                      [0, 1, 0, 1, 0],
                      [1, 0, 0, 0, 1]], dtype=bool)
cross_mask = np.array([[0, 0, 1, 0, 0],   
                       [0, 0, 1, 0, 0],
                       [1, 1, 1, 1, 1],
                       [0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0]], dtype=bool)


plus_labels = label(binary_erosion(binary_space, plus_mask))
plus_count = len(np.unique(plus_labels)) - 1


cross_labels = label(binary_erosion(binary_space, cross_mask))
cross_count = len(np.unique(cross_labels)) - 1


print(f"Количество звезд в виде плюсов: {plus_count}")
print(f"Количество звезд в виде крестов: {cross_count}")
print(f"Общее количество звезд: {plus_count + cross_count}")
