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
