import cv2
img = cv2.imread('../anh.jpg')
kernel_size = 1
def get_kernel(pos):
    global kernel_size
    kernel_size = min(pos, img.shape[0])
    kernel_size += (1 - kernel_size % 2)
cv2.namedWindow('Trackbar')
cv2.createTrackbar('Blur','Trackbar', 0,255,get_kernel)
while True:
    new_img = cv2.medianBlur(img, kernel_size)
    cv2.imshow('Trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()