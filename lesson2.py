#encoding:utf-8

#
#Lesson 2 访问与操作像素
#


import cv2

image = cv2.imread('testdata/MotoX.jpg')#读取图像
(b,g,r) = image[100,100]#读取(100,100)像素，Python中图像像素是按B,G,R顺序存储的
print "位置(100,100)处的像素 - 红:%d,绿:%d,蓝:%d" %(r,g,b)#显示像素值
image[100,100] = (100,150,200)#更改位置(100,100)处的像素
(b,g,r) = image[100,100]#再次读取(0,0)像素
print "位置(100,100)处的像素 - 红:%d,绿:%d,蓝:%d" %(r,g,b)#显示更改后的像素值
corner = image[100:200,100:200] #读取像素块
cv2.imshow("Corner",corner) #显示读取的像素块
print corner #打印出像素块
cv2.waitKey(0)#程序暂停
image[100:200,100:200] = (255,255,255) #更改读取的像素块
cv2.imshow("Updated",image) #显示图像
cv2.waitKey(0)#程序暂停