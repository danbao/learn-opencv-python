# openCV Python 学习笔记
## 加载、显示和保存图像
### 一、函数简介

1. imread—读取图像  
函数原型 ：imread(filename, flags=None)  
filename ：读取的图像路径名；例如：”testdata/MotoX.jpg”。  
flags ：彩色图or灰色图，1：表示彩色图；0：表示灰色图。  

2. imshow—显示图像  
函数原型 ：imshow(winname, mat)  
winname ：窗口名字；例如：”MotoX”。  
mat ：要显示的图像矩阵。  

3. imwrite—保存图像   
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
![python learning 1](http://ww1.sinaimg.cn/large/61b54654gw1extxgv8d1lj21cu10mnhz.jpg)

## 访问与操作像素

### 一、函数简介

1. 获取三维矩阵(i,j)处的元素   
(b,g,r) = image[i,j]，image大小为：MxNxK。

2. 获取三维矩阵的子矩阵——第i行到第j行与第m列到第n列的交叉部分   
newImage = image[i:j,m:n]，image大小为：MxNxK。


### 二、实例演练

1. 访问图像（0,0）处的像素并更改；  
2. 访问图像第0行到第100行与第0列到第100列的交叉部分并更改；

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
![corner](http://ww1.sinaimg.cn/large/61b54654gw1extzi2o1hhj20b406s74j.jpg)

![Updated](http://ww4.sinaimg.cn/large/61b54654gw1extzinxqnyj211i0yktmf.jpg)


## 基本绘图

### 一、函数简介

1. zeros—构造全0矩阵  
函数原型：zeros(shape, dtype=None, order=’C’)  
shape：矩阵大小；例如：300x300  
dtype：数据类型；例如：”uint8”  
order：数据排列顺序，默认按列排的  

2. line—画线
函数原型：line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)  
img：在img上绘图  
pt1：起点；例如：(0,0)  
pt2：终点；例如：(300,300)  
color：线的颜色；例如：(0,255,0)(绿色)  
thickness：线的粗细程度，例如：-1,1,2,3…  
其它参数默认即可。

3. rectangle—画矩形
函数原型：rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)  
img：在img上绘图  
pt1：起点；例如：(0,0)  
pt2：终点；例如：(300,300)  
color：线的颜色；例如：(0,255,0)(绿色)  
thickness：线的粗细程度，例如：-1,1,2,3…  
其它参数默认即可。  

4. circle—画圆形
函数原型：circle(img, center, radius, color, thickness=None, lineType=None, shift=None)  
img：在img上绘图  
center：圆心；例如：(0,0)  
radius：半径；例如：20  
color：线的颜色；例如：(0,255,0)(绿色)  
thickness：线的粗细程度，例如：-1,1,2,3…  
其它参数默认即可。  

5. randint—产生[low,high)中的随机整数
函数原型：randint(low, high=None, size=None)  
low：区间下界;例如：0  
high：区间上界；例如：256  
size：个数；例如：size = (2,)，产生2个随机整数  

### 二、 实例演练
1. 画一条绿线
2. 画一条红线
3. 画一个绿色矩形
4. 画一个红色矩形
5. 画一个蓝色矩形
6. 画同心圆
7. 随机画圆

```python
#encoding:utf-8

#
#Lesson 3 基本绘图
#

import numpy as np
import cv2

canvas = np.zeros((300,300,3),dtype="uint8")
#画绿线
green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green,2)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画红线
red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red,3)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画绿色矩形
cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画红色矩形
cv2.rectangle(canvas,(50,200),(200,225),red,5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画蓝色矩形
blue = (255,0,0,)
cv2.rectangle(canvas,(200,50),(225,125),blue,-1)#-1表示实心
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画圆1——有规律的画圆
canvas = np.zeros((300,300,3),dtype="uint8")#重新初始化变量canvas(三维的矩阵)
(centerX,centerY) = (canvas.shape[1] / 2,canvas.shape[0] / 2)#获取图像中心
white = (255,255,255)#设置白色变量
for r in xrange(0,175,25):
    cv2.circle(canvas,(centerX,centerY),r,white)#circle(图像，圆心，半径，颜色)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画圆2——随机画圆
for i in xrange(0,25):
    radius = np.random.randint(5,high = 200)#生成1个[5,200)的随机数
    color = np.random.randint(0,high = 256,size = (3,)).tolist()#生成3个[0,256)的随机数
    pt = np.random.randint(0,high = 300,size = (2,))#生成2个[0,300)的随机数
    cv2.circle(canvas,tuple(pt),radius,color,-1)#画圆
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
```

### 三、结果如下：
1. 绿线  
![绿线](http://ww1.sinaimg.cn/large/61b54654gw1exu1nk2463j20go0hw3z3.jpg)

2. 红线  
![红线](http://ww2.sinaimg.cn/large/61b54654gw1exu1o38l4fj20go0hw0tv.jpg)

3. 绿色矩形
![绿色矩形](http://ww1.sinaimg.cn/large/61b54654gw1exu1odgvavj20go0hwab9.jpg)

4. 红色矩形
![红色矩形](http://ww4.sinaimg.cn/large/61b54654gw1exu1oqisvqj20go0hw3zt.jpg)

5. 蓝色矩形
![蓝色矩形](http://ww1.sinaimg.cn/large/61b54654gw1exu1owxkazj20go0hw0u1.jpg)

6. 同心圆
![同心圆](http://ww1.sinaimg.cn/large/61b54654gw1exu1p4ise4j20go0hwwfv.jpg)

7. 随机圆
![随机圆](http://ww1.sinaimg.cn/large/61b54654gw1exu1p9hkl7j20go0hwq3f.jpg)
