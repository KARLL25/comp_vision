import cv2
from scipy.spatial import distance

total_pencils_count = 0

for current_img in range(1, 13):
    raw_image = cv2.imread(f"images/img ({current_img}).jpg")
    grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(grayscale_image, (7, 7), 0)
    _, thresholded_image = cv2.threshold(blurred_image, 120, 255, 0)
    contours, _ = cv2.findContours(thresholded_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    current_pencil_number = 1
    for current_contour in contours:
        x, y, w, h = cv2.boundingRect(current_contour)
        points_of_box = cv2.boxPoints(cv2.minAreaRect(current_contour))
        width_euclidean = distance.euclidean(points_of_box[0], points_of_box[1])
        height_euclidean = distance.euclidean(points_of_box[0], points_of_box[3])
        if (height_euclidean > 3 * width_euclidean and height_euclidean > 1000) or (width_euclidean > 3 * height_euclidean and width_euclidean > 1000):
            print(f"Image: {current_img}, Pencil: {current_pencil_number}, X: {x}, Y: {y}, W: {w}, H: {h}")
            current_pencil_number += 1
            cv2.drawContours(blurred_image, [current_contour], 0, (0, 255, 0), 20)
            total_pencils_count += 1

    cv2.namedWindow(f"Processed Image {current_img}", cv2.WINDOW_KEEPRATIO)
    cv2.imshow(f"Processed Image {current_img}", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("Общее количество карандашей:", total_pencils_count)
