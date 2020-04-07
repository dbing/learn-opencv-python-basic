import cv2 as cv

# 从文件加载图像
src = cv.imread('./example/02/input.png')

# 创建一个窗口
cv.namedWindow('input', cv.WINDOW_AUTOSIZE)

# 指定窗口展示图像
cv.imshow('input', src)

# 将图像从一种颜色空间转换为另一种颜色空间
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# 将图像保存到指定文件
cv.imwrite('./example/02/gray.png', gray)

cv.imshow('gray', gray)
cv.waitKey(0)
cv.destroyAllWindows()


# https: // docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html?highlight = imwrite  # cv2.imwrite
