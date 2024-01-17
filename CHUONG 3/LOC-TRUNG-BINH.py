import cv2
img = cv2.imread('../anh.jpg')

kernelW = 1
kernelH = 1

def get_kernelW(pos):
    global kernelW
    kernelW = min(pos,img.shape[1])
def get_kernelH(pos):
    global kernelH
    kernelH = min(pos, img.shape[0])
    
cv2.namedWindow('Trackbar')
cv2.createTrackbar('Kernel W','Trackbar', 0,255,get_kernelW)
cv2.createTrackbar('Kernel H','Trackbar',0,255,get_kernelH)

while True:
    kernel_size = (kernelW, kernelH)
    new_img = cv2.blur(img, kernel_size)
    cv2.imshow('Trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()