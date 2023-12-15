import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

def process_data(file_path):
    data = np.load(file_path)
    rotated_data = np.rot90(data, k=-1)
    flipped_data = np.fliplr(rotated_data)
    return flipped_data

def plot_trajectories(x, y, label, marker):
    plt.scatter(x, y, label=label, marker=marker, alpha=0.5)

x_object1, y_object1, x_object2, y_object2 = [], [], [], []

for i in range(100):
    file_path = f'out/h_{i}.npy'

    processed_data = process_data(file_path)

    detected_regions = sorted(regionprops(label(processed_data)), key=lambda region: region.area)

    if len(detected_regions) >= 2:
        (x1, y1), (x2, y2) = [region.centroid for region in detected_regions[:2]]
        x_object1.append(x1)
        y_object1.append(y1)
        x_object2.append(x2)
        y_object2.append(y2)

plt.title("Траектория движения")
plt.plot(x_object1, y_object1, label='Object 1')
plt.plot(x_object2, y_object2, label='Object 2')
plt.legend()
plt.show()
