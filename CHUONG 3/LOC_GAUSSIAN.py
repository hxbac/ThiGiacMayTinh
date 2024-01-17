import cv2
img = cv2.imread('../anh.jpg')
kernel = 1
def get_kernel(pos):
    global kernel
    kernel = min(pos,img.shape[1])
    kernel += (1 - kernel % 2)
cv2.namedWindow('Trackbar')
cv2.createTrackbar('Gaussian','Trackbar', 0, 255,get_kernel)
while True:
    new_img = cv2.GaussianBlur(img, (kernel,kernel), 0)
    cv2.imshow('Trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
    
cv2.destroyAllWindows()
    