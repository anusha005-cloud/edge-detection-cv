import cv2
import os

image = cv2.imread("images/sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Edge Detection")

def nothing(x):
    pass

cv2.createTrackbar("Threshold 1", "Edge Detection", 100, 255, nothing)
cv2.createTrackbar("Threshold 2", "Edge Detection", 200, 255, nothing)

while True:
    t1 = cv2.getTrackbarPos("Threshold 1", "Edge Detection")
    t2 = cv2.getTrackbarPos("Threshold 2", "Edge Detection")

    edges = cv2.Canny(gray, t1, t2)

    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Detection", edges)

    key = cv2.waitKey(1)

    if key == ord("s"):
        os.makedirs("output", exist_ok=True)
        cv2.imwrite("output/edge_output.png", edges)
        print("Image saved in output folder!")

    if key == 27:
        break

cv2.destroyAllWindows()