# 面试题
将见过的面试题和自己想到查到的回答

* [1. 训练加速](#1.训练加速)
    * 数据并行
    * 数据并行(nn.distributed) \* [todo]
    * 模型并行
    * pytorch的dataparallel

* [2. 目标检测](#2.目标检测) 
    * 1.算法有哪些？他们的对比？
        * RCNN：
        * fast RCNN
        * faster RCNN
        * YOLO
        * SSD
    * 2.简述一下YOLOv2的原理，v1和v2有什么区别？
    * 3.非极大抑制是什么，有什么作用？
    * 4.如何实现mOU 和非极大抑制？即手推计算过程。
    * 5.nms的发展（greedy-nms，soft-nms，fast-nms，matrix-nms） \* [todo]
    * 6.YOLOv2为什么将输入尺寸从448降到416 \* [todo]
    * 7.YOLOv2对于anchor的使用与faster-rcnn有何不同
    * 8.YOLOv2,v3一个anchor可以对应几个GT？SSD呢？RCNN系列呢？
    * 9.YOLOv3对于v2做了怎样的改进？
    * 10.YOLOv2与v3筛选正负样本的方式类似，具体是怎样进行的？这种操作解决了什么问题？
    * 11.YOLOv3的多尺度输出结构与FPN有何不同？
    * 12.YOLOv2,v3的anchor聚类如何做？指标是什么？
    * 13.FPN的多尺度输出结构与SSD的多尺度输出结构哪个效果更好
    * 14.faster-rcnn在撒anchor的时候，是如何把特征图坐标映射到图像上的？
    * 15.faster-rcnn的OHEM与ssd的OHEM有何不同
    * 16.roi pooling与roi align的具体操作
    * 17.retinanet解决了以往one-stage检测器的什么问题
    * 18.Focal loss一定有效吗？为什么？试举出一个例子
    * 19.介绍cascade-RCNN和DCN模块。Cascade-rcnn解决了什么问题？cascade-RCNN一般选用几个阶段？
    * 20.anchor-free的方式大概分为哪两种？各有什么特点？
    * 21.coco的mAP的计算公式

* [3. 循环卷积神经网络](#3.循环卷积神经网络) 
    * 1.LSTM为什么会导致梯度爆炸？要如何解决？

* [4. 语义分割](#4.语义分割) 
    * 1.主要语义分割的算法有哪些，他们有什么区别？
    * 2.deeplabv3的核心是什么？
    * 3.感受野会受到什么因素的影响？怎么影响？
    * 4.介绍空洞卷积以及DeepLabv3中的ASPP模块 \* [todo]
    * 5.双线性插值，转置卷积和反卷积的区别与联系 \* [todo]
    * 6.介绍语义分割、实例分割和全景分割 \* [todo]
    * 7.后处理方法：CRF \* [todo]

* [5. Backbone](#5.Backbone) 
    * 1.resnet中的恒等快捷连接在前向传播和反向传播都有什么作用？
    * 2.ResNet和ResNeXt的区别 \* [todo]
    * 3.Inception中的deep supervision有什么作用 \* [todo]  
    * 4.resnet的shortcut结构有什么缺点?如何改进? \* [todo]    
    * 5.resnet的post activation有什么作用? \* [todo]  
    * 6.shufflenet的shuffle操作如何进行? \* [todo]  

* [6. 卷积神经网络基础](#6.卷积神经网络基础)
    * 1.Batch Normalization 在卷积神经网络中的作用是什么?
    * 2.1*1卷积的作用是什么？
    * 3.两层较小的卷积核和一个较大的卷积核比较，各有什么缺点和优点？
    * 4.不同激活函数有什么区别？
    * 5.卷积层输出大小的计算?
    * 6.dropout层为什么可以促进正则化？pytorch中dropout在训练与测试时如何使用？
    * 7.平方误差损失函数和交叉熵损失函数分别适用于什么场景？
    * 8.梯度消失/爆炸的原因?
    * 9.损失降不下来怎么办？
    * 10.weight decay vs L2 正则项
    * 11.avarage-pooling与max-pooling的区别与联系？它们的梯度反传如何进行？
    * 12.各种normalization层了解多少？(包括SyncBN)
    * 13.为什么学习率的设置要与batchsize成线型关系
    * 14.ReLU有哪些改进的方式
    * 15.神经网络中参数中的偏置bias有什么作用
    * 16.caffe的im2col是怎么操作的？ \* [todo]

* [7. 神经网络训练场景问题](#7.神经网络训练场景问题)
    * 1.怎么判断过拟合，怎么处理？
    * 2.怎么解决图像语义分割中的样本不均衡问题?

* [8. Python](#8.Python)
    * 1.装饰器是什么，有什么作用？
    * 2.迭代器
    * 3.生成器
    * 4.深拷贝与浅拷贝的区别 \* [todo]
    * 5.Python中is和==的区别
    * 6.解释with语句
    * 7.什么是面向对象？面向过程和面向对象的区别？
* [9. 机器学习](#9.机器学习)
    * 1.讲讲逻辑回归和支持向量机 \* [todo]
    * 2.手写逻辑回归的损失函数 \* [todo]
* [10.传统图像处理](#10.传统图像处理)
    * 1.直方图均衡  
    * 2.直方图匹配  
    * 3.SIFT的特点  
    * 4.刚体变换，仿射变换，透视变换（投影变换）  
    * 5.索贝尔算子长什么样?为什么长这样?
    * 6.拉普拉斯边算子?  
    * 7.图像亮度、对比度、饱和度 
    * 8.高斯金字塔与拉普拉斯金字塔