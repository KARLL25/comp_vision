import cv2
import numpy as np

def process_color(image, lower_bound, upper_bound, color_name):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_shapes, rectangles_count, circles_count = 0, 0, 0
    color_dict = {'red': (0, 0, 255), 'blue': (255, 0, 0), 'green': (0, 255, 0),
                  'pink': (255, 0, 255), 'yellow': (0, 255, 255)}

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            rectangles_count += 1
            draw_contour(image, contour, color_dict[color_name])
        elif len(approx) >= 6:
            circles_count += 1
            draw_contour(image, contour, color_dict[color_name])

        total_shapes += 1

    return total_shapes, rectangles_count, circles_count

def draw_contour(image, contour, color):
    cv2.drawContours(image, [contour], -1, color, 2)

def display_results(color_name, total_shapes, rectangles_count, circles_count):
    print(f"{color_name.capitalize()} objects:\n")
    print(f"Всего фигур: {total_shapes}")
    print(f"Кругов: {circles_count}")
    print(f"Квадратов: {rectangles_count}\n")

def main():
    image = cv2.imread('balls_and_rects.png')

    color_ranges = {'red': ([0, 100, 100], [10, 255, 255]),
                    'green': ([40, 50, 50], [80, 255, 255]),
                    'blue': ([110, 50, 50], [130, 255, 255]),
                    'pink': ([140, 100, 100], [170, 255, 255]),
                    'yellow': ([20, 100, 100], [40, 255, 255])}

    total_shapes_all = 0

    for color_name, (lower_bound, upper_bound) in color_ranges.items():
        total_shapes, rectangles_count, circles_count = process_color(image, np.array(lower_bound), np.array(upper_bound), color_name)
        total_shapes_all += total_shapes
        display_results(color_name, total_shapes, rectangles_count, circles_count)

    print(f"Общее количество фигур: {total_shapes_all}")

    height, width = image.shape[:2]
    resized_image = cv2.resize(image, (800, 800))

    cv2.imshow('Detection by colors and shapes', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
