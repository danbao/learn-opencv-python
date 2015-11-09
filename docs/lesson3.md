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
