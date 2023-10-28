import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label

def area(labeled, label=1):
    return (labeled[labeled == label] / label).sum()

areas = {69:0,
         145:0,
         305:0,
         609:0}

coins = np.load("coins.npy.txt")
labeled = label(coins)

for lb in range(1, np.max(labeled)+1):
    res = area(labeled,lb)
    for j in areas:
        if j==res:
            areas[j] +=1

sum = areas[69] * 1 + areas[145] * 2 + areas[305] * 5 + areas[609] * 10

print(sum)

    




# plt.imshow(labeled)
# plt.show()
