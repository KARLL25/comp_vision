import numpy as np
from scipy.signal import correlate2d

def read_image_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    image_data = np.array([list(map(int, line.split())) for line in lines])

    return image_data

img1_data = read_image_data('img1.txt')
img2_data = read_image_data('img2.txt')

correlation = correlate2d(img1_data, img2_data, mode='same', boundary='fill', fillvalue=0)

y, x = np.unravel_index(np.argmax(correlation), correlation.shape)

print(f'Смещение по вертикали (y): {y}')
print(f'Смещение по горизонтали (x): {x}')
