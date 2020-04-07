import cv2 as cv

# 从文件加载图像
src = cv.imread('./example/02/input.png')

# 创建一个窗口
cv.namedWindow('input', cv.WINDOW_AUTOSIZE)

# 在指定的窗口中显示图像
cv.imshow('input', src)

# 等待按键 参数：delay-延迟（以毫秒为单位）。0是表示“永远”的特殊值。
cv.waitKey(0)

# 销毁所有HighGUI窗口
cv.destroyAllWindows()


# https: // docs.opencv.org/3.0-beta/modules/highgui/doc/user_interface.html?highlight = namedwindow  # imshow# 
