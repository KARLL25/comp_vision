import numpy as np

def read_image_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    
    max_size_mm = float(lines[0].split()[0])
    
    
    image_data = np.array([list(map(int, line.split())) for line in lines[2:]])
    
    return max_size_mm, image_data


filenames = ['figure1.txt', 'figure2.txt', 'figure4.txt', 'figure5.txt', 'figure6.txt']

for filename in filenames:
    max_size_mm, image_data = read_image_data(filename)
    
    
    resolution_mm_per_pixel = max_size_mm / image_data.shape[1]
    
    print(f'Изображение {filename}: Номинальное разрешение = {resolution_mm_per_pixel} мм/пиксель')
