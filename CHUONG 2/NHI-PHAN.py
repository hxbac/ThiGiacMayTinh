import cv2
img = cv2.imread('../anh.jpg')

binary = 1
def get_binary(pos):
    global binary
    binary = pos

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('trackbar')
cv2.createTrackbar('nhi phan','trackbar', 0,255,get_binary)

while True:
    ret,new_img = cv2.threshold(img_gray, binary, 255, cv2.THRESH_BINARY)
    cv2.imshow('trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()