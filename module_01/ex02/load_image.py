import cv2

def test():
    image = cv2.imread('animal.jpeg')
    cv2.imshow("OpenCV Image",image)
    cv2.waitKey(0)
test()