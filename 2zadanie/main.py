import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation, binary_opening, binary_closing)

from skimage.measure import label


wires =np.load(r"wires6.npy")
struct = np.ones((3,2))

labeled = label(wires)
for lb in range(1, np.max(labeled)+1):
    new_image = np.zeros_like(wires)
    new_image[labeled==lb] = 1
    eroded_wire = binary_erosion(new_image, struct)
    parts = np.max(label(eroded_wire))

    if parts == 1:
        print(f"Провод №{lb} не порван.")
    else:
        print(f"Провод №{lb} порван на {parts} части.")




plt.subplot(121)
plt.imshow(labeled)
plt.show()

