import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation, binary_opening, binary_closing
from skimage.measure import label

def process_binary_image(pic):
    def print_type_info(mask, label_func):
        result = label(label_func(pic, mask)).max()
        return result

    mask1 = np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1]])

    mask2 = np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [1, 1, 0, 0, 1, 1],
                     [1, 1, 0, 0, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1]])

    mask3 = np.array([[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1],
                      [1, 1, 0, 0, 1, 1],
                      [1, 1, 0, 0, 1, 1]])

    mask4 = np.array([[0, 0, 1, 1, 1, 1],
                      [0, 0, 1, 1, 1, 1],
                      [0, 0, 0, 0, 1, 1],
                      [0, 0, 0, 0, 1, 1],
                      [0, 0, 1, 1, 1, 1],
                      [0, 0, 1, 1, 1, 1]])

    mask5 = np.array([[0, 0, 1, 1, 1, 1],
                      [0, 0, 1, 1, 1, 1],
                      [0, 0, 1, 1, 0, 0],
                      [0, 0, 1, 1, 0, 0],
                      [0, 0, 1, 1, 1, 1],
                      [0, 0, 1, 1, 1, 1]])

    print(f"Общее количество объектов на бинарном изображении: {np.max(pic)}")
    print(f"Type 1: {print_type_info(mask1, binary_opening)}")
    print(f"Type 2: {print_type_info(mask4, binary_opening)}")
    print(f"Type 3: {print_type_info(mask5, binary_opening)}")
    print(f"Type 4: {print_type_info(mask2, binary_opening) - print_type_info(mask1, binary_opening)}")
    print(f"Type 5: {print_type_info(mask3, binary_opening) - print_type_info(mask1, binary_opening)}")


pic = np.load("psnpy.txt")
pic = label(pic)

# Обработка изображения
process_binary_image(pic)
