import cv2
img = cv2.imread('../anh.jpg')
change = 1
def get_change(pos):
    global change
    change = pos / 100
cv2.namedWindow('Trackbar')
cv2.createTrackbar('Thu phong', 'Trackbar', 0,200,get_change)
while True:
    new_img = cv2.resize(img,None, fx = change, fy = change, interpolation = cv2.INTER_LINEAR)
    cv2.imshow('Trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()
    
