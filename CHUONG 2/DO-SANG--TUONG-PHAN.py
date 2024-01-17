import cv2
img = cv2.imread('../anh.jpg')
beta = 1
alpha = 1
def get_beta(pos):
    global beta
    beta = pos
def get_alpha(pos):
    global alpha
    alpha = pos / 10

cv2.namedWindow('Trackbar')
cv2.createTrackbar('Do sang','Trackbar', 0 ,255,get_beta)
cv2.createTrackbar('Tuong phan', 'Trackbar', 0, 255,get_alpha)
while True:
    new_img = cv2.convertScaleAbs(img,None,alpha,beta)
    cv2.imshow('Trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()