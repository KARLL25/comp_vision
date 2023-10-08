import numpy as np


def read_image_data (filename):
    with open(filename, 'r') as file:
        lines = file.readlines()


    max_size_mm = float(lines[0])

    image_data = np.array([list(map(int, line.split())) for line in lines[2:]])

    return max_size_mm, image_data
