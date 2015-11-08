# openCV Python 学习笔记
## 加载、显示和保存图像
### 一、函数简介

1. imread—读取图像  
函数原型 ：imread(filename, flags=None)  
filename ：读取的图像路径名；例如：”testdata/MotoX.jpg”。  
flags ：彩色图or灰色图，1：表示彩色图；0：表示灰色图。  

* imshow—显示图像  
函数原型 ：imshow(winname, mat)  
winname ：窗口名字；例如：”MotoX”。  
mat ：要显示的图像矩阵。  

* imwrite—保存图像   
函数原型 ： imwrite(filename, img, params=None)    
filename ：保存到的图像路径名；例如：”testdata/NewMotoX.jpg”。   
img ：要保存的图像矩阵；例如：image。  
params ：缺省的参数。  

### 二、实例演练
从硬盘中加载一幅图像并显示和保存图像，代码如下：

```python
#encoding:utf-8
#
#读入并显示图像
#
import cv2
image = cv2.imread('testdata/MotoX.jpg')#打开图像
print "图像宽度:%d个像素" % (image.shape[1])#获取图像的宽度
print "图像高度:%d个像素" % (image.shape[0])#获取图像的高度
print "图像通道数: %d" % (image.shape[2])#获取图像的通道数
cv2.imshow("Image",image)   #显示图像
cv2.imwrite('testdata/NewMotoX.jpg',image)#保存图像到:/testdata/NewMotoX.jpg
cv2.waitKey(0)  #程序暂停
```

#### 结果如下：
```
图像宽度:675个像素  
图像高度:600个像素  
图像通道数: 3
```
![python learning 1](//ww1.sinaimg.cn/large/61b54654gw1extxgv8d1lj21cu10mnhz.jpg)

## 访问与操作像素

### 一、函数简介

1. 获取三维矩阵(i,j)处的元素
(b,g,r) = image[i,j]，image大小为：MxNxK。

* 获取三维矩阵的子矩阵——第i行到第j行与第m列到第n列的交叉部分
newImage = image[i:j,m:n]，image大小为：MxNxK。


### 二、实例演练

1. 访问图像（0,0）处的像素并更改；
* 访问图像第0行到第100行与第0列到第100列的交叉部分并更改；

```python
#encoding:utf-8
import cv2
#
#Lesson 2 访问与操作像素
#
#
#Lesson 2 访问与操作像素
#

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
```

#### 结果如下：

```
位置(100,100)处的像素 - 红:130,绿:203,蓝:72
位置(100,100)处的像素 - 红:200,绿:150,蓝:100
[[[100 150 200]
  [ 74 206 129]
  [ 73 208 128]
  ...,
  [ 63 150 112]
  [ 66 153 115]
  [ 68 155 117]]

 [[ 74 207 134]
  [ 77 212 134]
  [ 78 215 134]
  ...,
  [ 54 149 104]
  [ 57 152 108]
  [ 59 154 110]]

 [[ 75 208 135]
  [ 77 212 136]
  [ 79 215 137]
  ...,
  [ 46 145  99]
  [ 51 150 104]
  [ 54 153 107]]

 ...,
 [[ 43 135 100]
  [ 43 130  96]
  [ 50 134 100]
  ...,
  [ 32 108  84]
  [ 35 113  89]
  [ 38 116  92]]

 [[ 46 138 103]
  [ 42 129  95]
  [ 39 123  89]
  ...,
  [ 40 118  94]
  [ 34 115  90]
  [ 30 111  86]]

 [[ 51 143 108]
  [ 42 129  95]
  [ 26 110  76]
  ...,
  [ 53 134 109]
  [ 56 139 114]
  [ 57 140 115]]]
```
![corner](//ww1.sinaimg.cn/large/61b54654gw1extzi2o1hhj20b406s74j.jpg)

![Updated](//ww4.sinaimg.cn/large/61b54654gw1extzinxqnyj211i0yktmf.jpg)
