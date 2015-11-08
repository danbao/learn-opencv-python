#encoding:utf-8

#
#Lesson 1 读入并显示图像
#

import cv2

image = cv2.imread('testdata/MotoX.jpg')#打开图像
print "图像宽度:%d个像素" % (image.shape[1]) #获取图像的宽度
print "图像高度:%d个像素" % (image.shape[0]) #获取图像的高度
print "图像通道数: %d" % (image.shape[2]) #获取图像的通道数
cv2.imshow("Image",image)#显示图像
cv2.imwrite('testdata/NewMotoX.jpg',image)#保存图像到: /testdata/NewMotoX.jpg
cv2.waitKey(0)#程序暂停
