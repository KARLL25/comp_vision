import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion

def load_data(index):
    return np.load(f"out/h_{index}.npy")

def plot_object_trajectories(data_list):
    object_colors = {}
    object_positions = {}

    for idx, data in enumerate(data_list):
        eroded_data = binary_erosion(data)
        labeled_data = label(eroded_data)
        props = regionprops(labeled_data)

        for prop in props:
            label_value = prop.label
            y, x = prop.centroid

            color = object_colors.setdefault(label_value, 'orange' if len(object_colors) % 2 == 0 else 'green')
            if label_value in object_positions:
                prev_x, prev_y = object_positions[label_value]
                plt.plot([prev_x, x], [prev_y, y], color=color)  

            object_positions[label_value] = (x, y)

    plt.title("Траектория движения")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()

# Пример использования
data_list = [load_data(i) for i in range(100)]
plot_object_trajectories(data_list)
