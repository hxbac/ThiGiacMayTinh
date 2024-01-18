# Import Thư viện
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("D:\\Image.jpg")

##################################################################

# Thay đổi kích thước ảnh

# img là tên biến ảnh đầu vào
# 500, 500 là kích thước sau khi thay đổi   w, h
image = cv2.resize(img, (500, 500))

##################################################################

# Thay đổi kích thước ảnh trong Trackbar

# Image là tên cữa sổ đầu vào
cv2.resizeWindow("Image", 500, 500)

##################################################################

# Chiếu phối cảnh ảnh

# import thư viện numpy
import numpy as np
# pts1 chứa toạ độ 4 điểm cần cắt (Mở Paint để check toạ độ)
# pts2 chứa toạ độ 4 điểm của hình sau khi cắt
pts1 = np.float32([[170,2],[668,6],[100,338],[639,397]])
pts2 = np.float32([[0,0],[210,0],[0,297],[210,297]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(210,297))

##################################################################

# Ảnh xám
anh_xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

##################################################################

# Ảnh âm bản
am_ban = 255 - img

##################################################################

# In ra giá trị màu tại điểm có toạ độ nhập vào
x = int(input("Nhập tọa độ x: "))
y = int(input("Nhập tọa độ y: "))
color = img[x, y]
print("Giá trị màu tại điểm ảnh ({}, {}): {}".format(x, y, color))

##################################################################

img = cv2.imread("")
print("Kích thước của ảnh là: {}".format(img.shape))

##################################################################

# Hàm phân ngưỡng (Lưu ý: ảnh đầu vào là ảnh xám)
# Phân ngưỡng nhị phân
_, nhi_phan = cv2.threshold(anh_xam, 120, 255, cv2.THRESH_BINARY)

# Phân ngưỡng thích nghi 
thich_nghi = cv2.adaptiveThreshold(anh_xam, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Phân ngưỡng Otsu
_, otsu = cv2.threshold(anh_xam, 0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

##################################################################

# Hàm lọc ảnh
# Lọc trung bình
# + BLur
blur = cv2. blur(img, (5,5))

# + filter 2D
# Tạo ma trận 1
import numpy as np
kernel = np.ones((5,5), np.uint8)/25
filter2d = cv2.filter2D(img, -1, kernel) 

# Lọc trung vị (medianBlur)
medianBlur = cv2.medianBlur(img, 5)

# Lọc GaussianBlur
GaussianBlur = cv2.GaussianBlur(img, (5,5), 0)


# Lọc song phương
song_phuong = cv2.bilateralFilter(img, 9, 75, 75)

# ##################################################################

# Các hàm tách biên (Lưu ý: Tất cả các ảnh đầu vào là ảnh phân ngưỡng)
# Tách biên Canny
Canny = cv2.Canny(nhi_phan, 100, 200)

# Tách biên Sobel
grayx = cv2.Sobel(nhi_phan, cv2.CV_64F, 1, 0, ksize = 3)
grayy = cv2.Sobel(nhi_phan, cv2.CV_64F, 0, 1, ksize = 3)
absx = cv2.convertScaleAbs(grayx)
absy = cv2.convertScaleAbs(grayy)
Sobel = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)

# Tách biên laplacian
Laplacian = cv2.convertScaleAbs(cv2.Laplacian(nhi_phan, cv2.CV_64F, ksize = 3))

# ##################################################################

# Phép co, giãn, mở, đóng ảnh (Ảnh đầu vào là ảnh nhị phân) 
# Tạo ma trận Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# Phép co
erode = cv2.erode(nhi_phan, kernel, iterations=1)
# Phép giãn
dilate = cv2.dilate(nhi_phan, kernel, iterations=1)
# Phép mở
opening = cv2.morphologyEx(nhi_phan, cv2.MORPH_OPEN, kernel)
# Phép đóng
closing = cv2.morphologyEx(nhi_phan, cv2.MORPH_CLOSE, kernel)

##################################################################

# Tìm và vẽ Contours (Ảnh đầu vào là ảnh phân ngưỡng nhị phân)
tim,_ = cv2.findContours(nhi_phan, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# (0,0,255): contours màu đỏ, 
# (255,0,0): contours màu xanh da trời, 
# (0, 255, 0): contours màu xanh lá cây
anh_contour = cv2.drawContours(img.copy(), tim, -1, (0, 255, 0), 2)

# ##################################################################

# Cắt ảnh bắt đầu tại điểm (x1, y1) kết thúc tại điểm (x2, y2)
x1 = int(input("Nhap toa do x1: "))
y1 = int(input("Nhap toa do y1: "))

x2 = int(input("Nhap toa do x2: "))
y2 = int(input("Nhap toa do y2: "))
anh_cat = img[y1:y2, x1:x2]

# cắt ảnh nhập chiều rộng, chiều cao
chieu_rong = int(input("Nhap chieu rong: "))
chieu_cao = int(input("Nhap chieu cao: "))
anh_cat = img[0:chieu_cao, 0:chieu_rong]

# cắt ảnh nhập toạ độ trên trái, chiều rộng, chiều cao
x1 = int(input("Nhap toa do x1: "))
y1 = int(input("Nhap toa do y1: "))
chieu_rong = int(input("Nhap chieu rong: "))
chieu_cao = int(input("Nhap chieu cao: "))
anh_cat = img[y1:y1 + chieu_cao, x1: x1 + chieu_rong]

# ##################################################################

# Thay đổi độ sáng (beta), độ tương phản (alpha)
output = cv2.convertScaleAbs(img, alpha = 1, beta = 20)

# ##################################################################

# Xoay ảnh
# Đọc kích thước ảnh
(h,w) = img.shape[:2]
# Tạo tâm xoay M
# (w/2, h/2): tâm xoay ở giữa, 30 là xoay sang trái 30 độ
M = cv2.getRotationMatrix2D((w/2, h/2), 30, 1)
output = cv2.warpAffine(img, M,(w,h))

# ##################################################################

# Dịch ảnh
# import thư viện numpy
import numpy as np
# Đọc kích thước ảnh
(h, w) = img.shape[:2]
# Tạo ma trận dịch ảnh
# Tx dương dịch ảnh sang phải, Tx âm dịch ảnh sang trái
# Ty dương dịch ảnh xuống dưới, Ty âm dịch ảnh lên trên
M = np.float32([[1,0,Tx],[0,1,Ty]])
output = cv2.warpAffine(img, M, (w,h))

# ##################################################################

# Lấy khoảng Trackbar 
cv2.createTrackbar('Thu phong','Image',50,100, get_ksize)
scale = cv2.getTrackbarPos("Thu phong", "Image")/100.0 + 0.5

# Thu phóng Ảnh
# fx, fy là 2 tham số lấy từ Trackbar
output = cv2.resize(img, None, fx = fx, fy = fy, interpolation = cv2.INTER_LINEAR)

# ##################################################################

# Tạo điều kiện cho Trackbar = 0
x = 0
def get_ksize(pos):
    global x
    x = pos if pos % 2 != 0 else pos + 1


# ##################################################################

# Các bước tạo Trackbar
# B1: Tạo biến và gán giá trị cho biến, số lượng biến tuỳ theo yêu cầu đề
x = 1
# B2: Tạo hàm lấy giá trị cho biến
def get_x(pos):
    global x
    x = pos
# B3: Tạo cữa sổ hiển thị Trackbar 
# (Lưu ý: Đặt trùng tên với phần imshow để Trackbar hiện chung với ảnh)
cv2.namedWindow("Image")
# B4: Tạo Trackbar ("Tên Trackbar","Tên cữa số hiển thị", "Ngưỡng dưới", "Ngưỡng trên", "Tên Hàm")
cv2.createTrackbar('Blur','Image',0,255,get_x)
# B5: Khởi tạo vòng lặp 
while True:
    # Thay các hàm theo chức năng vào và sửa tên biến 
    # Tuỳ vào đề sẽ có các hàm khác nhau
    blur = cv2.blur(img,(x,x))
    # Show ảnh vừa thay đổi lên
    cv2.imshow("Image", blur)
    # Tạo điều kiện thoát chương trình
    if cv2.waitKey(1) == ord('q'):
        break

# ##################################################################

# Hiện ảnh trên Matplotlib
# Import thư viện Matplotlib
import matplotlib.pyplot as plt
# Chia vùng, show ảnh lên và đổi lại màu
# Trong đó subplot(221) là 2 hàng, 2 cột và hiện ở vị trí thứ 1
# cv2.cvtColor(img, cv2.COLOR_BGR2RGB) để đổi lại hệ màu cho ảnh
plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(222), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(223), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(224), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Show Matplotlib lên
plt.show()

##################################################################

cv2.imshow("Image", anh_cat)
cv2.waitKey(0)
cv2.destroyAllWindows()
